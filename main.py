from tkinter import ttk
import tkinter
from tkinter import *
import tkinter.scrolledtext as scrolledtext 
from tkinter import messagebox
import random
from queue import PriorityQueue
import time
from PIL import ImageTk,Image
import keyboard

#these are all the algorithm part
from bubble_sort_ import *
from selection_sort_ import *
from merge_sort_ import *
from quick_sort_ import *
from insertion_sort_ import *
from linear_search import *
from binary_search import *

root1 = Tk()

# iconphoto() method is used to set the titlebar icon ofany tkinter/toplevel window.
# But to set any image as the icon of titlebar, image should be the object of PhotoImage class.
p1 = PhotoImage(file = 'bar-chart.png')
root1.iconphoto(False, p1)


menubar = Menu(root1)
filemenu = Menu(menubar, tearoff=0)
filemenu1 = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar, tearoff=0)


def change_the_root(l):
    # root 1 is for 'Searching and Sorting algorithm' 
    # root 2 is for 'Path Finding'
    # root 3  is for 'explanation and codes'
    global root,root1,root2,root3
    if l ==1:
        root2.pack_forget()
        root3.pack_forget()
        root.pack()
        root1.config(bg="black")
    elif l==2:
        root.pack_forget()
        root3.pack_forget()
        root2.pack()
        root1.config(bg="white")
    elif l==3:
        root2.pack_forget()
        root.pack_forget()
        root3.pack()
        root1.config(bg="black")

        
#   menubar
filemenu.add_command(label="Searching and Sorting",command=lambda:change_the_root(1))
filemenu.add_command(label="Path Finding",command=lambda:change_the_root(2))
filemenu2.add_command(label="explanation and codes",command=lambda:change_the_root(3))
menubar.add_cascade(label="Visualization Types", menu=filemenu)
menubar.add_cascade(label="Explanation & Codes", menu=filemenu2)
root1.config(menu=menubar)

width=root1.winfo_screenwidth()
spacer=(" "*(int(width)//7))
root1.title(spacer+"ALGORITHM VISUALIZER")
root1.config(bg="black")

root=Frame(root1)
root.config(bg="black")
ui_frame=Frame(root,width=600,height=200,bg="grey")
ui_frame.grid(row=1,column=0,padx=10,pady=5)


natural_width=root1.winfo_screenwidth()-100
natural_height=root1.winfo_screenheight()-250

    
#   Canvas is the function of tkinter

canvas=Canvas(root,width=natural_width,height=natural_height,bg="#171717")
canvas.grid(row=0,column=0,padx=20,pady=5)


#  to draw the  graph
def drawdata(data,colorarray):
    canvas.delete("all")
    c_height=natural_height
    c_width=natural_width
    x_width=c_width/(len(data)+1)
    offset = 5
    spacing =10
    normalize=[i/max(data) for  i in data]

    for i,height  in enumerate(normalize):
        x0,y0=i*x_width+offset+spacing,c_height-height*(natural_height-65)
        x1,y1=(i+1)*x_width+offset+spacing,c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=('Helvetica','20','bold'),fill="#F46F07")
    
    root.update_idletasks()
        
data=[]
Label(ui_frame,text="Algorithm: ",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)

#  If selected algorithm is Linear search  or  Binary search
def change_the_case():
    global algo_menu,ui_frame1
    generate()
    if algo_menu.get()=="Linear search" or algo_menu.get()=="Binary search":
        ui_frame1.grid(row=0,column=4)
    else:
        ui_frame1.grid_forget()

        
algo_menu=Spinbox(ui_frame,values=('Bubble Sort','Merge Sort',"Insertion Sort","Quick sort","Selection Sort","Linear search","Binary search"),command=change_the_case,state="readonly")
algo_menu.grid(row=0,column=1,padx=5,pady=5)


#   to generate random array
def generate():
    global data
    global algo_menu

    minval=int(minv.get())
    maxval=int(maxv.get())
    size=int(sizeentry.get())

    data=[]
    for i in range(size):
        data.append(random.randrange(minval,maxval+1))

    if algo_menu.get()=="Binary search":
        data.sort()

    drawdata(data,["#90C6EE" for x in range(len(data))])

#   check type of algorithm selected 
def start_alg():
    global data
    global algo_menu
    global l2

    if algo_menu.get()=='Bubble Sort':
        bub_sort(data,drawdata,0.7)
    
    elif algo_menu.get()=='Merge Sort':
        merge_sort(data,0,len(data),drawdata,0.7)

    elif algo_menu.get()=="Insertion Sort":
        insertion_sort(data,drawdata,0.7)

    elif algo_menu.get()=="Quick sort":
        quicksort(data,0,len(data)-1,drawdata,0.7)
        drawdata(data,["#90EE90"  for x in range(len(data))])

    elif algo_menu.get()=="Selection Sort":
        sel_sort(data,drawdata,0.7)

    elif algo_menu.get()=="Linear search":
        if l2.get()=="":
            tkinter.messagebox.showinfo(title="visualizer", message="no input given")
        else:
            Linear_search(data,drawdata,0.7,int(l2.get()))
    
    elif algo_menu.get()=="Binary search":
        if l2.get()=="":
            tkinter.messagebox.showinfo(title="visualizer", message="no input given")
        else:
            binarySearch (data, 0, len(data)-1, int(l2.get()),drawdata,0.7)


def rig(e):
    generate()

def rig2(e):
    generate()

def rig3(e):
    generate()

#  To get the random array on a click ( works like refreshing your array ) and starting the algorithm
ui_frame1=Frame(ui_frame,bg="grey")
Button(ui_frame,text="Randomize",command=generate,bg="#90C6EE").grid(row=0,column=2,padx=5,pady=5,sticky=W)
Button(ui_frame,text="Start",command=start_alg,bg="#90EE90").grid(row=0,column=3,padx=5,pady=5,sticky=W)

#   Find box for Linear and Binary Search
l1=Label(ui_frame1,text="Find :",bg="grey")
l1.grid(row=0,column=4,padx=5,pady=5,sticky=W)
l2=Entry(ui_frame1)
l2.grid(row=0,column=5,padx=5,pady=5,sticky=W)

#  scale for getting size
sizeentry=Scale(ui_frame,label="SIZE",from_=3,to=20,length=300, orient = HORIZONTAL,command=rig)
sizeentry.grid(row=1,column=0,padx=5,pady=5,sticky=W,columnspan=4)

#  scale for speed
speedscale=Scale(ui_frame,label="SPEED SCALE (SEC)",from_=0.01,to=1,length=200,resolution=0.01, orient = HORIZONTAL)
speedscale.grid(row=1,column=4,padx=5,pady=5,sticky=W)

#  scale for min value
minv=Scale(ui_frame,label="MIN VALUE",from_=1,to=10, orient = HORIZONTAL,command=rig2)
minv.grid(row=1,column=5,padx=5,pady=5,sticky=W)

#  scale for max value
maxv=Scale(ui_frame,label="MAX VALUE",from_=15,to=99, orient = HORIZONTAL,command=rig3)
maxv.grid(row=1,column=6,padx=5,pady=5,sticky=W)

get_frame=Frame(root,bg="grey")
get_frame.grid(row=0,column=3,padx=2,pady=5,columnspan=2,rowspan=2)
generate()

#pathfinding part

#  dimensions for grid
global_row=25
global_column=40

# configuring grid 
if root1.winfo_screenwidth()<1366 or root.winfo_screenheight()<768:
    global_row-=3
    global_column-=3

root2=Frame(root1)
border_=Frame(root2,bg="black")
box=Frame(border_)
start=False
des=False
vari,varj=0,0
img1=ImageTk.PhotoImage(Image.open("images/ma.png").resize((20,20),Image.ANTIALIAS))
img2=ImageTk.PhotoImage(Image.open("images/home.png").resize((20,20),Image.ANTIALIAS))

start__=False
destination=False
place_wall=False

speed__=0.01
grid=[]
grid1=[]

def fs(x1,y1,start_x1,start_y1,destination_x2,destination_y2):
    return abs(x1-start_x1)+abs(y1-start_y1)+abs(x1-destination_x2)+abs(y1-destination_y2)

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

for i in range(global_row):
    f=[]
    for j in range(global_column):
        f.append(0)
    grid.append(f)
    
def color_adi(i,j,grid1):
    global start__,destination,place_wall,start,des,grid,img1,img2,b1,b2
    global visited
    if start__:
        grid1[i][j].config(bg="lightblue",image=img1,width=23,height=20)
        b1.config(bg="lightblue")
        if start!=False:
            visited=[]
            grid1[start[0]][start[1]].config(bg="white",text=" ",width=3,height=1,image="")
               
        start=(i,j)
        start__=False
    elif destination:
        b2.config(bg="#e47ae6")
        grid1[i][j].config(bg="#e47ae6",image=img2,width=23,height=20)
        if des!=False:
            grid1[des[0]][des[1]].config(bg="white",text=" ",width=3,height=1,image="")
        des=(i,j)
        destination=False
    elif place_wall:
        try:
            grid1[i][j].config(bg="black")
            grid[i][j]=1
        except:
            pass

#   A star algorithm 

def a_star(grid):
    found=0
    global start,des,speed__
    openlist=[]
    closedlist=[]
    came_from = {}
    openlist.append(start)

    while len(openlist)!=0 and found!=1:
        fscores_in_open_lsit=[]
        for i in openlist:
            fscores_in_open_lsit.append(fs(i[0],i[1],start[0],start[1],des[0],des[1]))
        q=openlist[fscores_in_open_lsit.index(min(fscores_in_open_lsit))]
        closedlist.append(q)
        openlist.pop(fscores_in_open_lsit.index(min(fscores_in_open_lsit)))
        successor=[]
        successors_f_cost=[]
        
        for i in range(q[0]-1,q[0]+2,1):
            for j in range(q[1]-1,q[1]+2,1):
                if i>=0 and j>=0 and i<len(grid) and j<len(grid) and ((i,j) not in closedlist) and grid[i][j]!=2:
                    successor.append((i,j))
                    openlist.append((i,j))
                    successors_f_cost.append(fs(i,j,start[0],start[1],des[0],des[1]))
        for i in successor:
            if i[0]==des[0] and i[1]==des[1]:
                print("found",i[0],i[1])
                found=1
                break
            else:
                q=successor[successors_f_cost.index(min(successors_f_cost))]
                if q not in closedlist:
                    closedlist.append(q)

        draw(openlist,closedlist,grid1)
        time.sleep(speed__)


def draw_path(path):
    global start,des,img3
    for x in path:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j:
                    if(x[0]==des[0] and x[1]==des[1]) or (x[0]==start[0] and x[1]==start[1]):
                        grid1[i][j].config(bg="#90C6EE")
                    else:
                        grid1[i][j].config(bg="#90C6EE")

                
                    
visited=[]    
def draw(openlist,grid):
    global visited

    path=[]
    for x in openlist:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j and grid[i][j]["bg"]!="#468ec2" and (i,j) not in path:
                    path.append((i,j))
                    visited.append((i,j))

    for x in path:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j :
                    grid[i][j].config(bg="#468ec2")

    root1.update_idletasks()

def algorithm( grid, start, end,came_from):
    count = 0
    global grid1
    global speed__
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    g_score = {(i,j): float("inf") for i in range(len(grid)) for j in range(len(grid[0]))}
    g_score[start] = 0
    f_score = {(i,j): float("inf") for i in range(len(grid)) for j in range(len(grid[0]))}
    f_score[start] = h(start, end)
    open_set_hash = {start}
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            return True

        neighbors=[]
        for i in range(current[0]-1,current[0]+2,1):
            for j in range(current[1]-1,current[1]+2,1):
                if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j]!=1:
                    if (i,j)!=start:
                        neighbors.append((i,j))
                            
        for n in neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = temp_g_score
                f_score[n] = temp_g_score + h(n, end)
                if n not in open_set_hash:
                    count += 1
                    open_set.put((f_score[n], count, n))
                    open_set_hash.add(n)
        
        draw(open_set_hash,grid1)
        time.sleep(speed__)
                    
    return False


def reconstruct_path(came_from, current,path):
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.append(des)

def run_algo():
    global grid,start,des
    came_from={}
    path=[]
    if algorithm(grid, start, des,came_from):
        reconstruct_path(came_from, des,path)
        draw_path(path)
    else:
        tkinter.messagebox.showinfo(title="Pathfinding visualizer", message="path not found ")
        


def walls(i,j,grid1):
    global grid
    global start__,destination,place_wall,start,des,grid,des,start,vari,varj
    
    if place_wall:

        if keyboard.is_pressed("w"):
            if start!=False and des!=False:
                if grid1[i][j]["bg"]=="white":
                    grid1[i][j].config(bg="black")
                    grid[i][j]=1
            else:
                place_wall=False

        if keyboard.is_pressed("c"):
            if start!=False and des!=False:
                if grid1[i][j]["bg"]=="black":
                    grid1[i][j].config(bg="white")
                    grid[i][j]=0
            else:
                place_wall=False
        
       
def create_butt(i,j):
    global grid1
    jb=Button(box,text=" ",width=3,height=1,command=lambda:color_adi(i,j,grid1),bg="white")
    jb.bind("<Enter>",func=lambda event:walls(i,j,grid1))
    return jb
    
#   function for creating the grid
def create_grid():
    global grid1,global_row,global_column
   
    for i in range(global_row):
        f=[]
        for j in range(global_column):
            f.append(create_butt(i,j))
            f[-1].grid(row=i,column=j)

        grid1.append(f)
        
        
create_grid()

box.grid(row=0,column=0,padx=10,pady=10)

box1_create=Frame(root2,bg="grey")
box1=Frame(box1_create,bg="grey")

#  Function to clear the path visualization
def clear():

    global grid,grid1,start__,place_wall,destinationm,start,des,b1,b2

    b1.config(bg="lightblue")
    b2.config(bg="#e47ae6")

    start__,place_wall,destination=False,False,False
    start,des=False,False
    global img1,img2
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]=0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
  
            grid1[i][j].config(bg="white",text=" ",image="",width=3,height=1)
            grid1[i][j].image = ""
    
    
def assignstart():
    global start__,b1
    b1.config(bg="#276ea1")
    b2.config(bg="#e47ae6")
    start__=True

def assigndes():
    global destination,b2
    b1.config(bg="lightblue")
    b2.config(bg="#c865c9")
    destination=True

def assignwall():
    global place_wall
    place_wall=True

def start_alg():
    global grid,start__,place_wall,destination,des,start,algo_menu1,route,route_found,visited
    global visited1,visited2,visited_pos_f ,visited_pos_r ,visited_node_f ,visited_node_r ,route_f ,route_r ,parents
    
    if algo_menu1.get()=="A star algorithm":
        run_algo()
        start__,place_wall,destination=False,False,False
        start,des=False,False
        visited=[]
        route = None
        route_found = False
    elif algo_menu1.get()=="Dijkstras algorithm":
        run_algo2()
        start__,place_wall,destination=False,False,False
        start,des=False,False
        visited=[]
        route = None
        route_found = False
     
visited = []
route = None
route_found = False


def run_algo2():
    global grid,start__,place_wall,destination,des,start,alg_menu1,start,des,visited
    global route,route_found

    visited.append(start)
    dist={}
    came_from={}
    path=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j)==start:
                dist[(i,j)]=0
                came_from[(i,j)]=(i,j)
            else:
                dist[(i,j)]=float("inf")
                came_from[(i,j)]=None

    dijkstras(grid,start,start,des,dist,came_from)
    dijkstras_execute()

    visited=[]

    route = None
    route_found = False
    try:
        came_froms(start,des,came_from,path)
        draw_path(path)
    except:
        tkinter.messagebox.showinfo(title="visualizer", message="path not found ")


def print_grid(grid,grid1):
    global start
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                if grid1[i][j]["bg"]!="yellow" and (i,j)!=start:
                    grid1[i][j].config(bg="yellow")
    root1.update_idletasks()
                    
def checkValid(move):
    global grid
    if move[0]>=0 and move[0]<len(grid) and move[1]>=0 and move[1]<len(grid[0]):
        if grid[move[0]][move[1]]!=1 and move not in visited:
            visited.append(move)
            return True
    return False

def findEnd(first_out,des):
    if first_out == des:
        return True
    return False

def print_grid1(visited):
    global start
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in visited and grid1[i][j]["bg"]!="#468ec2" and (i,j)!=start:
                grid1[i][j].config(bg="#468ec2")

    root1.update_idletasks()
                
def dijkstras_execute():

    global route_found,start,des,grid,route,visited
    queue = [start]
    moves_queue = ['']
    first_out = ''
    first_moves = ''
    path=[]
    global speed__

    while len(queue) > 0:
        first_out = queue.pop(0)
        first_moves = moves_queue.pop(0)
        for m in ['L', 'R', 'U', 'D','UR','UL','DL','DR']:
            i, j = first_out
            if m == 'L':
                i -= 1
            elif m == 'R':
                i += 1
            elif m == 'U':
                j -= 1
            elif m == 'D':
                j += 1
            elif m == 'UR':
                i += 1
                j-=1
            elif m == 'UL':
                i-= 1
                j-=1
            elif m == 'DL':
                j += 1
                i-=1
            elif m == 'DR':
                j += 1
                i+=1

# Make new variable "latest_moves" for adding onto the queue again, because you don't want the 'parent' variable to change
            latest_moves = first_moves + str((i,j))+" . "
            if checkValid((i, j)):
                print_grid1(visited)
                time.sleep(speed__)
                queue.append((i, j))
                moves_queue.append(latest_moves)

            if findEnd((i, j),des):
                route = latest_moves
                route_found = True
                break
        
        if route_found:
            break


def dijkstras(grid,src,start,des,dist,came_from):
    for i in range(start[0]-1,start[0]+2,1):
        for j in range(start[1]-1,start[1]+2,1):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and (i,j)!=src and (i,j)!=start and grid[i][j]==0:
                if dist[(i,j)]>1+dist[start]:
                    came_from[(i,j)]=start
                    dist[(i,j)]=1+dist[start]
                    dijkstras(grid,src,(i,j),des,dist,came_from)
                        
                    
def came_froms(src,des,came_from,path):
    if came_from[des]==src:
        path.append(des)
        path.append(src)
        return True
    else:
        path.append(des)
        came_froms(src,came_from[des],came_from,path)

def speed_change():
    global speed__,algo_menu2

    if algo_menu2.get()=="Noraml":
        speed__=0.01
    elif algo_menu2.get()=="Fast":
        speed__=0.005
    elif algo_menu2.get()=="Super Fast":
        speed__=0.001
    else:
        speed__=0.1

#codes and explanation
root3=Frame(root1)
root3.config(bg="white")
imag1=["explanations/1-Title.jpg", "explanations/2-Welcome.jpg", "explanations/3-Welcome-copy-2.jpg", "explanations/4-Welcome-copy-3.jpg", "explanations/5-Welcome-copy-1.jpg", "explanations/6-Welcome-copy-4.jpg", "explanations/7-Welcome-copy-5.jpg", "explanations/8-Welcome-copy-6.jpg", "explanations/9-Welcome-copy-7.jpg", "explanations/10-Welcome-copy-8.jpg", ]

docimg1=[ImageTk.PhotoImage(Image.open(i).resize((root3.winfo_screenwidth()-200,root3.winfo_screenheight()-200),Image.ANTIALIAS)) for i in imag1]
doc_count=0
docimages1=Label(root3,image=docimg1[0])
docimages1.grid(row=0,column=0,padx=40,pady=20)


explanation_=Frame(root3)
def gor1(a):
    global doc_count,imag1,docimg1
    if a==1:
        doc_count-=1
    else:
        doc_count+=1

    if doc_count<0:
        doc_count=len(imag1)-1
    if doc_count>=len(imag1):
        doc_count=0
    docimages1.config(image=docimg1[doc_count])
    
forward1=Button(explanation_,text="<< Backward",command=lambda:gor1(1))
forward1.grid(row=0,column=0,padx=10,pady=10)

backward1=Button(explanation_,text="Forward >>",command=lambda:gor1(0))
backward1.grid(row=0,column=1,padx=10,pady=10)

explanation_.grid(row=1,column=0)

    
which=Label(box1,text="Algorithm :",bg="grey")
which.grid(row=0,column=0,padx=3)
algo_menu1=Spinbox(box1,values=("Dijkstras algorithm","A star algorithm"),state="readonly")
algo_menu1.grid(row=0,column=1,padx=3,pady=5)
# wht2=Label(box1,text="Speed :",bg="grey")
# wht2.grid(row=0,column=2,padx=3)
algo_menu2=Spinbox(box1,values=("Normal","Fast","Super Fast","Slow"),command=speed_change,state= "readonly")
algo_menu2.grid(row=0,column=3,padx=3,pady=5)
b1=Button(box1,text="Source Node",command=assignstart,bg="lightblue")
b1.grid(row=0,column=4,padx=3,pady=5)
b2=Button(box1,text="Destination Node",command=assigndes,bg="#e47ae6")
b2.grid(row=0,column=5,padx=3,pady=5)
b3=Button(box1,text="Walls",command=assignwall,bg="black",fg="white").grid(row=0,column=6,padx=3,pady=5)

b4=Button(box1,text="Visualize",command=start_alg,bg="#90EE90").grid(row=0,column=7,padx=3,pady=5)
Button(box1,text="Clear Board",command=clear).grid(row=0,column=8,padx=3,pady=5)

box1.grid(row=0,column=0,padx=20,pady=5)
box1_create.grid(row=1,column=0)
border_.grid(row=0,column=0,padx=50,pady=5)
root.pack()
root1.mainloop()
