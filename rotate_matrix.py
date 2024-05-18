class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        N = len(A)

        # Transpose the matrix
        for i in range(N):
            for j in range(i, N):
                A[i][j], A[j][i] = A[j][i], A[i][j]
            # Reverse each row
        for i in range(N):
            A[i].reverse()
        return A


sol = Solution()

matrix1 = [[1, 2], [3, 4]]

print(sol.rotate(matrix1))
