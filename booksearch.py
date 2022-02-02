
def search_book(testmarks,bookname):
    final=[]
    k=0
    i=0
    student=[]
    for student_mark in testmarks:
         if bookname  in student_mark[2]: 
           student=student_mark
           final.append(student)
           i+=1 
           k+=1
    
      
    return final
   
 



