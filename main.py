from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class CalculatorApp(App):
    pass

class MainScreen(BoxLayout):
    Display_Text = StringProperty("-")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.N1 = ""
        self.N2 = ""
        self.Operater = ""
        self.Answer = ""
        
    def Number_Button(self,Number):
        if self.Operater == "":
            self.N1 += Number
            self.Display_Text = self.N1
        else:
            self.N2 += Number
            self.Display_Text += Number
    
    def Operater_Buttons(self,op):
        if self.Operater == "" and (self.N1 != "" or self.Answer != ""):
            self.Operater = op
            self.Display_Text += op
            if self.N1 == "": self.N1 = self.Answer
    
    def Reset(self):
        self.N1 = ""
        self.N2 = ""
        self.Operater = ""
    
    def Clear(self):
        if self.N2 != "":
            self.N2 = ""
            self.Display_Text = self.Display_Text[:self.Display_Text.find(self.Operater) + 1]
        elif self.Operater != "":
            self.Display_Text = self.Display_Text[:self.Display_Text.find(self.Operater)]
            self.Operater = ""
        else: 
            self.N1 = ""
            self.Display_Text = "-"

    def Calculate(self):
        if self.N2 != "":
            self.N1 = int(self.N1)
            self.N2 = int(self.N2)
            if self.Operater == "+": self.Answer = self.N1 + self.N2
            elif self.Operater == "-": self.Answer = self.N1 - self.N2
            elif self.Operater == "*": self.Answer = self.N1 * self.N2
            elif self.Operater == "/": self.Answer = self.N1/self.N2
            self.Reset()
            self.Display_Text = str(self.Answer)

CalculatorApp().run()