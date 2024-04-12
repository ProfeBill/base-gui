from kivy.app import App


from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

# Logica de la tarjeta de credito
from CreditCard.Payments import CreditCardCalculator

class PaymentApp(App):
    def build(self):
        contenedor = GridLayout(cols=2,padding=20,spacing=20)

        contenedor.add_widget( Label(text="Valor de la compra") )
        self.compra = TextInput(font_size=30 )
        contenedor.add_widget(self.compra)

        # Siempre se retorna el widget que contiene a todos los demás
        return contenedor
        

if __name__ == "__main__":
    PaymentApp().run()