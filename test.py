class Ball:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    def jump(self):
        print("I jump!")

print("Please create a ball!")
size = input("What size? (big, medium, small)")
color = input("What color? (red, green, blue, etc)")
myBall = Ball(size, color)
print("Hi! I'm a", size, color, "ball!")
print("Let's jump the ball!")
myBall.jump()
