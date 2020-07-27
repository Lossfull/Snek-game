import pygame

class Snake:
    def __init__(self, length, speed, square_size,):
        self.length = length
        self.speed = speed
        self.square_size = square_size
        self.x = []
        self.y = []
        for i in range(length):
            self.x.append(0)
            self.y.append(0)

    def set_window_width_height(self, width, height):
        self.width = width
        self.height = height

    def draw_snake(self, surface):
        for j in range(self.length):
            pygame.draw.rect(surface, (255, 255, 255), (self.x[j], self.y[j], self.square_size, self.square_size))

    def move_in_direction(self, rotation_flag):
        if rotation_flag == 'right':
            for i in range(self.length - 1):
                self.x[i] = self.x[i + 1]
                self.y[i] = self.y[i + 1]
            self.x[self.length - 1] += self.square_size + 1
            # x += 15
            if self.x[self.length - 1] >= self.width:
                self.x[self.length - 1] -= self.width
        elif rotation_flag == 'left':
            for i in range(self.length - 1):
                self.x[i] = self.x[i + 1]
                self.y[i] = self.y[i + 1]
            self.x[self.length - 1] -= self.square_size + 1
            # x -= 15
            if self.x[self.length - 1] <= -(self.square_size + 1):
                self.x[self.length - 1] += self.width
        elif rotation_flag == 'up':
            for i in range(self.length - 1):
                self.x[i] = self.x[i + 1]
                self.y[i] = self.y[i + 1]
            self.y[self.length - 1] -= self.square_size + 1
            # y -= 15
            if self.y[self.length - 1] <= -(self.square_size + 1):
                self.y[self.length - 1] += self.height
        elif rotation_flag == 'down':
            for i in range(self.length - 1):
                self.x[i] = self.x[i + 1]
                self.y[i] = self.y[i + 1]
            self.y[self.length - 1] += self.square_size + 1
            if self.y[self.length - 1] >= self.height:
                self.y[self.length - 1] -= self.height


if __name__ == '__main__':
    pygame.init()
    sc = pygame.display.set_mode((600, 400))
    snake = Snake(10, 10, 15)
    snake.set_window_width_height(600, 400)
    rotation_flag = 'right'
    clock = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rotation_flag = 'right'
                elif event.key == pygame.K_LEFT:
                    rotation_flag = 'left'
                elif event.key == pygame.K_UP:
                    rotation_flag = 'up'
                elif event.key == pygame.K_DOWN:
                    rotation_flag = 'down'

        snake.move_in_direction(rotation_flag)
        sc.fill((0, 0, 0))
        snake.draw_snake(sc)
        pygame.display.update()
        clock.tick(snake.speed)