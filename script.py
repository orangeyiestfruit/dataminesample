#Code works: No
import openpyxl
#Third party module. Accessible using "pip install openpyxl" under your python/Scripts file in cmd. Reads data from Excel files, a very user friendly way of gathering data - more friendly
#than I could ever write with the stupid tkinter module. TODO: Make a compatible excel file with data that it can read, and put it in machine-readable format.
data = []
stats = []
mlikes = 0
import itertools
from time import *
#TODO: 
#Make more adaptable to more input, except data that does not include all subcategories.
#Create a client and server side - the client sends data using gather function, client recieves it and appends it to 'database' file.
#Keep in mind - we need a booth with a presentation.
"""
def gather():
for y in range(0,100):
    try:
        gend = int(input("Male = 0, Female = 1\n"))
        teen = int(input("Teenager(13-19) = 1, not a teenager = 0\n"))
        snap = int(input("Snapchat = 1, no Snapchat = 0\n"))
        part = int(input("Republican = 0, Democrat/Libertarian = 1\n"))
        opin = int(input("Do you like Ford automanufacturers? Y = 1, N = 0"))
        comp = [opin,teen,gend,snap,part]
        print("Thank you for your input!")
        sleep(2);                 #just gathering manual input 
        data.append(comp)
    except:
        print("Please try again!")
        """
def excelgather():
    wb = Workbook()
    wb = wb.active
    iter = -1
    openpyxl.load_workbook("data.xlsx")
        while True:
            iter+=1
            nameA = "A"+str(iter)
            nameB = "B"+str(iter)
            nameC = "C"+str(iter)
            nameD = "D"+str(iter)
            nameE = "E"+str(iter)
            try:
                data.append([wb["preference"][nameA]])
                data.append([wb["teenager"][nameB]])
                data.append([wb["gend"][nameC]])
                data.append([wb["snapchat"][nameD]])
                data.append([wb["partisan"][nameE]])
            except:
                break   
#class functions():
        
    def strip(filename):
        f = open(filename,"r")
        data = []
        bina = f.readline()
        r = bina.split(" ")
        for rt in r:
            data.append(list(map(int, rt)))
        return data
    data = strip("paul.txt")
    #data = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]

    def subcateg(subcat,value):
        li = 0
        su = 0
        for liked in data:
            if liked[0] == 1 and liked[subcat]== value:
                li+=1
            if liked[subcat] == value:
                su+=1
        try:
            return round((li/su),4)
        except:
            print("Insufficient Data.")
    def gener(*arg):
        stats = []
        for argsd in range(1,len(arg)):
            stats.append(subcateg(1,arg[0]))
            stats.append(subcateg(2,arg[1]))
            stats.append(subcateg(3,arg[2]))
            stats.append(subcateg(4,arg[3]))
        return stats

    def gini(stat):
        r = 0
        for vals in stat:
            r+=(vals)*(vals)
        return 1-r/(len(data[0])-1)
    def iters():
        #Don't tell me to clean this up.
        als = list(itertools.product([0,1], repeat=4))  
        todo = []
        todo2 = []
        count = []
        for fun in als:
            #making als processable by gini function
            fun = ",".join(str(fun))
            fun = fun.replace(",","")
            fun = fun.replace("(","")
            fun = fun.replace(")","")
            fun = fun.replace(" ","")
            todo.append(gini(gener(int(fun[0]),int(fun[1]),int(fun[2]),int(fun[3]))))
            fuc = int(fun[0]),int(fun[1]),int(fun[2]),int(fun[3])
            todo2.append(fuc)
        r = todo.index(min(todo))
        m = todo.index(max(todo))
        return(min(todo),todo2[r],max(todo),todo2[m])
    iterlist =list(iters())
    print("Your most favourable demographic is,", iterlist[1], "with a certainty of,", iterlist[0],"that they will not like your product.")
    print("Your least favourable demograhic is,", iterlist[3], "with a certainty of,", iterlist[2],"that they will not like your product.")
