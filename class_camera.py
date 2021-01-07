from main import size
from class_buttonsForBlawhi import Buttons


class Camera:
    def __init__(self, borders):
        self.dx = 0
        self.pos_over_field = 0
        self.borders = borders
        
    def apply(self, obj):
        if self.pos_over_field in range(size[0] // 2, self.borders - size[0] // 2):
            if type(obj) != Buttons:  # у кнопок по другому rect задан
                obj.rect.x += self.dx
            else:
                obj.rect.left += self.dx
    
    def update(self, target):
        if target.rect.x in range(size[0] // 2, self.borders - size[0] // 2):
            new_dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)
            if self.pos_over_field == 0:
                self.pos_over_field = self.dx - new_dx + size[0] // 2
            else:
                self.pos_over_field += self.dx - new_dx
            self.dx = new_dx
            return True  # маркер, что изменения были произведены
        self.dx = 0
        return False
        
