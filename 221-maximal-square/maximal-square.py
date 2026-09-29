class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        mat1=[[0]*n for i in range(m)]
        side=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        mat1[i][j]=1
                    else:
                        mat1[i][j]=1+min(mat1[i-1][j],mat1[i][j-1],mat1[i-1][j-1])
                    side=max(side,mat1[i][j])
        return side*side                
