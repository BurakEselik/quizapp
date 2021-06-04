"""
aim: english quiz
author: burak eselik
date:24 march 2021
"""
from time import sleep
import quizapp_db

class Quiz:
    
    def __init__(self):
        self.write1 = """         -----------------------------------------------
        |                                               |
        |            WELCOME TO THE QUIZ                | 
        |                APPLICATION                    |
        |                                         v0.1  |
         -----------------------------------------------
              """
        print(self.write1)
        self.showDisplay()

    #show console
    def showDisplay(self):
        sleep(.4)
        write2 = """
        -----------------------Main Menu-----------------------
        PLEASE TYPE&ENTER THESE KEYWORDS OF WHAT YOU WANT TO DO:
        FOR FAST QUIZ 'exe'
        FOR WORD OPERATIONS 'wop'
        FOR QUIT 'q'
        """
        print(write2)
        data1 = input("TYPE HERE :")
        sleep(.3)
        if data1 == 'exe':
            self.createQuestion()
            self.showDisplay3()

        elif data1 == 'wop':
            self.showDisplay2()
        elif data1 in 'qQ':
            self.getOut()
        else:
            print("YOU DID WRONG CHOICE!")
            self.showDisplay()
    
    def showDisplay2(self):
        sleep(.4)
        write3 = """
        ------------------Word Operation Menu------------------
        FOR ADD A NEW WORD 'add'
        FOR CHECK A WORD   'check'
        FOR UPDATE A WORD  'update'
        FOR BACK           'back'
        """
        
        print(write3)
        data2 = input("TYPE HERE :").lower()
        if data2 == 'add':
            data_1 = input("Enter English Word Here : ")
            print("Attention: You must separate different meanings with comma(,). Do not use space!")
            data_2 = input("Enter The Word Meaning Here : ")
            quizapp_db.getInputData(data_1, data_2)
            x = quizapp_db.getWriteOnTable()
            if not x: self.showDisplay()
            else: pass
            self.showDisplay()
        elif data2 == 'check':
            sleep(.6)
            which_word = input("WRITE THE WORD : ").lower()
            checked_word = quizapp_db.getCheckWord(which_word)
            if checked_word: print(f'There is the word "{(which_word)}" in the database!')
            else: print(f'The word "{(which_word)}" DOES NOT exist in the database!')
            self.showDisplay()
        elif data2 == 'update':
            data_3 = input("Enter the row id       :")
            data_4 = input("Enter English word     :").lower()
            print("Attention: You must separate different meanings with comma(,). Do not use space!")
            data_5 = input("Enter the word meainig :").lower()
            try:
                quizapp_db.update_words(int(data_3), data_4, arg2=data_5)
            except Exception as e:
                print(e)
            finally: self.showDisplay()
        elif data2 == "back":
            sleep(.6)
            self.showDisplay()
        else:
            print("You made a wrong choice. Try again!")
            self.showDisplay2()

    def createQuestion(self):
        self.answers = []
        self.questions = quizapp_db.getRandomWords()
        for i,k in enumerate(self.questions, 1):
            question = "Q{} -) {} :".format(str(i), k[1])
            answer = input(question)
            self.answers.append(answer)
        #print(self.answers)
        
    def getCheckAnswer(self):
        sleep(.4)
        score = 0
        for i, j in enumerate(self.answers):
            if j in list(self.questions)[i][2].split(","):
                score += 20
        return f"Your Score: {score}"

    def showDisplay3(self):
        sleep(.6)
        ques = list(self.questions)
        ans  = self.answers
        mtn0 = "ID"
        mtn1 = "WORD"
        mtn2 = "RIGHT ANSWER"
        mtn3 = "YOUR ANSWERS"
        mtn4 = "-"*96
        table = "{:^6}|{:^30}|{:^30}|{:^30}\n{}".format(mtn0, mtn1, mtn2, mtn3, mtn4)
        print(table) 
        for i in range(5):
            sleep(.5)
            print("{:^6}|{:^30}|{:^30}|{:^30}\n{}".format(ques[i][0], ques[i][1], ques[i][2], ans[i], mtn4))
            if i == 4:
                print("-"*41+f"{(self.getCheckAnswer())}"+"-"*41, mtn4, sep="\n")

        x = input("CONTINUE OR BACK(con/back):")
        if x == "con":
            self.createQuestion()
            self.showDisplay3()
        elif x == "back":
            self.showDisplay()
        else:
            print("WRONG CHOICE try again later!")
            self.getOut()

    def getOut(self):
        print("SEE YOUUU..")
        sleep(.7)
        exit()

    def main(self):
        pass

if __name__ == "__main__":
    instance = Quiz()
    