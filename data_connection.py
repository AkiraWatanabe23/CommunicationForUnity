'''Unityの入力によって処理を分けるテスト'''
class ProcessBase:
    '''各処理を関数毎に分ける'''
    def sum(self, num1, num2):
        '''和'''
        return num1 + num2

    def diff(self, num1, num2):
        '''差'''
        return num1 - num2

    def prod(self, num1, num2):
        '''積(product)'''
        return num1 * num2

    def quot(self, num1, num2):
        '''商(quotient)'''
        return num1 // num2

carculation = ProcessBase()
way_to_car, n1, n2 = input('計算方法、num1、num2を入力して').split()
result = 0

pass_num1 = int(n1)
pass_num2 = int(n2)

match way_to_car:
    case way_to_car if way_to_car == "s":
        result = carculation.sum(pass_num1, pass_num2)

    case way_to_car if way_to_car == "d":
        result = carculation.diff(pass_num1, pass_num2)

    case way_to_car if way_to_car == "p":
        result = carculation.prod(pass_num1, pass_num2)

    case way_to_car if way_to_car == "q":
        result = carculation.quot(pass_num1, pass_num2)

print(result)
