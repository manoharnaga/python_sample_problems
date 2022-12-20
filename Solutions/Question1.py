n = int(input("Enter the Number of Stars:"))

#   CANNOT PRINT ODD NUMBER OF STARS!!
if n%2:
    print('CANNOT PRINT ODD NUMBER OF STARS!!')
    exit()

starti=0
endi=n-1
while(starti<endi):
    for i in range(0,n):
        if(i>=starti and i<=endi):
            print("*",end='')
        else:
            print(" ",end='')
    starti+=1
    endi-=1
    if(starti<endi):
        print("")



while(starti>=0 and endi<n):
    for i in range(0,n):
        if(i>=starti and i<=endi):
            print("*",end='')
        else:
            print(" ",end='')
    print("")
    starti-=1
    endi+=1
    
    