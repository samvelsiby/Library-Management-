from datetime import date
def bookreturn(Data,bookid):
     
    x=0
    
    for record in Data:
        if bookid == (record[0]): 
           if  record[5]!= "0":
             x=1

          
    return x    

def  intologfile1(Data,id):
    log=[]
    today = date.today()
    today1=str((today))
    f=open("logfile.txt","r")
    for record in f:
        striprecord=record.strip()
        splitrecord=striprecord.split(",")
        log.append(splitrecord)

    f=open("logfile.txt","w")
    for record in log:
         if record[0]==id: 
            record[2]=today1
    for record in log:
           newrecord=record[0]+","+record[1]+","+record[2]+"\n"
           f.write(newrecord)
    f.close()  


def changecode1(Data,id):
    
    for record in Data:
         if record[0]==id: 
            record[5]="0"
    
    f=open("database.txt","w")
    for record in Data:
       newrecord=record[0]+","+record[1]+","+record[2]+","+record[3]+","+record[4]+","+record[5]+"\n"
       f.write(newrecord)
    f.close()         

    