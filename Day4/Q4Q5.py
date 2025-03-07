keys = ["Name", "Age", "Position"]
values = ["Seif", 24, "DevOps Engineer"]
dict={k:v for k,v in zip(keys, values)}
print(dict)


class Engine:
    def __init__(self,fuel_type,horsepower):
        self.fuel_type=fuel_type
        self.horsepower=horsepower

    def __str__(self):
        return f"Engine: {self.fuel_type}, {self.horsepower} HP"

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
    def __str__(self):
        return f"Car: {self.brand} {self.model}\n{self.engine}"

engine = Engine(fuel_type="petrol", horsepower=150)
car = Car(brand="BMW", model="X3", engine=engine)
print(car)
