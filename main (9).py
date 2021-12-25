class Field:

    def set_unit(self, y, x, unit):
        pass


class Unit:

    def __init__(self, move_type):
        self.move_type = move_type
        pass

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.move_type == 'fly':
            return self.speed * 1.2
        elif self.move_type == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')

