from main import size
from class_buttonsForBlawhi import Buttons
from class_platform import PlatformHor


class Camera:
    def __init__(self, borders):
        self.dx = 0
        self.pos_over_field = 0
        self.borders = borders

    def apply(self, obj):
        if self.pos_over_field in range(size[0] // 2 - 9, self.borders - size[0] // 2):
            if type(obj) != Buttons and type(obj) != PlatformHor:  # у кнопок по другому rect задан
                obj.rect.x += self.dx
            elif type(obj) == PlatformHor:
                obj.orig += self.dx
                obj.rect.left += self.dx
            else:
                obj.rect.left += self.dx

    def update(self, target, left):
        # возвращает маркер, что персонаж должен остаться на середине экрана
        if self.pos_over_field in range(size[0] // 2 - target.rect.w // 2,
                                        self.borders - size[0] // 2 - target.rect.w // 2):
            # блави находится посередине экрана и экран двигается
            new_dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)
            if self.pos_over_field == 0:
                self.pos_over_field = target.rect.x
            else:
                self.pos_over_field -= new_dx
            self.dx = new_dx
            return True

        elif self.pos_over_field < size[0] // 2 - target.rect.w // 2:
            # блави приближается к левой границе и экран не двигается
            new_dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)
            if self.pos_over_field < 0:
                self.pos_over_field = 0
            else:
                self.pos_over_field = target.rect.x
            self.dx = 0
            return False

        elif self.pos_over_field >= self.borders - size[0] // 2 - target.rect.w // 2:
            # блави приближается к правой границе и экран не двигается
            new_dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)
            self.pos_over_field = self.borders - size[0] // 2 - new_dx - target.rect.w // 2
            self.dx = 0
            return False
