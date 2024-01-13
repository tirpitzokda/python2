from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from instructions import*

Window.clearcolor = (.55, 0.45, 0.6, 0.4)
btn_color = (0.97, 0.9, 0.8, 1)

age = 7
name = ''
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Введите имя', halign = 'right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введите возраст', halign = 'right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text = 'Начать', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.9,None), height = '30sp')
        line2 = BoxLayout(size_hint=(0.9,None), height = '30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        return sm

app = HeartCheck()
app.run()
