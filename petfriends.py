class Cat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info_Cat(self):
        print(f'Имя животного: {self.name},\n Возраст животного: {self.age},\n Пол животного: {self.gender}')
