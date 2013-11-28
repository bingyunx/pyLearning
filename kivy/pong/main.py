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

class PongBall(Widget):
    pass

class PongGame(Widget):
    def on_touch_down(self, touch):
        print "(%d,%d)" % (touch.x, touch.y)

class PongApp(App):
    def build(self):
        game = PongGame()
        print "game center is %s" % game.center
        return game
    

if __name__ == "__main__":
    PongApp().run()
