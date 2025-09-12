class Person():
    def __init__(self,name,age,gender,job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
    
    def person_info(self):
        print(f"{self.name}님의 나이는 {self.age}, 성별은 {self.gender}, 직업은 {self.job}")

    def shot(self, gun):
        gun.ammo.reload()
        print(f'{self.name}이 {gun.name}을 쏘다')

class Ammo():
    def reload(self):
        print('재장전 중')

class Gun():
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.ammo = Ammo()
    def gun_info(self):
        return f'{self.name} 총기 번호:{self.number}'

class Riffle(Gun):
    def gun_info(self):
        return f'라이플 {self.name} 총기 번호:{self.number}'
    
    
person1 = Person('홍길동',23,'남자','도둑')
k2 = Gun('K2',2112102929)
k14 = Riffle('K14',3140732)
print(k2.gun_info())
print(k14.gun_info())
person1.person_info()
person1.shot(k2)