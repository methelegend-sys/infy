def checkConsecutive(mat,m,n):
  res=[]
  for i in range(m):
    for j in range(n):
      #condition for checking dialgonal elements
      if i<m-3 and j<n-3:
        count=0
        for k in range(4):
          if mat[i][j]==mat[i+k][j+k]:
            count+=1
          else:
            break
        if count==4:
          res.append(mat[i][j])
        

      #condition for checking elements to the right
      if j<n-3:
        count=0
        for k in range(4):
          if mat[i][j]==mat[i][j+k]:
            count+=1
          else:
            break
        if count==4:
          res.append(mat[i][j])
          
      #condition for checking elements vertically
      if i<m-3:
        count=0
        for k in range(4):
          if mat[i][j]==mat[i+k][j]:
            count+=1
          else:
            break
        if count==4:
          res.append(mat[i][j])
  return res

if __name__=="__main__":
    m=int(input())
    '''mat=[[0]]*m
    for i in range(m):
        arr=list(map(int,input().strip().split()))
        mat[i]=arr
    '''
    mat=[[7, 8, 9, 5, 4, 2,],
         [5, 7, 9, 4, 5, 2],
         [6, 8, 7, 9, 2, 2],
         [1, 4, 2, 7, 6, 2],
         [1, 1, 1, 1, 1, 4]]
    n=len(mat[0])
    res=checkConsecutive(mat,m,n)
    print(min(res))
