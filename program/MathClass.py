import operator
from functools import reduce

class Math:
    """math class"""
    def themes(self):
        requestTheme = str(input("add\nsubtruct -sub\ndivide -div\nmultiply -mult\nprobability -prob\n"))
        return requestTheme
    
    def list_of_ints(self):
        str_list_of_nums = str(input("Plese enter at least two numbers separeted throw space\n")).split(" ")
        correct_list_of_nums = []
        
        for i in str_list_of_nums:
            try:
                correct_list_of_nums.append(int(i))
            except:
                continue
        
        return correct_list_of_nums
   
    
    def chooseOperation(self, theme):
        lowerTheme = theme.lower()

        if lowerTheme in ["add"]:
            int_list = self.list_of_ints(self)
            answer = self.add(self, int_list)   
            return answer

        if lowerTheme in ["subtruct", "-sub"]:
            int_list = self.list_of_ints(self)
            answer = self.subtruct(self, int_list)    
            return answer
        
        if lowerTheme in ["divide", "-div"]:
            int_list = self.list_of_ints(self)
            answer = self.divide(self, int_list)  
            return answer
        
        if lowerTheme in ["multiply", "-mult"]:
            int_list = self.list_of_ints(self)
            answer = self.multiply(self, int_list)   
            return answer
        
        if lowerTheme in ["probability", "-prob"]:
            print("probability is chosen\n")
            return
        
        return False
    
    def add(self, number_list: list):
        sum = reduce(operator.__add__, number_list)
        return sum

    def subtruct(self, number_list: list):
        sub = reduce(operator.__sub__, number_list)
        return sub
    
    def multiply(self, number_list: list):
        multiplied = reduce(operator.__mul__, number_list)
        return multiplied
    
    def divide(self, number_list: list):
        divided = reduce(operator.__truediv__, number_list)
        return divided

    def probability(self):
        #number of probability that we want to find from all posible ways
        #number of all posible ways
        return