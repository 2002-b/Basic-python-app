import kivy
from kivy.app import App

from kivy.uix.label import Label



class SpartanApp(App):

    def build(self):

        return Label(text="This is Bhairavi!!!")

if __name__ =="__main__":
    SpartanApp().run()
