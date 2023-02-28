import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
     # layout
        layout = [
            [sg.Text('Peso'),sg.Input()],
            [sg.Text('Altura'),sg.Input()],
            [sg.Button('Calcular')]
        ]
        janela = sg.Window('Calculadora de IMC').layout(layout)
        self.button, self.values = janela.Read()
    def Iniciar(self):
        print(self.values)
tela = TelaPython()
tela.Iniciar()