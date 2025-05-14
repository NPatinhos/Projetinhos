from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CombustivelApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Entradas principais
        self.gasolina_comum = TextInput(hint_text='Valor da Gasolina Comum (R$)', input_filter='float')
        self.gasolina_aditivada = TextInput(hint_text='Valor da Gasolina Aditivada (R$)', input_filter='float')
        self.etanol = TextInput(hint_text='Valor do Etanol (R$)', input_filter='float')

        # Entrada de percurso
        self.distancia = TextInput(hint_text='Distância do percurso (km)', input_filter='float')
        self.autonomia = TextInput(hint_text='Autonomia usando Gasolina (km/l)', input_filter='float')

        # Botão adicionar percurso
        self.botao_adicionar_percurso = Button(text='Adicionar Percurso', size_hint=(1, 0.3))
        self.botao_adicionar_percurso.bind(on_press=self.adicionar_percurso)

        # Lista de percursos adicionados
        self.lista_percursos = Label(text='Percursos adicionados: 0', size_hint=(1, 0.3))

        # Botão calcular
        self.botao_calcular = Button(text='Calcular Melhor Combustível', size_hint=(1, 0.4))
        self.botao_calcular.bind(on_press=self.calcular)

        # Resultado
        self.resultado = Label(text='')

        # Adicionando componentes ao layout
        self.layout.add_widget(self.gasolina_comum)
        self.layout.add_widget(self.gasolina_aditivada)
        self.layout.add_widget(self.etanol)
        self.layout.add_widget(self.distancia)
        self.layout.add_widget(self.autonomia)
        self.layout.add_widget(self.botao_adicionar_percurso)
        self.layout.add_widget(self.lista_percursos)
        self.layout.add_widget(self.botao_calcular)
        self.layout.add_widget(self.resultado)

        # Lista para armazenar percursos
        self.percursos = []

        return self.layout

    def adicionar_percurso(self, instance):
        try:
            distancia = float(self.distancia.text)
            autonomia = float(self.autonomia.text)
            self.percursos.append((distancia, autonomia))
            self.lista_percursos.text = f"Percursos adicionados: {len(self.percursos)}"
            self.distancia.text = ''
            self.autonomia.text = ''
        except:
            self.lista_percursos.text = "⚠️ Preencha corretamente distância e autonomia!"

    def calcular(self, instance):
        try:
            preco_gc = float(self.gasolina_comum.text)
            preco_ga = float(self.gasolina_aditivada.text)
            preco_et = float(self.etanol.text)

            if not self.percursos:
                self.resultado.text = "⚠️ Adicione pelo menos um percurso!"
                return

            # Inicializar os custos
            custos = {'Gasolina Comum': 0, 'Gasolina Aditivada': 0, 'Etanol': 0}

            for distancia, autonomia_gasolina in self.percursos:
                autonomia_etanol = autonomia_gasolina * 0.7  # Corrigindo a eficiência do etanol

                custos['Gasolina Comum'] += (distancia / autonomia_gasolina) * preco_gc
                custos['Gasolina Aditivada'] += (distancia / autonomia_gasolina) * preco_ga
                custos['Etanol'] += (distancia / autonomia_etanol) * preco_et

            melhor = min(custos, key=custos.get)

            self.resultado.text = (f"🏆 Melhor opção: {melhor}\n\n"
                                   f"Gasolina Comum: R$ {custos['Gasolina Comum']:.2f}\n"
                                   f"Gasolina Aditivada: R$ {custos['Gasolina Aditivada']:.2f}\n"
                                   f"Etanol: R$ {custos['Etanol']:.2f}")

        except Exception as e:
            self.resultado.text = "⚠️ Preencha todos os campos corretamente!"

# Rodar o App
if __name__ == '__main__':
    CombustivelApp().run()
