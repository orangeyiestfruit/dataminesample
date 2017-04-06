data = []
stats = []
mlikes = 0
import itertools
from time import *
#0 = dislike the company, 0 = not a teen, 0 = not female, 0 = no snapchat, 0 = republican


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


def strip(filename):
    f = open(filename,"r")
    data = []
    bina = f.readline()
    r = bina.split(" ")
    for rt in r:
        fd = rt.split("-")
        data.append(list(map(int, fd)))
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
def gener(one,two,thr,fou):
    stats = []
    stats.append(subcateg(1,one))
    stats.append(subcateg(2,two))
    stats.append(subcateg(3,thr))
    stats.append(subcateg(4,fou))
    return stats
stats = gener(0,1,0,1)

def gini(stat):
    r = 0
    for vals in stats:
        r+=(vals)*(vals)
    return 1-r/(len(data[0])-1)
def iters():
    #Don't tell me to clean this up.
    als = list(itertools.product([0,1], repeat=4))  
    todo = []
    for fun in als:
        #making als processable by gini function
        fun = ",".join(str(fun))
        fun = fun.replace(",","")
        fun = fun.replace("(","")
        fun = fun.replace(")","")
        fun = fun.replace(" ","")
        todo.append(gini(gener(fun[0],fun[1],fun[2],fun[3])))
    return(max(todo))
print(iters())
print(gini(gener(0,0,0,0)))

