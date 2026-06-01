class Circle:
    def __init__(self, radius):
        self._radius = 0
        self.set_radius(radius)

    def set_radius(self, new_radius):
        if Circle._is_valid_radius(new_radius):
            self._radius = new_radius
        else:
            raise ValueError('Некорректный радиус')

    @staticmethod
    def _is_valid_radius(radius):
        return isinstance(radius, (int, float)) and radius > 0


class Counter:
    total_count = 0

    def __init__(self):
        self.instance_count = 0
        __class__.total_count += 1.

    def increment(self):
        self.instance_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count

    @staticmethod
    def get_description():
        return "Это класс для подсчета."


class Brain:
    def think(self):
        return 'думает'


class Person:
    def __init__(self, name):
        self.name = name
        self.brain = Brain()

    def person_think(self):
        return f'{self.name} {self.brain.think()}'


if __name__ == '__main__':
    p = Person('dfghhg')
    print(p.person_think())
