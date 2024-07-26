from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class CalculatorApp(App):
    pass

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.N1 = ""
        self.N2 = ""
        self.Operater = ""
        self.Answer = 0
        self.Display_Text = StringProperty("-")

    def Number_Button(self,Number):
        if self.N1 == "":
            self.N1 = int(Number)
            self.Display_Text = Number
        elif self.Operater != "":
            self.N2 = int(Number)
            self.Display_Text += Number
    
    def Operater_Buttons(self,op):
        if self.Operater == "":
            self.Operater = op
            self.Display_Text += op
    
    def Reset(self):
        self.N1 = ""
        self.N2 = ""
        self.Operater = ""
    
    def Calculate(self):
        if self.N2 != "":
            if self.Operater == "+": self.Answer = self.N1 + self.N2
            elif self.Operater == "-": self.Answer = self.N1 - self.N2
            elif self.Operater == "*": self.Answer = self.N1 * self.N2
            elif self.Operater == "/": self.Answer = self.N1/self.N2
            self.Reset()
            self.Display_Text = self.Answer



CalculatorApp().run()