from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
for i in range(341):
    i_png=open(f"outputpng\\{i}.png", "r+")
KV = '''
ScrollView:

    MDList:
        id: container
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineIconListItem(text=f"Item {i}", icon="language-python")


            )

Test().run()