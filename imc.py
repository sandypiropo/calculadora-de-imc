import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('LightGreen2')
     # layout
        layout = [
            [sg.Text('Digite seu peso e a sua altura: ')],
            [sg.Text('Peso (Kg)', size=(7,0)),sg.Input(size=(25,0),key='Peso')],
            [sg.Text('Altura (M)', size=(7,0)),sg.Input(size=(25,0),key='Altura')],
            [sg.Button('Calcular')],
            [sg.Text('', size=(40,1), key='output')]
        ]
        #Janela
        self.janela = sg.Window('Calculadora de IMC').layout(layout)
       
    
    def Iniciar(self):
        while True:
            # Extração de dados da tela
            self.button, self.values = self.janela.Read()
            peso = float(self.values['Peso'])
            alt = float(self.values['Altura'])

            if self.button == 'Calcular':
                imc = peso / (alt ** 2)

                if imc < 18.5:
                    resultado = 'Abaixo do peso'
                elif 18.5 <= imc < 25:
                    resultado = 'Peso ideal'
                elif 25 <= imc <= 30:
                    resultado = 'Sobrepeso'
                elif imc <= 40:
                    resultado = 'Obesidade'
                else:
                    resultado = 'Obesidade morbida'

                self.janela.Element('output').Update(f'Seu IMC é: {imc:.2f}. Classificação: {resultado}')

tela = TelaPython()
tela.Iniciar()

