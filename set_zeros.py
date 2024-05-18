class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A:
            return

        M = len(A)
        N = len(A[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # Check if first row has any zeros
        for j in range(N):
            if A[0][j] == 0:
                first_row_has_zero = True
                break

        # Check if first column has any zeros
        for i in range(M):
            if A[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and first column to mark zeros
        for i in range(1, M):
            for j in range(1, N):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0

        # Zero out cells based on markers in first row and column
        for i in range(1, M):
            for j in range(1, N):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(N):
                A[0][j] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(M):
                A[i][0] = 0

        return A


# Example usage
sol = Solution()

matrix1 = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]

matrix2 = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]

print(sol.setZeroes(matrix1))  # Output: [[0, 0, 0], [1, 0, 1], [1, 0, 1]]
print(sol.setZeroes(matrix2))  # Output: [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
