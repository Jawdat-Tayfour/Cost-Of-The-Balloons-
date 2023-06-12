n = int(input()) #test cases number
for i in range(n):
    price = 0 #total price
    ij= input() # seperate prices for different balloons    
    m = int(input()) #number of students
    ijlist = list(ij.split(" "))
    i = int(ijlist[0]) #seperating the prices
    j = int(ijlist[1])    
    for k in range(m):
        pp = input() # each student
        pplist = list(pp.split(" ")) # making student status a list
        if pplist[0] == '0': # calculating
            price += 0 
        elif pplist[0] == '1':
            price += i
        if pplist[1] == '0':
            price += 0 
        elif pplist[1] == '1':
            price += j
    print(price)        #printing the price
