# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, 
# is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула 
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar 
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно 
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        if self.speed > 0:
            print('Машина едет')
        
    def stop(self):
        if self.speed == 0:
            print('Машина Стоит')
    
    def turn(self):
        print('Машина повернула')
        
    def show_speed(self):
        return self.speed
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Значение скорости превышено на {}".format(self.speed - 60))
        else:
            print(self.speed)
    
class SportCar(Car):
    def sport(self):
        print('SportCar class')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Значение скорости превышено на {}".format(self.speed - 40))
        else:
            print(self.speed)
            
class PoliceCar(Car):
    def pol(self):
        print('Police class')
        

c = Car(80, 'green', 'alfa', True)
c.speed
c.show_speed()


w = WorkCar(80, 'green', 'alfa', True)
w.speed
w.show_speed()




