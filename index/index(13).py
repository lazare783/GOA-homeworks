num= int(input("enter number:"))
def greet(num):
    x=0
    for i in str(num):
        x+=int(i)
    return int(num)%x 
print(greet(num))



def greet(num):
    while num%2==1:
        return num+1
    return num
    
print(greet(33))
print(greet(23))



x= int(input("enter number:"))
def greet(num):
    if num%2==0:
        num+=5
        return num%5
    else:
        num=num*3
        return num%5
           
print(greet(x))



x=input("enter your name:")
y=input('enter your surname:')
z=input("enter your age:")    
m=input("enter were are you from:")

print(f"you are {x} {y}, {z} years old and you are from {m}")



#num = 2
# print("Hello " + str(num) + " world")
# print("Hello", num, "world")
# print(f'Hello {num} world')
#ამ სამიდან საუკეთსო ხერხია მესამე რადგან პირველში უნდა ჩასვა სტრინგში მეორეში კი სიტყვების ცალცალკე ბრჭყალებში ჩასმა გიწევს.



# name = ['gurami','lazare','alexi',20, 5]
# #          0        1        2     3
# print(name[3]+name[4])


# num=[1,2,3,4,5,6,7,8,9,10]
# x=[]
# for i in num:
#     if i %2==0:
#         x.append(i)
# print(x)


#classwork(14)

def greet(L,num):
    res=[]
    for i in L:
        if i%num==0:
            res.append(i)
    return res
print(greet([1,23,165,2,3,92,10,34,911],3))

#new kwy words
# res=[3,4,5]

# # res.insert(2, 6) #chaamatebs ricxvs
# # print(res)

# res.pop(2) #amoagdebs ricxvs
# print(res)


