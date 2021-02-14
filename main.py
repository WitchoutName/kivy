import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass

    def pressed(self, instance):
        name = self.name.text
        last = self.last.text
        email = self.email.text

        self.name.text = ""
        self.last.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
