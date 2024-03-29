# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте 
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
#     Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
#     для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 


#     реализовать абстрактные классы для основных классов проекта, 
#     проверить на практике работу декоратора @property.
      
class clothes:
    def __init__(self, closes_type, weigth):
        self.closes_type = closes_type
        self.weigth = weigth
        
    def calc(self):
        if self.closes_type == 'пальто':
            return self.weigth/6.5 + 0.5
        elif self.closes_type == 'костюм':
            return 2 * self.weigth + 0.3
        else:
            return 'не считаем'
        
    def __add__(self, other):
        return (self.weigth/6.5 + 0.5) + (2 * other.weigth + 0.3)
    
    
m = clothes('пальто', 6)
print(m.calc())

m1 = clothes('костюм', 6)
print(m1.calc())    

print(m + m1)    
