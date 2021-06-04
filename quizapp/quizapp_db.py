import sqlite3
from time import sleep
import random
from printProgressBar import *
liste = []

__all__ = ['liste', 'create_connection', 'create_table', 'getInputData', 'getWriteOnTable',
           'update_words', 'getCheckWord', 'getRandomWords', 'numberOfDbRow']

def create_connection(db_file):
    """
    Defination:
        Create a database connection to the SQlite3 
        datebase specified by the 'db_file'. 
    @params:
        :param db_file  -Required: database file (str)
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def create_table(t_name="words"):
    """
    Defination:
        Creating a table
    @params:
        :param t_name -Optional: What should be this table name?
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    sql = f"CREATE TABLE IF NOT EXISTS {t_name} ('id' INTEGER UNIQUE, 'iword' TEXT UNIQUE, 'tmeaning' TEXT, PRIMARY KEY('id'))"
    cur.execute(sql)

def getInputData(arg1, arg2):
    """
    Defination:
        takes from user that english word and its turkish means.
    @params:
        :param arg1 -Required: Defines a word it must be English. (str)
        :param arg2 -Required: Defines a word it should be Turkish or English. (str)
    """
    data_1 = numberOfDbRow() + 1
    data_2 = str(arg1).lower()  #delete the word that end's spaces
    data_3 = str(arg2).lower()
    liste.append(data_1)
    liste.append(data_2)
    liste.append(data_3)
    
def getWriteOnTable(arg=liste):
    """
    Defination:
        Overwrites the table.
    @params:
        :param arg -Optional: len(arg) must be 3 and list. (list)
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO words VALUES (?, ?, ?)""", arg)
        print("THE DATA IN PROGRESS..")
        print()
########################progress bar##########################
        a = 0
        while True:
            sleep(0.06)
            a += 1
            if a == 21:
                break
            printProgressBar(a, 20)
##############################################################
        conn.commit()
        if getCheckWord(liste[1]):
            print("Successfully added.")
        else:
            print("The word cound not be added!") 
        
    except sqlite3.IntegrityError as e:
        #Is run finally section after 'return' ? Responce: YES
        print("UPSii, this word already have in the database.", e) #send log file here.
        return False

    finally:
        liste.clear()

def update_words(row, arg1, arg2=None):
    """
    Defination:
        update 'iword', 'tmeaning' of table of 'words'\n
    @params: \n   
        :param row     -Required: Defines which within row's will doing change. (int) \n
        :param arg1    -Required: Defines new english word. (str)\n
        :param arg2    -Optional: Defines the English word's meaning in Turkish. (str) \n
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    sql = """UPDATE words
             SET iword=(?),
                 tmeaning=(?) 
             WHERE id=(?)"""
    cur.execute(sql, (arg1, arg2, int(row)))
    print("THE DATA IN PROGRESS..")
    print()
########################progress bar##########################
    a = 0
    while True:
        sleep(0.06)
        a += 1
        if a == 21:
            break
        printProgressBar(a, 20)
##############################################################
    conn.commit()
    if getCheckWord(arg1):
        print("Successfully update!")
    else:
        print("The word cound not be update!")
    #changed = conn.total_changes
    #print("The number of changes made: ", changed)

def getCheckWord(arg, t_name="words"):
    """
    Defination:
        Checking the database word
    @params:
        :param arg     -Required: A word what will checking in datebase in given table's names. (str)
        :param t_name  -Optional: 
    Return: 
        If there is which given word returns True. if not in database returns False.   
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM {} WHERE iword = (?)".format(t_name),(str(arg),)) 
    if cur.fetchall(): return True
    else: return False

def getRsample(t_name="words"):
    """
    Defination:
        Brings five words from datebase in given table's name.
    @params:
        :param t_name -Optional: A table name in database (str)
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM {}""".format(t_name))  #We chosed all datas on in the database.
    listele = cur.fetchall()  #Fetch all data we chose, recorded on a list called 'listele'. If data might lot u may face an issue.
    return print(random.sample(listele, 5))  
    

def getRandomWords(t_name="words"): #More Useful
    """
    Defination:
        Brings five words from datebase in given table.
    @params:
        :param t_name -Optional: A table name in databası (str)
    Return:
        Returns a set how five tuple choosen in database.
    """
    database = 'db.sqlite'
    conn = create_connection(database)
    cur = conn.cursor()
    myset = set() 
    while len(myset) < 5: 
        r_number = random.randrange(numberOfDbRow()+1)  
        cur.execute("""SELECT * FROM {} WHERE id = ?""".format(t_name), (r_number,))  
        myset.update(list(cur.fetchall())) 
    return myset

def numberOfDbRow(db_name="db.sqlite", t_name="words"):
    """
    Defination:
        Defines how many are there row in the given table.
    @params:
        :param db_name -Optional: Indicates that given database path. Or name.
        :param t_name  -Optional: Indicates that given within database's a table name. 
    Return:
        Returns number of rows of table as a integer.
    """
    database = db_name #this variable may write as a param.
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(t_name))
    dbDatas = cur.fetchall()
    return int(len(dbDatas))

def __test():
    # create_table()
    pass
    # x = getCheckWord("junk")
    # print(x)
    # getRandomWords()
    # getRsample()
    # print(numberOfDbRow())
    

if __name__ == '__main__':
    __test()
    exit()