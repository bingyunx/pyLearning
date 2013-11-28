import kivy
#import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

from kivy.vector import Vector
from kivy.clock import Clock

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            vx,vy = ball.vel_x,ball.vel_y
            offset_y = (ball.center_y - self.center_y)/(self.height/2)
            bounce = Vector(-1*vx,vy)*1.05
            ball.velocity = bounce.x,bounce.y+offset_y 

class PongBall(Widget):

    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    velocity = ReferenceListProperty(vel_x, vel_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos 

class PongGame(Widget):

    def on_touch_down(self, touch):
        print "(%d,%d)" % (touch.x, touch.y)

    def on_touch_move(self, touch):
        if touch.x < self.width/4:
            self.player1.center_y = touch.y
        elif touch.x > self.width * 3 / 4:
            self.player2.center_y = touch.y

    def reset(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        self.player1.center_y = self.center_y
        self.player2.center_y = self.center_y

    def update(self,dt):
        self.ball.move()
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if self.ball.top>self.top or self.ball.y<self.y:
            self.ball.vel_y *= -1
        
        if self.ball.right>self.right:
            self.player1.score+=1
            self.reset()
        elif self.ball.x<self.x:
            self.player2.score+=1
            self.reset()
            
class PongApp(App):
    def build(self):
        game = PongGame()
        game.reset()
        print "game center is %s" % game.center
        Clock.schedule_interval(game.update,1.0/60.0)
        return game
    

if __name__ == "__main__":
    PongApp().run()
