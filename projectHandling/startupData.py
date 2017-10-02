from components import create
import sqlite3 as dab
import colorama as clr
import os, time

class Data:
    compMode = "curren"
    lastProjects = None
    lastProjNames = None
    db = None
    cur = None

    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
        clr.init()
    
    #Check on the databse existance and create it if necessary with the table
    def createLPDatabase(self):
        Data.db = dab.connect("./Data/Temp/LastProjects.db")
        Data.cur = Data.db.cursor()
        Data.cur.execute('''CREATE TABLE IF NOT EXISTS ProjTable(prim INTEGER PRIMARY KEY,name TEXT,filePath TEXT, tmstp INT)''')
        Data.db.commit()

    #Insert the new projects to the database and update it if needed
    #The time the project got accessed is defined automaticly by 
    def insert(self, name, filePath):
        if(Data.lengthOfDB(self) < 6):
            Data.cur.execute("SELECT filePath  FROM ProjTable")
            #insert it into the database if there is nothing
            if(Data.lengthOfDB(self) == 0):
                    Data.cur.execute("INSERT INTO ProjTable(name, filePath, tmstp)  VALUES(?,?,?)", (name, filePath, time.time()))
                    Data.db.commit()
            else:
                #if there is something, loop throu the databse to see if it is already there
                exists = True
                for i in range(Data.lengthOfDB(self)):
                    Data.cur.execute("SELECT filePath  FROM ProjTable")
                    if Data.cur.fetchall()[i][0] == filePath:
                        exists = False
                        break
                #If it doesnt exist, insert it!
                if exists:
                    Data.cur.execute("INSERT INTO ProjTable(name, filePath, tmstp)  VALUES(?,?,?)", (name, filePath, time.time()))
                    Data.db.commit()
                else:
                    #Update the time of the project in the list
                    Data.cur.execute("SELECT filePath  FROM ProjTable")
                    Data.cur.execute("UPDATE ProjTable SET tmstp = ? where filePath = ?", (time.time(), Data.cur.fetchall()[i][0]))
                    Data.db.commit()
        else:
            #Determine the oldest project and replace it!
            oldestIndex = 0
            oldestStamp = time.time()
            Data.cur.execute("SELECT *  FROM ProjTable")
            for i in range(len(Data.cur.fetchall)):
                Data.cur.execute("SELECT tmstp  FROM ProjTable")
                if(Data.cur.fetchall()[i] < oldestStamp):
                    Data.cur.execute("SELECT tmstp  FROM ProjTable")
                    oldestStamp = Data.cur.fetchall()[i]
                    oldestIndex = i
            
            #Update the oldest project
            Data.cur.execute("UPDATE ProjTable SET name = ? where prim = ?", (name, oldestIndex))
            Data.cur.execute("UPDATE ProjTable SET filePath = ? where prim = ?", (filePath, oldestIndex))
            Data.cur.execute("UPDATE ProjTable SET tmstp = ? where prim = ?", (time.time(), oldestIndex))

    def readDB(self, row):
        Data.cur.execute("SELECT *  FROM ProjTable")
        return Data.cur.fetchall()[row]

    #Get the length of the database
    def lengthOfDB(self):
        Data.createLPDatabase(self)
        Data.cur.execute("SELECT *  FROM ProjTable")
        return len(Data.cur.fetchall())