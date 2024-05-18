class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # Initialize variables to the first element of the array
        max_current = A[0]
        max_global = A[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(A)):
            # Update max_current to be the maximum of the current element or the current element plus max_current
            max_current = max(A[i], max_current + A[i])

            # Update max_global if max_current is greater than max_global
            if max_current > max_global:
                max_global = max_current

        return max_global


# Example usage
sol = Solution()

# Test case 1
print(sol.maxSubArray([1, 2, 3, 4, -10]))  # Output: 10

# Test case 2
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
