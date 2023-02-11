from LinearRegClass import Linear_Regression as LinReg

#x and y should be paired by index eg x[0] should be paired with y[0], and x[1] to y[1]
grades =   [4,4,7,4,9,9,4,1,4,3,6,9,7,7,1,4,4,3]#1 - 9 ordered
hrsstudy = [10,10,16,10,20,21,10,4,10,8,90,77,66,5,4,6,9,6]#any thing, same order as grades
    
LR = LinReg(hrsstudy,grades)
m,c,prob = LR.figure_out()
#print(f'm = {m}, c = {c}')
print(f'Equation: y = {m}x + {c} with correlation probability of {prob}')
while True:
    num = float(input('enter num of hrs studied'))
    y = LR.UserNum(num,False)
    if y >= 9: y = 9
    elif y <= 0: y = 0
    print(f'Expected grade is {y}')
    