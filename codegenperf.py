import sympy
from sympy import Matrix, symbols

def _make_expr_01():
    
    C = Matrix(3, 3, symbols('C00, C01, C02, C10, C11, C12, C20, C21, C22'))

    F = Matrix(3, 3, symbols('F00, F01, F02, F10, F11, F12, F20, F21, F22'))

    Fg = Matrix(3, 3, symbols('Fg11, Fg12, Fg13, Fg21, Fg22, Fg23, Fg31, Fg32, Fg33'))

    Fg_inv=Fg.inv()

    Ce=Fg_inv.T*C*Fg_inv

    Cedet=Ce.berkowitz_det()

    return Cedet

class TimeFCodegen01:

    def setup(self):
        self.expr = _make_expr_01()

    def time_fcodegen(self):
        result=codegen(['Test', self.expr], 'F95')
