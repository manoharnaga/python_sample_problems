print("Enter any 10 words Below: ")

# USER INPUT -- 10 WORDS
input_list=[]
for i in range(0,10):
    x = input("Enter the Word_"+str(i+1)+":")
    input_list.append(x)


# SORT ACCORDING TO USER_INPUT 
choice = input("Enter ascending/descending:")
if(choice=="ascending"):
    input_list.sort()              #Ascending Order
elif(choice=="descending"):
    input_list.sort(reverse=True)  #Descending Order
else:
    print("INVALID INPUT")
    exit()


#BEFORE Appending
for i in range(0,10):
    print(input_list[i],end=' ')
print("") #new line




# APPEND A NEW ELEMENT AND PRINT THE SORTED LIST
new_element = input("Enter a New Word:")
input_list.append(new_element)


#SORT AFTER APPENDING
if(choice=="ascending"):
    input_list.sort()              #Ascending Order
elif(choice=="descending"):
    input_list.sort(reverse=True)  #Descending Order


    
#AFTER Appending
for i in range(0,11):
    print(input_list[i],end=' ')
print("") #new line

