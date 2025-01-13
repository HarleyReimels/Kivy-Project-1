from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from datetime import datetime




class Interface(FloatLayout):
    
        
    def buttonClicked(self):
        current_time = datetime.now().strftime("%H:%M")
        self.ids.my_label.text = self.ids.my_textinput.text
        
        
class ProjectApp(App):
    pass

ProjectApp().run()