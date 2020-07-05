file=open('Header.txt','r')
Header=file.readlines()
for lines in Header:
    print(lines)
    print()
file.close()

file=open('Stock.txt','r')
Book=file.readlines()

list=[]
for l in Book:
    list.append(l.replace("\n"," ").split(","))

for line in Book:
    print(line)
file.close()
selectid=[]
bookname=[]
author=[]
quantity=[]
price=[]
for column in list:
    selectid.append(column[0])
    bookname.append(column[1])
    author.append(column[2])
    quantity.append(column[3])
    price.append(column[4])
file.close()

def writeStock():
    file=open('Stock.txt','w')
    for i in range(0,len(selectid),1):
        file.write(str(selectid[i]) +',' )
        file.write(''+str(bookname[i]) +',' )
        file.write(''+str(author[i]) +',' )
        file.write(''+str(quantity[i]) +',' )
        file.write(''+str(price[i]))
        file.write("\n")
    file.close()

def borrow():
    result=int(quantity[bookid-1])-1
    quantity[bookid-1]="      "+str(result)+"        "
    print("The number of remaining book is : "+str(result))


def deposit():
    result=int(quantity[bookid-1])+1
    quantity[bookid-1]="      "+str(result)+"        "
    print("The number of remaining book is : "+str(result))

def amount():
    amount=float(price[bookid-1])
    return amount


name=str(input("Enter your name: "))
collegeid=str(input("Enter your college id: "))
ans='y'
while ans=='y':
    index=0
    bookid=int(input('Enter the book id: '))
    for i in range(0,len(selectid),1):
        if(bookid==int(selectid[i])):
            index+=1
            userinput=int(input("Press 1 to borrow or 2 to deposit:"))
            if(userinput==1):
                borrow()
                pay=amount()
                print("The amount to be paid is :"+str(pay))
                writeStock()
                #success=True
            elif(userinput==2):
                deposit()
                pay=amount()
                print("The amount to be paid was :"+str(pay))
                writeStock()
                #success=True
    if(index==0):
        print('The book is not here: ')
    ans=str(input("Press y to continue or any key to exit:"))
#else:
#print('The book is not here')
