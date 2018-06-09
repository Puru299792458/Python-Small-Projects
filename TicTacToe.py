import sys
l=[['-','-','-'],['-','-','-'],['-','-','-']]
user1=input("Choose your sign : ")
if(user1 =='x'):
    user2='o'
else:
    user2='x'
print("Matrix")
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")
    print("\n")
print("------------------------Start the game-----------------------")
game=True
while game:
    print("User 1")
    u1=int(input("Select a position to enter from out of 9 positions : "))
    if l[u1//3][u1%3]!='-':
        while True:
            print("Enter again as the position is already filled :")
            u1=int(input("Select a position to enter from out of 9 positions : "))
            if(l[u1//3][u1%3]=='-'):
                l[u1//3][u1%3]='x'
                break
    else:
        l[u1//3][u1%3]='x'
    print("Matrix")
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            print(l[i][j],end=" ")
        print("\n")
    if(l[0][0]==l[1][1]==l[2][2]==user1 or l[0][0]==l[1][0]==l[2][0]==user1 or l[0][0]==l[0][1]==l[0][2]==user1 or
    l[0][1]==l[1][1]==l[2][1]==user1 or l[0][2]==l[1][1]==l[2][0]==user1 or l[0][2]==l[1][2]==l[2][2]==user1 or
    l[1][0]==l[1][1]==l[1][2]==user1 or l[2][0]==l[2][1]==l[2][2]==user1):
        print("XXXXXXXXXXXXXXXXXXXXXXXX********User 1 has won********XXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys.exit()
    #if(pos==1):
    #    if
    print("User 2 Turn")
    u2=int(input("Select a position to enter from out of 9 positions : "))
    if l[u2//3][u2%3]!='-':
        while True:
            print("Enter again as the position is already filled :")
            u2=int(input("Select a position to enter from out of 9 positions : "))
            if(l[u2//3][u2%3]=='-'):
                l[u2//3][u2%3]='o'
                break
    else:
        l[u2//3][u2%3]='o'
    if(l[0][0]==l[1][1]==l[2][2]==user2 or l[0][0]==l[1][0]==l[2][0]==user2 or l[0][0]==l[0][1]==l[0][2]==user2 or
    l[0][1]==l[1][1]==l[2][1]==user2 or l[0][2]==l[1][1]==l[2][0]==user2 or l[0][2]==l[1][2]==l[2][2]==user2 or
    l[1][0]==l[1][1]==l[1][2]==user2 or l[2][0]==l[2][1]==l[2][2]==user2):
        print("XXXXXXXXXXXXXXXXXXXXXXXX********User 2 has won********XXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys.exit()
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            print(l[i][j],end=" ")
        print("\n")
