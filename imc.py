import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
     # layout
        layout = [
            [sg.Text('Digite seu peso e a sua altura: ')],
            [sg.Text('Peso (Kg)', size=(5,0)),sg.Input(size=(25,0),key='peso')],
            [sg.Text('Altura (M)', size=(5,0)),sg.Input(size=(25,0),key='alt')],
            [sg.Button('Calcular')]
        ]
        #Janela
        self.janela = sg.Window('Calculadora de IMC').layout(layout)
       
    
    def Iniciar(self):
        while True:
            # Extração de dados da tela
            self.button, self.values = self.janela.Read()
            peso = self.values['peso']
            alt = self.values['alt']
            print(f'peso: {peso}')
            print(f'alt: {alt}')

tela = TelaPython()
tela.Iniciar()
