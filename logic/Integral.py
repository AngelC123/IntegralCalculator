from sympy import *

class Integral:
    def __init__(self, funcion = "", a = 0.0, b = 0.0, variable = ""):
        self.funcion = funcion
        self.a = float(a)
        self.b = float(b)
        self.variable = variable

    def integrar(self):
        if self.variable == 'x':
            try:
                x = symbols('x')
                resultado = integrate(parse_expr(self.funcion), x)
                return resultado
            except Exception as e:
                return str(e)
        if self.variable == 'y':
            try:
                y = symbols('y')
                resultado = integrate(parse_expr(self.funcion), y)
                return resultado
            except Exception as e:
                return str(e)
        if self.variable == 'θ':
            try:
                theta = symbols('θ')
                resultado = integrate(parse_expr(self.funcion), theta)
                return resultado
            except Exception as e:
                return str(e)

    def integrarDefinida(self):
        if self.variable == 'x':
            try:
                x = symbols('x')
                resultado = integrate(parse_expr(self.funcion), (x, self.a, self.b))
                return resultado
            except Exception as e:
                return str(e)
        if self.variable == 'y':
            try:
                y = symbols('y')
                resultado = integrate(parse_expr(self.funcion), (y, self.a, self.b))
                return resultado
            except Exception as e:
                return str(e)
        if self.variable == 'θ':
            try:
                theta = symbols('θ')
                resultado = integrate(parse_expr(self.funcion), (theta, self.a, self.b))
                return resultado
            except Exception as e:
                return str(e)