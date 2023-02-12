import math
from random import randint as rand

class Linear_Regression:
    def __init__(self,x_list,y_list):
        self.x_list = x_list
        self.y_list = y_list
        self.list_len = len(x_list)
        self.m = None
        self.c = None
        pass    
    
    def most_freq(self, List): #Finds the most common pattern with a minimun freq of at least 50%
        counter = 0
        num = List[0]
         
        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency > counter):
                counter = curr_frequency
                num = i
     
        return (num,counter)


    def figure_out(self): # try to figure out m and c from the list where if more than a certain amount of times usee and most common or more than 80%/ 20% error
        x_list = self.x_list
        y_list = self.y_list
        list_len = self.list_len
        found_m = False
        possible_m = 0
        error_percent = 0.5
        error_margin = error_percent * list_len
        error_margin = int(error_margin)
        while found_m != True:
            c = []
            m = possible_m
            for i in range(len(x_list)):
                x = x_list[i]
                y = y_list[i]
                mx = x*m
                c.append(y - mx)
            
            c , count  = self.most_freq(c)

            if count >= error_margin:
                self.m = m
                self.c = c
                self.prob = count/list_len
                return (m,c,self.prob)
            c = []
            m = -m
            for i in range(len(x_list)):
                x = x_list[i]
                y = y_list[i]
                mx = x*m
                c.append(y - mx)
            
            c , count  = self.most_freq(c)

            if count >= error_margin:
                self.m = m
                self.c = c
                self.prob = count/list_len
                return (m,c,self.prob)
            
            
            else:
                possible_m += 0.0001
                possible_m = round(possible_m*10000)/10000
                pass
                
    def UserNum(self,num=1,toprint=True):
        y = (self.m * num ) + self.c
        y = math.trunc(y * 1e10)/1e10
        if toprint == True:
            print(f'The Number you entered would turn into {y} accurate upto 10dp')
        else: pass
        return y
    


if __name__ == '__main__':

    def func(x): # this is to convert our x values to y using a y = mx + c formula
        y = (-7.9 * x) + 78
        return y
    
    
    def make_x(num): #return a list of numbers num long to represent x 
        x_list = []
        for x in range(1,num):
            x_list.append(rand(1,num))
        return x_list

    def make_y(x_list): #returns a list of y numbers from the x_list
        y_list = []
        for x in x_list:
            y = func(x)
            y_list.append(y)
        return y_list


    num = 25
    x_list = make_x(num)
    y_list = make_y(x_list)
    
    LR = Linear_Regression(x_list,y_list)
    m,c,prob = LR.figure_out()
    print(f'm = {m}, c = {c}\nY = {m}X + {c} with a correlation probability of {prob}')
    while True:
        num = float(input('Enter any number'))
        LR.UserNum(num)


