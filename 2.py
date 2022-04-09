# Basic-python-app
import kivy
from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid, self).__init__()
        self.cols= 2

        self.add_widget(Label(text="Employee Name:"))
        self.e_name = TextInput()
        self.add_widget(self.e_name)

        self.add_widget(Label(text="Employee salary:"))
        self.e_salary = TextInput()
        self.add_widget(self.e_salary)

        self.add_widget(Label(text="Empoyee gender:"))
        self.e_gender = TextInput()
        self.add_widget(self.e_gender)

        self.press=Button(text="Click Me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Nme of Empolyee is "+self.e_name.text)
        print("Salary of Employee is "+self.e_salary.text)
        print("Gender of Employee is "+self.e_gender.text)



class SpartanApp(App):
    def build(self):
        return SpartanGrid()


if __name__ =="__main__":
    SpartanApp().run()
