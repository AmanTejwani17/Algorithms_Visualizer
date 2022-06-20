import time
import tkinter

from tkinter import messagebox

def Linear_search(a,drawdata,timetick,find):
    for i in range(len(a)):
        if a[i]==find:
            drawdata(a,['#90EE90' if x==i  else '#90C6EE' for x in range(len(a))])
            tkinter.messagebox.showinfo(title="Linear Search ", message="Congratulations, we have found your element at index  "+str(i+1))
            return
        else:
            drawdata(a,['white' if x==i  else '#90C6EE' for x in range(len(a))])
        time.sleep(float(timetick))


    drawdata(a,['#90C6EE'  for x in range(len(a))])

    tkinter.messagebox.showinfo(title="Linear Search", message="OOPS we are unable to found your element")

    

    
    
