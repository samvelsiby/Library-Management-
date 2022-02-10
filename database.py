from booksearch import * 
from bookreturn import *
from bookcheckout import * 
from bookweed import *
from pymongo import MongoClient
def read_book():
    
    Data=[]
    f=open("database.txt","r")
    for record in f:
        striprecord=record.strip()
        splitrecord=striprecord.split(",")
        Data.append(splitrecord)
        
    print("Student marks are read successfully. ")

   

    f.close()
    return Data
    


def save_data(Data):
     f=open("database.txt","w")
     for record in Data:
       newrecord="/n" +record[0]+","+record[1]+","+record[2]+","+record[3]+","+record[4]+","+record[5]
       f.write(newrecord)
     f.close()



     
         


