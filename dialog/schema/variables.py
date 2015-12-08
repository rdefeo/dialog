class Variables:
    def create(self):
        return {
            "var_folder": {
                "@name": "Home",
                (0, "var_folder"): [
                    self.create_conversation_management(),
                    self.create_movie_search(),
                ],
                (1, "var"): [
                    self.create_variable("Previous Certification Selected", "TEXT"),
                    self.create_variable("Previous Genre Selected", "TEXT"),
                    self.create_variable("Previous Recency Selected", "TEXT"),
                    self.create_variable("DateTime_Current", "DATETIME", description="Current date Time for US ET"),
                    self.create_variable("DateTime_Difference", "NUMBER"),
                    self.create_variable("DateTime_Mentioned_ENT", "TEXT")
                ]
            }
        }

    def create_variable(self, name, _type, description=None, initValue=None):
        doc = {
            (0, "@name"): name,
            (1, "@type"): _type
        }
        if initValue is not None:
            doc[(2, "@initValue")] = initValue

        if description is not None:
            doc[(3, "@description")] = description

        return doc

    def create_conversation_management(self):
        return {
            "@name": "Conversation Management",
            "@type": "VAR",
            "var": [
                self.create_variable("Topic", "TEXT"),
                self.create_variable("Request_Success", "YESNO",
                                     description="Did the user find what s/he was looking for?"),
                self.create_variable("Terminal_Exchange", "YESNO", initValue="No",
                                     description="Has the system already said goodbye?"),
                self.create_variable("Greeting_Count", "NUMBER", initValue="0",
                                     description="How many times a user says &quot;hi&quot; or &quot;howareyou&quot;"),
                self.create_variable("Small_Talk_Count", "NUMBER", initValue="0",
                                     description="How many times User engages Small Talk sequences"),
                self.create_variable("Out-of-Scope_Count", "NUMBER", initValue="0",
                                     description="How many times User engages out-of-scope sequences"),
                self.create_variable("User_Name", "TEXT", initValue="friend"),
                self.create_variable("First_Time", "YESNO", initValue="Yes",
                                     description="User's first time using the app.")
            ]
        }

    def create_movie_search(self):
        return {
            "@name": "Movie Search",
            "@type": "VAR",
            "var": [
                self.create_variable("Certification_Preference", "TEXT", description="User's preferred MPAA movie rating"),
                self.create_variable("Genre_Preference", "TEXT",
                                     description="User's preferred movie genre."),
                self.create_variable("Search_Now", "YESNO", initValue="No",
                                     description="Tells backend when to call the movie API"),
                self.create_variable("Recency_Preference", "TEXT",
                                     description="If the movie is current or upcoming"),
                self.create_variable("Selected_Movie", "TEXT"),
                self.create_variable("ZIP_Code_Preference", "TEXT", description="User's indicated ZIP code"),
                self.create_variable("Display_Trailer", "YESNO", initValue="No"),
                self.create_variable("Display_Movie_Details", "YESNO", initValue="No"),

            ]
        }

#                 <var name="Search_Results" type="TEXT" description="No_Hits, One_Hit, Multiple_Hits"/>
# 4845
#                 <var name="Display_Reviews" type="YESNO" initValue="No"
# 4846
#                      description="Tells backend to display reviews for Selected_Movie"/>
# 4847
#                 <var name="Num_Movies" type="NUMBER" initValue="0" description="Number of movie search results"/>
# 4848
#                 <var name="Current_Index" type="NUMBER" initValue="0"
# 4849
#                      description="Range of movies results to display. Values: 10, 20, 30..."/>
# 4850
#                 <var name="Show_Next" type="YESNO" initValue="No"
# 4851
#                      description="Show the next batch of movie search results."/>
# 4852
#                 <var name="Show_Previous" type="YESNO" initValue="No"
# 4853
#                      description="Show previous batch of movies search results."/>
# 4854
#                 <var name="Popularity_Score" type="NUMBER"
# 4855
#                      initValue="0.5" description="Popularity score as measured by TMDB.org."/>
# 4856
#                 <var name="Total_Pages" type="NUMBER" initValue="0"
# 4857
#                      description="Total number of pages returned by TMDB"/>
# 4858
#                 <var name="Last_Results" type="YESNO" initValue="No"
# 4859
#                      description="Determines if user has hit the Last Results node before."/>
# 4860
#                 <var name="First_Results" type="YESNO" initValue="No"
# 4861
#                      description="Determines if user has gone back to first results already."/>
# 4862
#                 <var name="Page" type="TEXT" initValue="new"
# 4863
#                      description="For paging search results: new, next, previous, repeat"/>
