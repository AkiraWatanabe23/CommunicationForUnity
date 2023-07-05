'''連立方程式を解く'''
import math

class Positions:
    '''座標の構造体'''
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

class Equation:
    '''二次方程式の各値を保存しておく'''
    def __init__(self, value_y, scalar_pow2, scalar_pow1, scalar_pow0):
        self.y = value_y
        self.a = scalar_pow2
        self.b = scalar_pow1
        self.c = scalar_pow0

    def __sub__(self, other):
        '''各値の差を求める'''
        return Equation(self.y - other.y,
                        self.a - other.a,
                        self.b - other.b,
                        self.c - other.c)

    def __mul__(self, value):
        '''式を係数倍する'''
        return Equation(self.y * value,
                        self.a * value,
                        self.b * value,
                        self.c * value)

#座標の定義
pos_a = Positions(100, 500)
pos_b = Positions(300, 200)
pos_c = Positions(600, 300)

#3つの式を立てる（ y = ax^2 + bx + c ）
formula1 = Equation(pos_a.y, pos_a.x ** 2, pos_a.x, 1)
formula2 = Equation(pos_b.y, pos_b.x ** 2, pos_b.x, 1)
formula3 = Equation(pos_c.y, pos_c.x ** 2, pos_c.x, 1)

#以下連立方程式を解く処理
subtract1 = formula1 - formula2
subtract2 = formula2 - formula3

#2値の最小公倍数を求める
lcm = math.lcm(subtract1.b, subtract2.b)
#引き算の時に全体に掛ける係数
coefficient1 = lcm / subtract1.b
coefficient2 = lcm / subtract2.b

#aについての方程式
line_a = subtract1 * coefficient1 - subtract2 * coefficient2

#各値を求める
value_a = line_a.y / line_a.a
value_b = (subtract1.y - subtract1.a * value_a) / subtract1.b
value_c = formula1.y - formula1.a * value_a - formula1.b * value_b

print(f"a = {value_a}")
print(f"b = {value_b}")
print(f"c = {value_c}")
