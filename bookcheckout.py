#----------------------------------------------bookchckout-------------------------------from datetime import date
from datetime import date



def bookcheckout(Data,bookid):
     
    x=0
    
    for record in Data:
        if bookid == (record[0]): 
           if  record[5]== "0":
             x=1

          
    return x    
           
def  intologfile(id):
    today = date.today()
    today1=str((today))
    f=open("logfile.txt","a")
    newlog= id+","+today1+","+"\n"
    f.write(newlog)
    f.close()
     
def changecode(Data,id,memberid):
    
    for record in Data:
         if record[0]==id: 
            record[5]=memberid
    f=open("database.txt","w")
    for record in Data:
       newrecord=record[0]+","+record[1]+","+record[2]+","+record[3]+","+record[4]+","+record[5]+"\n"
       f.write(newrecord)
    f.close()    
     
            