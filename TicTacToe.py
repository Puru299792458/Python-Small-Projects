import sys
l=[['-','-','-'],['-','-','-'],['-','-','-']]
print("Matrix")
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")
    print("\n")
user1=input("Choose your sign : ")
if(user1 =='x'):
    user2='o'
else:
    user1='o'
    user2='x'
print("------------------------Start the game-----------------------")
game=True
c=0
while game:
    c=c+1
    print(c)
    if (c==6):
        print("Match Draw")
        sys.exit()
    print("Matrix")
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            print(l[i][j],end=" ")
        print("\n")
    print("User 1")
    u1=int(input("Select a position to enter from out of 9 positions : "))
    if l[u1//3][u1%3]!='-':
        while True:
            print("Enter again as the position is already filled :")
            u1=int(input("Select a position to enter from out of 9 positions : "))
            if(l[u1//3][u1%3]=='-'):
                l[u1//3][u1%3]=user1
                break
    else:
        l[u1//3][u1%3]=user1
    if(l[0][0]==l[1][1]==l[2][2]==user1 or l[0][0]==l[1][0]==l[2][0]==user1 or l[0][0]==l[0][1]==l[0][2]==user1 or
    l[0][1]==l[1][1]==l[2][1]==user1 or l[0][2]==l[1][1]==l[2][0]==user1 or l[0][2]==l[1][2]==l[2][2]==user1 or
    l[1][0]==l[1][1]==l[1][2]==user1 or l[2][0]==l[2][1]==l[2][2]==user1):
        for i in range(0,len(l)):
            for j in range(0,len(l[i])):
                print(l[i][j],end=" ")
            print("\n")
        print("XXXXXXXXXXXXXXXXXXXXXXXX********User 1 has won********XXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys.exit()
    #if(pos==1):
    #    if
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            print(l[i][j],end=" ")
        print("\n")
    print("User 2 Turn")
    u2=int(input("Select a position to enter from out of 9 positions : "))
    if l[u2//3][u2%3]!='-':
        while True:
            print("Enter again as the position is already filled :")
            u2=int(input("Select a position to enter from out of 9 positions : "))
            if(l[u2//3][u2%3]=='-'):
                l[u2//3][u2%3]=user2
                break
    else:
        l[u2//3][u2%3]=user2
    if(l[0][0]==l[1][1]==l[2][2]==user2 or l[0][0]==l[1][0]==l[2][0]==user2 or l[0][0]==l[0][1]==l[0][2]==user2 or
    l[0][1]==l[1][1]==l[2][1]==user2 or l[0][2]==l[1][1]==l[2][0]==user2 or l[0][2]==l[1][2]==l[2][2]==user2 or
    l[1][0]==l[1][1]==l[1][2]==user2 or l[2][0]==l[2][1]==l[2][2]==user2):
        for i in range(0,len(l)):
            for j in range(0,len(l[i])):
                print(l[i][j],end=" ")
            print("\n")
        print("XXXXXXXXXXXXXXXXXXXXXXXX********User 2 has won********XXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys.exit()
