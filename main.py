from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



class CalculatorApp(App):
    pass

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.N1 = 0
        self.N2 = 0
        self.Operater = ""

    def Number_Button(self,Number):
        print(Number)  
    
    def Operater_Buttons(self,op):print(op)




CalculatorApp().run()