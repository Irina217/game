import arcade

# размер экрана и название
width = 800
height = 800
title = "test"

movespeed = 450


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width, height, title)

        # background
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # stats hero
        self.moveX = 0
        self.moveY = 0
        self.xhero = 50
        self.yhero = 100

    def on_draw(self):  # функция для рисование персонажа
        arcade.start_render()
        arcade.draw_circle_filled(self.xhero, self.yhero, 25, arcade.color.RED)

    def on_key_press(self, key, modifiers):  # обработка нажатия клавиш
        if key == arcade.key.LEFT:
            self.moveX = -movespeed
        elif key == arcade.key.RIGHT:
            self.moveX = movespeed
        elif key == arcade.key.UP:
            self.moveY = movespeed
        elif key == arcade.key.DOWN:
            self.moveY = -movespeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.moveX = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.moveY = 0

    def update(self, delta_time):  # обновление координат и грань экрана
        upX = self.xhero + self.moveX * delta_time
        upY = self.yhero + self.moveY * delta_time
        if upX > 800 or upX < 0:
            self.xhero = width // 2
            self.yhero = height // 2
        if upY > 800 or upY < 0:
            self.xhero = width // 2
            self.yhero = height // 2
        self.xhero += self.moveX * delta_time
        self.yhero += self.moveY * delta_time


# основа для запуска
def main():
    window = MyGame()
    arcade.run()


main()