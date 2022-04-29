
#Taylor Swift Project

#creat the classes:

class UserInput:
    def __init__(self,question, options, answer_for_sql):
        self.question = question
        self.options = options
        self.answer = None
        self.answer_for_sql = answer_for_sql
        self.query_input = ""
        pass

    def ask_question(self):
        print(self.question)

    def get_answer(self):
        qlist = (self.options.keys())
        print("\nChose from:\n")
        for i in qlist:
            print(i + "\n")
        self.answer = input("Option number: ")
        return self.answer

    def answer_for_query(self):
        if self.answer == "1":
            self.query_input = self.answer_for_sql.get("1")
            return self.query_input
        if self.answer == "2":
            self.query_input = self.answer_for_sql.get("2")
            return self.query_input
        if self.answer == "3":
            self.query_input = self.answer_for_sql.get("3")
            return self.query_input
        else:
            print("Please enter a valid option number")
            self.get_answer()
            self.answer_for_query()

class Query:
    def __init__(self,*args,**kwargs):
        pass

    def get_query(self):
        query = "SELECT #whatspotifyneeds# from master_song_list m INNER JOIN key_words k on m.PK_SongID=k.FK_SongID where k.vibeID = " + third_question.query_input + " and k.SubjectID = " + second_question.query_input + "ORDER BY RAND() LIMIT 8;"
        print(query)

# define the questions
first_question = UserInput("\nWhat type of playlist are ya feelin'?", {"1. Random Taylor Swift Playlist": "1", "2. It's all about me hun": "ME", "3. It's about someone...": "3"}, None)
second_answer = {"1":"CP", "2":"EX", "3":"ND"}
second_question = UserInput("\nI got you. Who is this about then?", {"1. My current partner": "1", "2. My ex": "2", "3. So we've never actually dated but...":"3"}, second_answer)
third_answer = {"1":"P", "2":"N", "3":"IC"}
third_question = UserInput("\nHow do you feel about them?", {"1. Great!":"P", "2. Ugh I hate them": "N", "3. It's complicated...": "IC"}, third_answer)
new_query = Query()



#question order and logic

first_question.ask_question()
first_question.get_answer()

if first_question.answer == "1":
    query = "#SQL QUERY FOR RANDOM PLAYLIST"
    print(query)
if first_question.answer == "2":
    query = ""#SQL QUERY FOR ME PLAYLIST"
    print(query)
if first_question.answer == "3":
    second_question.ask_question()
    second_question.get_answer()
    second_question.answer_for_query()
    third_question.ask_question()
    third_question.get_answer()
    second_question.answer_for_query()
    new_query.get_query()
else:
    print("Please enter a valid option number")
    first_question.ask_question()
    first_question.get_answer()
