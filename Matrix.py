# Create a Matrix
'''
c=int(input("Enter columns:"))
r=int(input("Enter rows:"))
def createMatrix(r,c):    
    l=[]
    for m in range(r):
        x=[]
        for n in range(c):
            x.append(input())
        l.append(x)
    return l
l=createMatrix(r,c)
'''



# Read a Matrix
'''
def readMatrix():    
    print("Matrix is :-\n")
    for i in l:
        for j in i:
            print("\t",j,end=" ")
        print()
    print()
readMatrix()
'''


# Read Matrix in Snake Pattern
'''
def readBySnakePattern(arr):
    for i in range(len(arr)):
        # Read Left to Right
        if i%2==0:
            for j in range(len(arr[i])):
                print(arr[i][j],end="  "*2)
            print()

        # Read Right to Left
        else:
            for j in range(len(arr[i])-1,-1,-1):
                print(arr[i][j],end="  "*2)
            print()
readBySnakePattern(l)
'''



# Read Matrix by Boundry Traversal
'''
def readByBoundryTraversal(arr):
    print()
    for i in range(len(arr)):
        # First Row From Left to Right
        if i==0:    
            for j in range(len(arr[i])):
                print(arr[i][j],end=" ")
            print()
        else:    
            # Read from top to bottom
            if i<len(arr)-1:
                print(arr[i][len(arr)-1],end=" ")

            # Read from bottom right to left
            else:    
                if i==len(arr)-1:
                    print()
                    for j in range(len(arr[i])-1,-1,-1):
                        print(arr[i][j] ,end=" ")
                    print()
        
    # Read from bottom to top
    for i in range(len(arr)-2,0,-1):
        print(arr[i][0])

readByBoundryTraversal(l)

'''



# Transpose of Matrix
'''
def transposeOfMatrix(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr[i])):
            temp=arr[i][j]
            arr[i][j]=arr[j][i]
            arr[j][i]=temp

transposeOfMatrix(l)
'''

# Rotate Matrix Anticlockwise 90 deg
'''
def rotate(arr):    
    if(len(arr)%2==0):    
        x=len(arr)-1
        for i in range(0,len(arr)//2):
            t=arr[i]
            arr[i]=arr[i+x]
            arr[i+x]=t

            x=x-1
    else:
        x=len(arr)-1
        for i in range(0,(len(arr)//2 )-1):
            t=arr[i]
            arr[i]=arr[i+x]
            arr[i+x]=t

            x=x-1


rotate(l)
   ''' 

# Spiral Traversal of Matrix
'''
def spiralTraversal(arr):    
    top=0 #Row
    bottom=len(arr)-1 #Row-reverse

    left=0  #Col
    right=len(arr)-1 #Col-reverse


    while(top<=bottom and left<=right):
        # Read Top Row
        for i in range(left,right+1):
            print(arr[top][i],end=" ")
        top+=1
        print()

        # Read Right Col
        for i in range(top,bottom+1):
            print(arr[i][right],end=" ")
        right-=1
        print()


        if(top<=bottom):
            for i in range(right,left-1,-1):
                print(arr[bottom][i],end=" ")
            bottom-=1

        if(left<=right):
            for i in range(bottom,top-1,-1):
                print(arr[i][left],end=" ")
            left+=1

spiralTraversal(l)
'''




# Search in Row-wise and Col-wise Sorted Matrix
'''
def searchInMatrix(arr,target):
    i=0
    j=0
    startSearching=True
    targetElm=target
    while(startSearching):
        if i<len(arr) and j<len(arr):    
            if targetElm!=arr[i][j]:
                if targetElm<arr[i][j+1]:
                    i+=1
                else:
                    j+=1
            else:
                print("Founded at index (",i,",",j,")")
                startSearching=False
        else:
            print("Not Founded")
            startSearching=False
arr=[

        [10,20,30,40],
        [15,25,35,45],
        [27,29,37,48],
        [32,33,39,50]
    ]
searchInMatrix(arr,29)
'''


# Median of Row Wise Sorted Matrix
matrix=[
    [1,3,5],
    [2,6,9],
    [3,6,9]
]

# Calculate Min Element
min=matrix[0][0]
for i in range(len(matrix)):
    if matrix[i][0]<min:
        min=matrix[i][0]
# Calculate Max Element
max=matrix[len(matrix)-1][0]
for i in range(len(matrix)):
    if matrix[i][len(matrix)-1]>max:
        max=matrix[i][len(matrix)-1]


# Binary Search For Counting Less Elements
def func(arr,val):
    low=0
    high=len(arr)-1
    count=0
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<val:
            low=mid+1
            count+=1
        else:
            high=mid-1
    return count





# Apply Binary Search

n=len(matrix)
m=n
low=min
high=max
while(low<=high):
    count=0
    mid=(low+high)//2

    for i in range(len(matrix)):
        count=count+func(matrix[i],mid)

    if count==(n*m)//2:
        print(low)
        break
    if count<(n*m)//2:
        low=mid+1
    else:
        high=mid-1

    








