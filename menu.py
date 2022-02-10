from tkinter import *
from database import *

Data=[]

def readdata():
    global Data
    Data=read_book()
    
def disp_book():
        
        i=0
        lstBook.delete(0,END)
        for record in Data:
            lstBook.insert(i,record[0]+"  "+record[1]+"  "+record[2]+"  "+record[3]+"  "+record[4]+"  "+record[5])
            i+=1  


def disp_book1(Data):
        print(Data)
        i=0
        lstBook.delete(0,END)
        for record in Data:
            lstBook.insert(i,record[0]+"  "+record[1]+"  "+record[2]+"  "+record[3]+"  "+record[4]+"  "+record[5])
            i+=1  

def Book_checkout():
    id=txtId.get()
    memberid=txtMemId.get()
    lstBook.delete(0,END)
    if int(memberid) >= 1000 and int(memberid) <= 9999: 
       code=bookcheckout(Data,id)
       if code==1:
           lstBook.insert(0,"Book has been succesfullt checked out")
           intologfile(id)
           changecode(Data,id,memberid)
           
       else:
           lstBook.insert(0,"Book  has been taken by another person")      
    else :
         lstBook.insert(0,"INVALID MEMBER ID")  



def Book_search():
    bookname=txtTitle.get()
    final=search_book(Data,bookname)
    disp_book1(final)
    

def Book_return():
    id=txtId1.get()
    code=bookreturn(Data,id)
    lstBook.delete(0,END)
    if code==1:
        intologfile1(Data,id)
        changecode1(Data,id)
        lstBook.insert(0,"Book has been succesfully returned")
    else:
         lstBook.insert(0,"Invalid book ID")   
def Book_weed():

    temp=[]

    temp = barchart(Data,0)
    j=0
    k=1
    lstBook.delete(0,END)
    lstBook.insert(0,"Suggested book to be weeded are:")
    for record in Data:
       for i in temp:
          if i+1==j:
             lstBook.insert(k,record[2])
             k=k+1
       j=j+1       

def Bar_graph():
    barchart(Data,1)
           
      

    

def say_bye():

    print("Bye")
    window.destroy()

    
    

#################################################
#------------------Main-------------------------#
#################################################
window=Tk()
window.title("Library Mangement")
window.geometry("1000x500")

# Create all GUI components 
btnReadBook=Button(window,text="Read Book",command=readdata)
btnDisplayBook=Button(window,text="Display Book",command=disp_book)
btnBookCheckout=Button(window,text="Book Checkout",
                    command=Book_checkout)
btnBookSearch=Button(window,text="Book Search",
                  command=Book_search)
btnBookreturn=Button(window,text="Book return",
                  command=Book_return)
btnDisplayBarGraph=Button(window,text="Display Bar Graph of Books",command=Bar_graph)
btnBookWeed=Button(window,text="Book Weed",
                    command=Book_weed)
btnBye=Button(window,text="Exit",command=say_bye)

lblTitle=Label(window,text="Title")
txtTitle=Entry(window,width=20)
lblId1=Label(window,text="Enter Book Id to Return")
txtId1=Entry(window,width=10)
lblMemId=Label(window,text="Member Id")
txtMemId=Entry(window,width=10)
lblId2=Label(window,text="Enter Book Id to Weed")
txtId2=Entry(window,width=10)
lblId=Label(window,text="Book Id")
txtId=Entry(window,width=10)
lstBook=Listbox(window)



# Define locations of the components 
btnReadBook.grid(column=0,row=0)
btnDisplayBook.grid(column=0,row=1)
lblMemId.grid(column=0,row=2)
txtMemId.grid(column=1,row=2)
lblId.grid(column=0,row=3)
txtId.grid(column=1,row=3)
lstBook.grid(column=2,row=0,rowspan=20)
btnBookCheckout.grid(column=0,row=4)
lblTitle.grid(column=0,row=5)
txtTitle.grid(column=1,row=5)
lstBook.grid(column=2,row=0,rowspan=20)
btnBookSearch.grid(column=0,row=6)
lblId1.grid(column=0,row=7)
txtId1.grid(column=1,row=7)
lstBook.grid(column=2,row=0,rowspan=20)
btnBookreturn.grid(column=0,row=8)
btnDisplayBarGraph.grid(column=0,row=9)
lblId2.grid(column=0,row=10)
txtId2.grid(column=1,row=10)
lstBook.grid(column=2,row=0,rowspan=20)
btnBookWeed.grid(column=0,row=11)



btnBye.grid(column=0,row=13)

window.mainloop()