# class vehicle():
#     def __init__(self,name,max_speed,mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_cap(self,capacity):
#         print('Vehicle Name :'+self.name+'    Seating capacity :'+capacity )

# class bus(vehicle):
#     def seating_cap(self, capacity='50'):
#         return super().seating_cap(capacity)

# #car = vehicle(250,300)
# bus = bus('volvo',300,400)
# print(bus.name,bus.max_speed,bus.mileage)
# bus.seating_cap()


###Static & static Method###
class student:
    name='class variable'
    def __init__(self,a,b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls):
        print("This is class Method &"+cls.name)

print(student.info())
print('Testing git command')


    

