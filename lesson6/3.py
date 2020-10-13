# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#     income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
#     содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
#     Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения 
#     полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
#     Проверить работу примера на реальных данных (создать экземпляры класса Position, 
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.postion = position
        self._income = income
        
        d = {
            'spec': 1000
            ,'chief_spec': 2000
        }
        
        self.bonus = d[self.postion]
    
class Position(Worker):
    def full_name(self):
        return self.name + ' ' + self.surname
    
    def get_total_income(self):
        return self._income + self.bonus

n = Position('al', 'get', 'spec', 4000)
print(n.get_total_income())
print(n.full_name())
