from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget,ImageRightWidget, IconRightWidget
import json

with open("../issues.json") as file:
    issues = json.load(file)



class MyItem(TwoLineAvatarListItem):
    def __init__(self, title, user, status, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = title
        self.secondary_text = user
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{status}.png")
        self.add_widget(self.image)
        # self pracuji s objekt i s předkem, protože dědím

    def on_press(self):
        print(self.text)



class Coments(BoxLayout):
    # kwargs a args pro slovníky, listy atd zkrátka arguments
    def __init__(self, *args, **kwargs):
        super(Coments, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        for i in issues:
            list.add_widget(MyItem(title=i['title'], user=i['user'], status=i["status"]))
        scrollview.add_widget(list)
        self.add_widget(scrollview)