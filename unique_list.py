# python program for obtaining list of unique elements from list of values entered
# #dynamically from the keyyboard
def readvalues():
    lst=[]
    n= int(input("Enter how many values you want to have:"))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            name=input("Enter {} values:".format(i))
            lst.append(name)
    return lst
def unique():
    listobj=readvalues()
    if len(listobj)==0:
        print("List is empty")
    else:
        uqlist=[]
        for val in listobj:
            if val.lower() not in [x.lower() for x in uqlist]:
                uqlist.append(val)
        else:
            print("given list={}".format(listobj))
            print("Unique list Elements={}".format(uqlist))
#main program
unique()