from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
Window.size = (500,700)
class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        button = Button(
            text='test',
            pos_hint={'center_x': 0.5, 'center_y': 0.745},
            size_hint=(None, None),
            background_normal='',
            background_down='',
            size=(60, 60)
        )
        button.bind(on_press=self.go_to_screen2)
        with self.canvas:
            size_x = Window.size
            x1 = size_x[0]
            size_y = Window.size
            y1 = size_y[1]
            Color(0, 0.5, 1, 1)
            Rectangle(pos=(0, y1), size=(x1,100))
            Color(1, 1, 1, 1)
            Rectangle(pos=(0, 0), size=(Window.size[0],Window.size[1]))
        label = Label(
            text='MATH TESTER',
            font_size = 40,
            color = (0, 0, 0, 1),
            font_name = 'Roboto',
            pos_hint = {'center_x':0.5, 'center_y':0.925},
            bold= True
        )
        img_menu = Image(
            source = 'menu.png',
            pos_hint = {'center_x':0.075, 'center_y':0.925},
            size_hint = (None, None),
            size = (60,60)
        )
        with self.canvas:
            Color(1, 0, 0, 1)
            Line(circle=(Window.size[0]/3.2, Window.size[1]-80, 50), width = 5)
            Color(0, 0.2, 0.8, 1)
            Line(circle=(Window.size[0] / 3.2 + 150, Window.size[1] - 250, 50), width=5)
            Color(0, 1, 0, 1)
            Line(circle=(Window.size[0] / 3.2 - 150, Window.size[1] - 250, 50), width=5)
            Color(0, 0, 0, 1)
            Line(points=(Window.size[0]/3.2 -150, Window.size[1]-195, Window.size[0]/3.2, Window.size[1]-135), width=3)
            Line(points=(Window.size[0] / 3.2 + 150, Window.size[1] - 195, Window.size[0] / 3.2, Window.size[1] - 135),
                 width=3)
        img1 = Image(
            source = 'treasure.png',
            pos_hint ={'center_x':0.5, 'center_y': 0.25},
            size_hint = (None,None),
            size = (150,150)
        )
        labe1 = Label(
            text = 'BOSS I',
            color = (1, 1, 0, 1),
            font_size = 40,
            bold = True,
            font_name = 'Roboto',
            pos_hint = {'center_x':0.5, 'center_y':0.1},
            outline_color = (0, 0, 0, 1),
            outline_width = 3

        )

        self.add_widget(button)
        self.add_widget(labe1)
        self.add_widget(img1)
        self.add_widget(img_menu)
        self.add_widget(label)

    def go_to_screen2(self, instance):
        app = App.get_running_app()
        app.root.current = 'screen2'
class Screen2(Screen):
    pass
class Test1(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        return sm
Test1().run()
