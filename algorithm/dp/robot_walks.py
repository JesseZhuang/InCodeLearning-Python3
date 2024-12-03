"""project euler 208, hacker rank robot walks"""


# def robot_walks(k, steps, modulo):
#     # Precompute factorials modulo `modulo`
#     fact = [1] * (5 * k + 1)
#     for i in range(2, 5 * k + 1):
#         fact[i] = fact[i - 1] * i % modulo
#
#     # Function to calculate modular inverse using Fermat's little theorem
#     def mod_inverse(x, mod):
#         return pow(x, mod - 2, mod)
#
#     # Function to calculate combinations modulo `modulo`
#     def comb(n, r, mod):
#         if n < r or r < 0:
#             return 0
#         return fact[n] * mod_inverse(fact[r], mod) % mod * mod_inverse(fact[n - r], mod) % mod
#
#     # The total number of ways to choose movements
#     total_ways = 0
#     for left_turns in range(k + 1):  # Number of left turn loops
#         # There are 5*k total moves split equally among left and right turns
#         right_turns = k - left_turns
#         if right_turns < 0:
#             continue
#         # Using stars and bars to distribute turns among directions
#         ways_left = comb(5 * k, left_turns, modulo)
#         ways_right = comb(5 * k, right_turns, modulo)
#         total_ways += (ways_left * ways_right) % modulo
#         total_ways %= modulo
#
#     return total_ways
#
#
# import unittest
#
#
# class TestRobotWalks(unittest.TestCase):
#     def test_small_case(self):
#         self.assertEqual(robot_walks(1, 6, 1000000007), 2)
#
#     def test_given_case(self):
#         self.assertEqual(robot_walks(3, 6, 1000000007), 8)
#
#     def test_large_case(self):
#         self.assertEqual(robot_walks(10, 6, 1000000007), 292)
#
#     def test_edge_case_zero(self):
#         self.assertEqual(robot_walks(0, 6, 1000000007), 1)
#
#
# if __name__ == "__main__":
#     unittest.main()
#
# # Example usage
# if __name__ == "__main__":
#     k = 3
#     steps = 6
#     modulo = 1000000007
#     print(robot_walks(k, steps, modulo))

def robot_walks(k, steps, modulo):
    from functools import lru_cache

    # Total arcs are `5 * k`
    total_arcs = 5 * k

    # Define a memoized DP function
    @lru_cache(None)
    def dp(x, y, z, steps_left):
        # Base case: If no steps are left, the robot must be at origin
        if steps_left == 0:
            return 1 if (x == 0 and y == 0 and z == 0) else 0

        # Recursive case: Try clockwise and counterclockwise moves
        clockwise = dp(x + 1, y - 1, z, steps_left - 1)
        counterclockwise = dp(x - 1, y + 1, z, steps_left - 1)

        # Return the result modulo the given constraint
        return (clockwise + counterclockwise) % modulo

    # Call the DP function starting from the origin
    return dp(0, 0, 0, total_arcs)


# Example usage
if __name__ == "__main__":
    k = 3
    steps = 6
    modulo = 1000000007
    print(robot_walks(k, steps, modulo))  # Expected output: 4060
