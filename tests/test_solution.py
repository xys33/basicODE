import unittest
from solution import basicODE

class TestLeetSkeleton(unittest.TestCase):
    def test_solution(self):
        """
        Test example for basicODE.py solution class method.
        Compares exact solution with solver result
        """

        #benchmark problem
        fprime = 1
        exactSol = 1
        y0 = 1
        t0 = 0
        tf = 5
        data = []
        solution_instance = basicODE.Solution()
        
        self.assertEqual(solution_instance.fake_sum(data), 6)

if __name__ == '__main__':
    unittest.main()