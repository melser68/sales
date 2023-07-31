from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="В магазин !",
                    pos_hint={"center_x": 0.5, "center_y": 0.6},
                ),
                MDRectangleFlatButton(
                    text="      Вихід      ",
                    pos_hint={"center_x": 0.5, "center_y": 0.4},
                )
            )
        )
    

MainApp().run()