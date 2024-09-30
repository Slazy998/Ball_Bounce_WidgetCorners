from kivy.graphics import Rectangle, Color, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button

class Ball_bounce(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)


class Rect_Move(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, .8, .4)
            self.rect = Rectangle(pos=self.center, size=(dp(200), dp(100)))
            print(self.rect)

    def on_size(self,*args):
        x=(self.rect.size[0]/2)
        y=(self.rect.size[1]/2)
        self.rect.pos=(self.center_x-x, self.center_y-y)


    def on_click_right(self):
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)

    def on_click_up(self):
        x, y = self.rect.pos
        y += dp(10)
        self.rect.pos = (x, y)

    def on_click_left(self):
        x, y = self.rect.pos
        x -= dp(10)
        self.rect.pos = (x, y)

    def on_click_down(self):
        x, y = self.rect.pos
        y -= dp(10)
        self.rect.pos = (x, y)

class CanvasExample1(Widget):
    pass

class CanvasExample(Widget):
    pass

class ButtonClick(GridLayout):
    my_text=StringProperty("Hello")
    count = 0
    checker=StringProperty("OFF")
    valid=BooleanProperty(False)
    valid_count=BooleanProperty(True)
    slider_label=StringProperty("0")
    text_input_str = StringProperty("foo")
    def on_click_progress(self):
        if self.valid:
            print("Button Clicked")
            self.count += 1
            self.my_text = str(self.count)

    def toggle_track(self,toggle):
        print(f'Toggle Button clicked: {toggle.state}')
        if toggle.state == "normal":
            self.checker="OFF"
            self.valid=False
            self.valid_count=True

        if toggle.state == "down":
            self.checker="ON"
            self.valid=True
            self.valid_count=False

    def on_slider_value(self,slider_value):
        self.slider_label=str(int(slider_value.value))

    def on_switch_valid(self,value):
        print(f'The switch is {value.active}')

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class MainPageLayout(PageLayout):
    pass

class MainScrollLayout(ScrollView):
    pass

class MainStackLayout(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i + 1), size_hint=(None,None), size=(dp(100),dp(100)))
            self.add_widget(b)

class MainGridLayout(GridLayout):
    pass

class MainAnchorLayout(AnchorLayout):
    pass

class MainBoxLayout(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class infra(App):
    pass

if __name__ == "__main__":
    infra().run()
