# main.py
from direct.showbase.ShowBase import ShowBase

class BaseballGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Field
        self.field = self.loader.loadModel("models/plane.egg")
        self.field.setScale(20, 40, 1)
        self.field.setPos(0, 0, -0.5)
        self.field.setColor(0.1, 0.5, 0.1, 1)
        self.field.reparentTo(self.render)

        # Mound
        self.mound = self.loader.loadModel("models/cylinder.egg")
        self.mound.setScale(2, 2, 0.5)
        self.mound.setPos(0, 0, 0)
        self.mound.setColor(0.8, 0.5, 0.3, 1)
        self.mound.reparentTo(self.render)

        # Ball
        self.ball = self.loader.loadModel("models/sphere.egg")
        self.ball.setScale(0.3)
        self.ball.setPos(0, 0, 1)
        self.ball.setColor(1, 1, 1, 1)
        self.ball.reparentTo(self.render)

        self.accept("space", self.throw_ball)
        self.is_throwing = False

    def throw_ball(self):
        if not self.is_throwing:
            self.is_throwing = True
            self.ball.setPos(0, 0, 1)
            self.throw_speed = 0.5
            self.taskMgr.add(self.move_ball, "move_ball")

    def move_ball(self, task):
        self.ball.setY(self.ball.getY() + self.throw_speed)
        self.throw_speed += 0.1
        if self.ball.getY() > 30:
            self.taskMgr.remove("move_ball")
            self.is_throwing = False
        return task.cont

app = BaseballGame()
app.run()