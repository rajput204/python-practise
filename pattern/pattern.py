#simple patter
for i in range(1,int(input("enter the number"))):
    for j in range(1,i):
        print("*",end=" ")
    print( )
print( )

#output:-
# * 
# * * 
# * * * 

#2nd pattern
for i in range(1,5):
        for j in range(1,5):
            print("*",end=" ")
        print( )
print( )
#output:-
# * * * * 
# * * * * 
# * * * * 
# * * * * 
        
#3rd 
for i in range(1,5):
    for j in range(i):
         print("*",end=" ")
    print( )
print( )
    
#output
# * 
# * * 
# * * * 
# * * * * 

#4th star
for i in range(1,5):
        for j in range(5-i):
               print("*",end=" ")
        print(" ")
print( )
        
#output
# * * * *  
# * * *  
# * *  
# *       

 

#5th
for i in range(1,5):
        for j in range(1,i):
            print(j,end=" ")
        print( )
#output:-
# 1 
# 1 2 
# 1 2 3 
        
#6th
for i in range(1,6):
        k=6-i
        for j in range(1,5):
            if j<=6-i:
                  print(j,end=" ")
        print( )
        
print( )

#output
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

#7th
for i in range(1,5):
    k=6-i
    for j in range(1,5):
            if j<= 6-i:
                print(k,end=" ")
                k-=1
    print( )
        
print( )

#output:-
# 5 4 3 2 
# 4 3 2 1 
# 3 2 1 
# 2 1 

#8th
for i in range(1,5):
        for j in range(1,8):
            if j<=5-i or j>=3+i:
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
        print( )
#output:-
# * * * * * * * 
# * * *   * * * 
# * *       * * 
# *           * 

for i in range(1,4):
    for j in range(1,2*i):
        print( "*",end=" ")
    else:
        print( )
print( )



for i in range(1,6):
    for j in range(1,5):
        if  (i==1 or j==4) or (i==5 or j==4)  or (i==3 or j==4) :
          print("*",end=" ")
    else:
        print( )
print( )

#output:-
# * * * *
# *
# * * * *
# *
# * * * *


for i in range(1,8):
    for j in range(1,5):
        if (i==1 or j==4) or(i==4 or j==4):
            print("*",end=" ")
    else:
        print( )
print ( )

#output:-
# * * * *
# *
# *
# * * * *
# *
# *
# *

for i in range(1,7):
    for j in range(1,6):
        if (i==6 or j==5):
            print("*",end=" ")
    else:
        print( )
print( )

#output:-
# *
# *
# *
# *
# *
# * * * * *

for i in range(1,6):
    for j in range(1,5):
        if (j==1 or j==4  or i==3)  :
            print("*",end=" ")
        else:
          print(" " ,end=" ")
    print( )

#output:-
# *     *
# *     *
# * * * *
# *     *
# *     *
    

for i in range(1,6):
    for j in range(i+1):
        if j==i or i==1 or i==2 or i==3 or j==2:
            print("*",end=' ')
    else:
        print(" ",end=' ')
    print( )
#output:-
# *     
# * *
# * * *
# * * * *
# * *
# * *
count=0   
for i in range(1,5):
    for j in range(1,5):
        print( chr(65+count),end=" ")
        count+=1
    print( )
#output:-
# A B C D
# E F G H
# I J K L
# M N O P

for i in range(0,6):
    for j in range(0,5):
        print(chr(65+i),end=" ")
    print( )
print( )
#output:-
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E
# F F F F F
for i in range(0,5):
    for j in range(0,5):
        print(chr(65+j),end=" ")
    print( )
#output:-
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print( )
print( )
#output:-
# A
# A B
# A B C
# A B C D
# A B C D E
