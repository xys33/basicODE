import unittest
from solution import odeSolver

class TestLeetSkeleton(unittest.TestCase):
    def test_solution(self):
        """
        Test example for ode_solver.py solution class method.
        Compares exact solution with solver result
        """

        #benchmark problem
        fprime = 1
        exactSol = 1
        y0 = 1
        t0 = 0  
        tf = 5
        data = []
        #solution_instance = ode_solver.Solution()
        
        # The client code picks a concrete strategy and passes it to the context.
        # The client should be aware of the differences between strategies in order
        # to make the right choice.

        data = ["a", "b", "c", "d", "e"]
        test_solver = odeSolver.ode_solver(odeSolver.ode_liniear())
        #print("Client: Strategy is set to normal sorting.")
        res_lin = test_solver.solve(data)
        #print()

        #print("Client: Strategy is set to reverse sorting.")
        test_solver.strategy = odeSolver.ode_trapezoidal()
        res_trap = test_solver.solve(data)
        
        
        self.assertEqual(','.join(res_lin),"a,b,c,d,e")
        self.assertEqual(','.join(res_trap),"e,d,c,b,a")
        

if __name__ == '__main__':
    unittest.main()