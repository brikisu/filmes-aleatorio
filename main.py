from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class BoasVindasApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # TÃtulo fixo no topo
        titulo = Label(
            text='[b]Boas-Vindas[/b]',
            font_size=28,
            size_hint=(1, 0.2),
            halign= 'center',
            height=60,
            valign='middle',
            markup=True
        )
        titulo.bind(size=titulo.setter('text_size'))

        self.caixa_nome = TextInput(
            hint_text='Digite seu nome...',
            size_hint=(1, 0.15),
            font_size=20
        )
        self.label = Label(
            text='',
            font_size=22,
            size_hint=(1, 0.2),
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))

        botao = Button(
            text='Enviar',
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            font_size=22,
            size_hint=(1, 0.15),
            height=60,
            valign = "bottom"   # top, middle, bottom
        )

        botao.bind(on_release=self.mostrar_mensagem)

        layout.add_widget(titulo)
        layout.add_widget(self.caixa_nome)
        layout.add_widget(botao)
        layout.add_widget(self.label)
        return layout

    def mostrar_mensagem(self, instance):
        nome = self.caixa_nome.text.strip()
        if nome:
            self.label.text = f'Bem-vindo(a), {nome}!'
        else:
            self.label.text = 'Por favor, digite seu nome.'

if __name__ == '__main__':
    BoasVindasApp().run()