from dialog.schema.elements import Variable
from dialog.schema.factories.variables import NAME_RESULTS_COUNT, NAME_PAGE


class Variables:
    def create(self):
        return {
            "var_folder": {
                "@name": "Home",
                (0, "var_folder"): [
                    self.create_conversation_management(),
                    self.create_movie_search(),
                    self.create_shoe_search(),
                ],
                (1, "var"): [
                    Variable("Previous Certification Selected", "TEXT"),
                    Variable("Previous Genre Selected", "TEXT"),
                    Variable("Previous Recency Selected", "TEXT"),
                    Variable("DateTime_Current", "DATETIME", description="Current date Time for US ET"),
                    Variable("DateTime_Difference", "NUMBER"),
                    Variable("DateTime_Mentioned_ENT", "TEXT")
                ]
            }
        }

    def create_conversation_management(self):
        return {
            "@name": "Conversation Management",
            "@type": "VAR",
            "var": [
                Variable("Topic", "TEXT"),
                Variable("Request_Success", "YESNO", description="Did the user find what s/he was looking for?"),
                Variable("Terminal_Exchange", "YESNO", init_value="No",
                         description="Has the system already said goodbye?"),
                Variable("Greeting_Count", "NUMBER", init_value="0",
                         description="How many times a user says &quot;hi&quot; or &quot;howareyou&quot;"),
                Variable("Small_Talk_Count", "NUMBER", init_value="0",
                         description="How many times User engages Small Talk sequences"),

                Variable("Out-of-Scope_Count", "NUMBER", init_value="0",
                         description="How many times User engages out-of-scope sequences"),

                Variable("User_Name", "TEXT", init_value="friend"),
                Variable("First_Time", "YESNO", init_value="Yes", description="User's first time using the app."),
            ]
        }

    def create_movie_search(self):
        return {
            "@name": "Movie Search",
            "@type": "VAR",
            "var": [
                Variable("Certification_Preference", "TEXT", description="User's preferred MPAA movie rating"),
                # Variable("Genre_Preference", "TEXT", description="User's preferred movie genre."),
                Variable("Search_Now", "YESNO", init_value="No",
                         description="Tells backend when to call the movie API"),
                Variable("Selected_Movie", "TEXT"),
                Variable("ZIP_Code_Preference", "TEXT", description="User's indicated ZIP code"),
                Variable("Display_Trailer", "YESNO", init_value="No"),
                Variable("Display_Movie_Details", "YESNO", init_value="No"),

            ]
        }

    def create_shoe_search(self):
        return {
            "@name": "Product Search",
            "@type": "VAR",
            "var": [
                Variable("Style_Preference", "TEXT", description="Style of the shoe being searched for"),
                Variable("Color_Preference", "TEXT", description="Color of the shoe being searched for"),
                Variable(NAME_RESULTS_COUNT, "NUMBER", init_value="0", description="number of results found"),
                Variable(NAME_PAGE, "TEXT", init_value="new", description="For paging search results: new, next, previous, repeat"),
            ]
        }

# <var name="Search_Results" type="TEXT" description="No_Hits, One_Hit, Multiple_Hits"/>
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
