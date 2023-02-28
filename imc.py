import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('LightGreen2')
     # layout
        layout = [
            [sg.Text('Digite seu peso e a sua altura: ')],
            [sg.Text('Peso (Kg)', size=(7,0)),sg.Input(size=(25,0),key='Peso')],
            [sg.Text('Altura (M)', size=(7,0)),sg.Input(size=(25,0),key='Altura')],
            [sg.Button('Calcular')]
        ]
        #Janela
        self.janela = sg.Window('Calculadora de IMC').layout(layout)
       
    
    def Iniciar(self):
        while True:
            # Extração de dados da tela
            self.button, self.values = self.janela.Read()
            peso = self.values['Peso']
            alt = self.values['Altura']
            print(f'Peso: {peso}')
            print(f'Altura: {alt}')

tela = TelaPython()
tela.Iniciar()
