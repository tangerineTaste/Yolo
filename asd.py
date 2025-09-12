class Person():
    def __init__(self,name,age,gender,job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
    
    def show_info(self):
        print(f"{self.name}님의 나이는 {self.age}, 성별은 {self.gender}, 직업은 {self.job}")

    def shot(self, gun):
        gun.ammo.reload()
        print(f'{self.name}이 {gun.name}을 쏘다')

class Ammo():
    def reload(self):
        print('재장전 중')

class Gun():
    def __init__(self,name):
        self.name = name
        self.ammo = Ammo()
    
    

person1 = Person('홍길동',23,'남자','도둑')
k2 = Gun('K2')
person1.show_info()
person1.shot(k2)