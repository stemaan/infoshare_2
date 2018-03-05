class Engine:
    def __init__(self, capacity, type, hp, running=False):
        self.capacity = capacity
        self.type = type
        self.hp = hp
        self.running = running

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def increase_hp(self, amount):
        self.hp += amount

    def __str__(self):
        return f'Pojemnosc {self.capacity} moc {self.hp} paliwo {self.type} dziala ? {self.running}'


class Car:
    def __init__(self, producer, model, engine=None):
        self.producer = producer
        self.model = model
        self.engine = engine

    def __str__(self):
        return f'Samochod marki {self.producer} model {self.model} silnik: {self.engine}'

    def __len__(self):
        return len(self.producer)

    def boost(self, amount):
        self.engine.increase_hp(amount)


if __name__ == '__main__':
    v8 = Engine(5.7, 'petrol', 400)
    jeep = Car('Jeep', 'Cheeroke XJ', v8)
    print(jeep)
    jeep.boost(100)
    print(jeep)