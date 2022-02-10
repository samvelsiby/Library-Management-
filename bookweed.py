import matplotlib.pyplot as pp


def barchart(Data,c):
    
    log=[]
    xaxis=[]
    yaxis=[]
    for record in Data:
      
       xaxis.append(record[0])
    
    f=open("logfile.txt","r")
    for record in f:
        striprecord=record.strip()
        splitrecord=striprecord.split(",")
        log.append(splitrecord)    
    for record in Data:
        k=0
        for i in log:
            if record[0]==i[0] :
               k=k+1
        yaxis.append(k) 
      
    xaxis.pop(0)
    yaxis.pop(0)
    if c==1:
      pp.title("BOOK LOG DATA")
      pp.xlabel("Book ID")
      pp.ylabel("NO OF TIMES BOOK HAS BEEN TAKEN")
      pp.bar(xaxis,yaxis,color='r')
      pp.show()
    else:
     temp=[]
     j=0
     for i in yaxis:
        if i>= 1:
          temp.append(j) 
        j=j+1  
     print(temp)
    
     return temp
   





    