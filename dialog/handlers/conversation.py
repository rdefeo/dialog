from json import loads, dumps

from tornado.web import RequestHandler, Finish
from watson_developer_cloud import DialogV1 as Dialog

personalized_prompt_current_index = "UPDATE CURRENT_INDEX"  # $NON-NLS-1$
personalized_prompt_movies_returned = "UPDATE NUM_MOVIES";  # $NON-NLS-1$


class Conversation(RequestHandler):
    def data_received(self, chunk):
        pass

    def initialize(self, dialog_service: Dialog, dialog_id):
        self.dialog_service = dialog_service
        self.dialog_id = dialog_id

    def on_finish(self):
        pass

    def match_search_now_pattern(self, wdsResponseText: str):
        """
        Checks and extracts movie parameters sent by WDS
        <p>
        This will extract movie parameters sent by WDS (in the response text) when they're sent.
        </p>

        @param wdsResponseText the textual part of the response sent by WDS
        @return the JsonObject containing the response from WDS as well as the parameters and their values sent by WDS.
        """

        result = {}
        # If WDS wants us to search themoviedb then it will return a JSON
        # payload within the response. Quickly check the response for a specific token
        print(wdsResponseText)
        wds_response_test = wdsResponseText.lower()
        if "{\"search_now\":" in wds_response_test:
            idx = wdsResponseText.lower().index("{\"search_now\":")  # $NON-NLS-1$

            # token exists, parse out some extra chars from dialog.
            json = wdsResponseText[idx:].strip()
            wdsResponseText = wdsResponseText[0: idx - 1].strip()
            if json.startswith("\""):  # $NON-NLS-1$
                json = json[0:]

            if json.endswith("\""):  # $NON-NLS-1$
                json = json[0: len(json) - 1]

            element = loads(json)
            result["Params"] = element  # $NON-NLS-1$

        result["WDSMessage"] = wdsResponseText  # $NON-NLS-1$ //$NON-NLS-2$ //$NON-NLS-3$
        return result

    def get(self, *args, **kwargs):
        """

        Makes chat conversation with WDS
        <p>
        This makes chat conversation with WDS for the provided client id and conversation id, against the user input provided.
        </p>
        <p>
        When WDS has collected all the required movie preferences, it sends a bunch of movie parameters embedded in the text response and signals to discover
        movies from themoviedb.org. There may be the following kinds of discover movie calls:
        <ul>
        <li>New search: First time searching for the given set of parameters
        <li>Repeat search: Repeat the search with the same parameters (just re-display the results)
        <li>Previous search: Display the results on the previous page
        <li>Next search: Display the results on the next page
        </ul>
        Depending on the kind of call, profile variables are set in WDS and personalized prompts are retrieved to be sent back to the UI in the payload.
        </p>
        *
        * @param conversationId the conversation id for the client id specified
        * @param clientId the client id for the session
        * @param input the user's input

        :param args:
        :param kwargs:
        :return: a response containing either of these two entities- {@code WDSConversationPayload} or {@code ServerErrorPayload}
        """
        conversation_id = self.get_argument("conversationId", None)
        client_id = self.get_argument("clientId", None)
        client_input = self.get_argument("input", None)


        # long lStartTime = System.nanoTime();
        # long lEndTime, difference;
        # String errorMessage = null, issue = null;
        # String wdsMessage = null;
        # JsonObject processedText = null;
        # if (input == null || input.trim().isEmpty()) {
        #     errorMessage = Messages.getString("WDSBlueMixProxyResource.SPECIFY_INPUT"); //$NON-NLS-1$
        #     issue = Messages.getString("WDSBlueMixProxyResource.EMPTY_QUESTION"); //$NON-NLS-1$
        #     UtilityFunctions.logger.error(issue);
        #     return Response.serverError().entity(new ServerErrorPayload(errorMessage, issue)).build();
        # }
        try:
            pass
            #
            # // 1.Get all the class info from NLC and set appropriate profile variables.
            # List<ClassifiedClass> classInfo = null;
            # if(nlcService != null){
            #     if (UtilityFunctions.logger.isTraceEnabled()) {
            #         UtilityFunctions.logger.trace(Messages.getString("WDSBlueMixProxyResource.NLC_SERVICE")); //$NON-NLS-1$
            #     }
            #     // Send utterance to NLC to get user intent
            #     Classification classification = nlcService.classify(classifier_id, input);
            #     classInfo = classification.getClasses();
            #     // Set classification profile variables for WDS.
            #     List<NameValue> nameValues = new ArrayList<NameValue>();
            #     nameValues.add(new NameValue("Class1", classInfo.get(0).getName()));
            #     nameValues.add(new NameValue("Class1_Confidence", Double.toString(classInfo.get(0).getConfidence())));
            #     nameValues.add(new NameValue("Class2", classInfo.get(1).getName()));
            #     nameValues.add(new NameValue("Class2_Confidence", Double.toString(classInfo.get(1).getConfidence())));
            #     dialogService.updateProfile(dialog_id, Integer.parseInt(clientId), nameValues);
            # }
            #
            # // 2. Send original utterance to WDS
            conversation = self.dialog_service.conversation(self.dialog_id, client_input, client_id, conversation_id)
            wds_message = " ".join(conversation["response"])

            profile = self.dialog_service.get_profile(self.dialog_id, client_id)
            print(profile)

            processed_text = self.match_search_now_pattern(wds_message)
            #         WDSConversationPayload conversationPayload = new WDSConversationPayload();
            if "Params" not in processed_text:  # $NON-NLS-1$
                # We do not have enough info to search the movie db, go back to the user for more info.
                self.write(
                    dumps(
                        {
                            "clientId": client_id,  # $NON-NLS-1$
                            # TODO seems really strange!!!
                            # conversationPayload.setConversationId(clientId); //$NON-NLS-1$
                            # "conversationId": conversation_id,
                            "conversationId": client_id,
                            "input": client_input,  # $NON-NLS-1$
                            "wdsResponse": processed_text["WDSMessage"]
                        }
                    )
                )
                self.set_status(200)
                raise Finish()

                #             if (UtilityFunctions.logger.isTraceEnabled()) {
                #                 // Log the execution time.
                #                 lEndTime = System.nanoTime();
                #                 difference = lEndTime - lStartTime;
                #                 UtilityFunctions.logger.trace("Throughput: " + difference/1000000 + "ms.");
                #             }

            else:
                # Dialog says we have enough info to proceed with a search of themoviedb..
                # Find out search variables.
                params = processed_text["Params"]
                new_search = False
                previous_search = False
                next_search = False
                repeat_search = False
                page = params["Page"]
                # String page = paramsObj.get("Page").getAsString(); //$NON-NLS-1$
                # switch (page) {
                # case "new":newSearch = true; //$NON-NLS-1$
                #     break;
                # case "next":nextSearch = true; //$NON-NLS-1$
                #     break;
                # case "previous":prevSearch = true; //$NON-NLS-1$
                #     break;
                # case "repeat":repeatSearch = true; //$NON-NLS-1$
                #     break;
                # default:
                #     errorMessage = Messages.getString("WDSBlueMixProxyResource.DIALOG_UNDERSTAND_FAIL"); //$NON-NLS-1$
                #     issue = Messages.getString("WDSBlueMixProxyResource.PAGE_TYPE_NOT_UNDERSTOOD"); //$NON-NLS-1$
                #     UtilityFunctions.logger.error(issue);
                # }
                #
                # if (UtilityFunctions.logger.isTraceEnabled()) {
                #     UtilityFunctions.logger.trace(Messages.getString("WDSBlueMixProxyResource.WDS_RESPONSE") + paramsObj); //$NON-NLS-1$
                # }
                # String prompt;
                # Integer currentIndex = Integer.parseInt(paramsObj.get("Index").getAsString()); //$NON-NLS-1$
                # Integer numMovies = 0;
                # Integer totalPages = 0;
                # boolean tmdbCallNeeded = true;
                # List<NameValue> nameValues;
                # if(paramsObj.has("Total_Movies")){
                #     numMovies = Integer.parseInt(paramsObj.get("Total_Movies").getAsString());
                #     totalPages = Integer.parseInt(paramsObj.get("Total_Pages").getAsString());
                #     // If the user wishes to "go back" when the first set of results is displayed or
                #     // "show more" results when all results have been displayed already---> do not need to make a call to themoviedb.org
                #     tmdbCallNeeded = !((currentIndex <= 10 && prevSearch) || (currentIndex == numMovies && nextSearch));
                # }
                # if(tmdbCallNeeded){
                #     // Need to make a call to TMDB.
                #     int pageNum = (int) Math.ceil((float) currentIndex / 20);// round up.. 10/20 = .5 == page# 1
                #     if ((nextSearch || newSearch) && (currentIndex % 20) == 0) {
                #         pageNum++;
                #     }
                #
                #     // Decrement page num. eg.: currentIndex = 30, 23, etc. Do not decrement page num for currentIndex = 20, 36, etc.
                #     if (prevSearch && (currentIndex % 20 <= 10 && (currentIndex % 20 != 0))) {
                #         pageNum--;
                #     }
                #
                #     int currentDisplayCount = (currentIndex % 10 == 0) ? 10 : currentIndex % 10;
                #     SearchTheMovieDbProxyResource tmdb = new SearchTheMovieDbProxyResource();
                #     conversationPayload = tmdb.discoverMovies(UtilityFunctions.getPropValue(paramsObj, "Genre"),  //$NON-NLS-1$
                #             UtilityFunctions.getPropValue(paramsObj, "Rating"),  //$NON-NLS-1$
                #             UtilityFunctions.getPropValue(paramsObj, "Recency"),  //$NON-NLS-1$
                #             currentIndex, pageNum, nextSearch || newSearch);
                #     int size = conversationPayload.getMovies().size();
                #     if (prevSearch) {
                #         currentIndex -= currentDisplayCount;
                #     } else if (nextSearch || newSearch) {
                #         currentIndex += size;
                #     }
                #
                #     nameValues = new ArrayList<NameValue>();
                #     // Save the number of movies displayed till now.
                #     nameValues.add(new NameValue("Current_Index", currentIndex.toString())); //$NON-NLS-1$
                #     // Save the total number of pages in a profile variable.
                #     nameValues.add(new NameValue("Total_Pages", conversationPayload.getTotalPages().toString())); //$NON-NLS-1$
                #     // Save the total number of movies in Num_Movies.
                #     nameValues.add(new NameValue("Num_Movies", conversationPayload.getNumMovies().toString())); //$NON-NLS-1$
                #     // Set the profile variables.
                #     dialogService.updateProfile(dialog_id, Integer.parseInt(clientId), nameValues);
                # }
                # if(!tmdbCallNeeded){
                #     // Set the value of the Index_Updated profile variable to No so that WDS knows that no indices were updated.
                #     nameValues = new ArrayList<NameValue>();
                #     nameValues.add(new NameValue("Index_Updated", "No"));
                #     dialogService.updateProfile(dialog_id, Integer.parseInt(clientId), nameValues);
                #     // Set some values in the ConversationPayload which are needed by the UI.
                #     List <MoviePayload> movies = new ArrayList<MoviePayload>();
                #     conversationPayload.setMovies(movies);
                #     conversationPayload.setNumMovies(numMovies);
                #     conversationPayload.setTotalPages(totalPages);
                # }
                # If first time, get personalized prompt based on Num_Movies
                prompt = personalized_prompt_current_index;
                if new_search or repeat_search:
                    prompt = personalized_prompt_movies_returned;


                # Get the personalized prompt.
                conversation = self.dialog_service.conversation(self.dialog_id, prompt, client_id, conversation_id)
                wds_message = " ".join(conversation["response"])

                self.write(
                    dumps(
                        {
                            "clientId": client_id,  # $NON-NLS-1$
                            # TODO seems really strange!!!
                            # conversationPayload.setConversationId(clientId); //$NON-NLS-1$
                            # "conversationId": conversation_id,
                            "conversationId": client_id,
                            "input": client_input,  # $NON-NLS-1$
                            "wdsResponse": wds_message
                        }
                    )
                )
                self.set_status(200)
                raise Finish()

                # if (UtilityFunctions.logger.isTraceEnabled()) {
                #     // Log the execution time.
                #     lEndTime = System.nanoTime();
                #     difference = lEndTime - lStartTime;
                #     UtilityFunctions.logger.trace("Throughput: " + difference/1000000 + "ms.");
                # }
                # // Return to UI.
                # return Response.ok(conversationPayload, MediaType.APPLICATION_JSON_TYPE).build();

        except:
            raise
            #     } catch (ClientProtocolException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.API_CALL_NOT_EXECUTED"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.CLIENT_EXCEPTION_IN_GET_RESPONSE"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (IllegalStateException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.API_CALL_NOT_EXECUTED"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.ILLEGAL_STATE_GET_RESPONSE"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (IOException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.API_CALL_NOT_EXECUTED"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.IO_EXCEPTION_GET_RESPONSE"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (HttpException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.TMDB_API_CALL_NOT_EXECUTED"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.HTTP_EXCEPTION_GET_RESPONSE"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (WatsonTheatersException e) {
            #         errorMessage = e.getErrorMessage();
            #         issue = e.getIssue();
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (URISyntaxException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.TMDB_URL_INCORRECT"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.URI_EXCEPTION_IN_DISOVERMOVIE"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     } catch (ParseException e) {
            #         errorMessage = Messages.getString("WDSBlueMixProxyResource.TMDB_RESPONSE_PARSE_FAIL"); //$NON-NLS-1$
            #         issue = Messages.getString("WDSBlueMixProxyResource.PARSE_EXCEPTION_TMDB_GET"); //$NON-NLS-1$
            #         UtilityFunctions.logger.error(issue, e);
            #     }
            #     return Response.serverError().entity(new ServerErrorPayload(errorMessage, issue)).build();
            # }
