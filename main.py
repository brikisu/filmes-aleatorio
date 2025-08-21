from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

FILMES = [
    "Anabelle - 2017",
    "Until Dawn - 2025",
    "Invocação do Mal - 2016",
    "O homem nas trevas - 2016",
    "Miles Morales - 2023",
    "A Freira - 2018",
    "A Morte te dá Parabéns - 2017",
    "A Morte te dá Parabéns 2 - 2019",
    "Uncharted - 2022",
    "Indiana Jones - 2023",
    "Velozes e Furiosos 9 - 2021",
    "Panico - 2022",
    "Superman - 2023",
    "Homem Aranha - 2023",
    "Batman - 2022",
    "Mulher Maravilha - 2020",
    "Capitã Marvel - 2019",
    "Shazam - 2019",
    "Vingadores Ultimato - 2019",
    "Vingadores Guerra Infinita - 2018",
    "Pantera Negra - 2018",
    "Deadpool - 2016",
    "Crepusculo Eclipse - 2010",
    "Crepusculo Amanhecer Parte 1 - 2011",
    "Crepusculo Amanhecer Parte 2 - 2012",
    "Marley e Eu - 2008",
    "A culpa é das estrelas - 2014",
    "A cinco passos de você - 2019",
    "Extraordinario - 2017",
    "Atraves da minha janela - 2022",
    "A Barraca do Beijo - 2018",
    "Gente Grande - 2018",
    "Gente Grande 2 - 2013",
    "Como se fosse a primeira vez - 2004",
    "10 coisas que eu odeio em você - 1999",
    "De repente 30 - 2004",
    "Vóvózona - 2020",
    "Branquelas - 2004",
    "Todo mundo em pânico - 2000",
    "Debi & Loide - 2001",
    "Esqueceram de mim - 1990",
    "Os Novatos - 2000",
    "Rampage - 2018",
    "Godzilla - 2014",
    "King Kong - 2005",
    "Truque de Mestre - 2013",
    "O Quiosque - 2017",
    "Esposa de Mentirinha - 2011",
    "Rango - 2011",
    "Zootopia - 2016",
    "Madagascar - 2005",
    "Kung Fu Panda - 2008",
    "Como Treinar o seu Dragão - 2010",
    "Procurando Nemo - 2003",
    "Divertidamente - 2015",
    "Up - Altas Aventuras - 2009",
    "Toy Story - 1995",
    "Toy Story 2 - 1999",
    "Projeto X - 2012",




]

class FilmeApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(
            orientation="vertical", 
            padding=20,
            spacing=10,
        )

        # Campo para nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome", 
            multiline=False,
            background_color=(155, 1, 5, 87)

        )
        self.layout.add_widget(self.nome_input)

        # Campo para genero
        self.genero_input = TextInput(
            hint_text="Digite um genero de filme", 
            multiline=False,
            background_color=(155, 1, 5, 87)
        )
        self.layout.add_widget(self.genero_input)

    
        self.botao = Button(
            text="Enviar", 
            size_hint=(1, 0.5),
            color =(10, 5, 1, 1),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.botao.bind(on_press=self.verificar_genero)
        self.layout.add_widget(self.botao)

        # Label para resultado
        self.resultado = Label(text="")
        self.layout.add_widget(self.resultado)

        return self.layout

    def verificar_genero(self, instance):
        nome = self.nome_input.text.strip()
        genero_texto = self.genero_input.text.strip()

        # Verificação de erros
        if not nome or not genero_texto:
            self.resultado.text = "Faz tudo ae cria."
            return

        try:
            genero = int(genero_texto)
        except ValueError:
            self.resultado.text = "Fala um número certo ae cria."
            return

        # Lógica da genero
        if genero < 18:
            filme = random.choice(FILMES)
            self.resultado.text = f"Olá, {nome}! O filme sugerido para você é: {filme}."
        elif genero > 60:
            filme = random.choice(FILMES)
            self.resultado.text = f"Olá, {nome}! Você é uma pessoa de muita sabedoria! generos avançadas requerem grandes cuidados :)"
        else:
            filme = random.choice(FILMES)
            self.resultado.text = f"Olá, {nome}! Você é maior de genero."


if __name__ == "__main__":
    FilmeApp().run()