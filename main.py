from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


def calculation(a, b, c, d, f):
    a = int(a.text)
    b = int(b.text)
    c = int(f.text)
    d = int(d.text)
    f = int(f.text)
    oklad_fakt = a / f * c
    st_sy_4asa = (oklad_fakt + oklad_fakt * 0.26) / c
    prem = (oklad_fakt + oklad_fakt * 0.26 + st_sy_4asa * 0.5 * d) * b / 100
    staz = (oklad_fakt + oklad_fakt * 0.26 + st_sy_4asa * 0.5 * d) * 0.1
    zp = oklad_fakt + prem + staz + oklad_fakt * 0.26 + st_sy_4asa * 0.5 * b / 100
    return str(zp)


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.lable_1 = Label(text='РАСЧЁТ ЗАРАБОТНОЙ ПЛАТЫ')
        a = self.input_data_a = TextInput(hint_text='Оклад')
        b = self.input_data_b = TextInput(hint_text='Премия')
        c = self.input_data_c = TextInput(hint_text='Кол-во отработанных часов')
        d = self.input_data_d = TextInput(hint_text='Кол-во сверхурочных часов')
        f = self.input_data_f = TextInput(hint_text='Норма часов')
        self.button = Button(text='Результат', size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        self.lable_2 = Label()
        self.button.bind(on_press=self.on_press_button)


    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.lable_1)
        box.add_widget(self.input_data_a)
        box.add_widget(self.input_data_b)
        box.add_widget(self.input_data_c)
        box.add_widget(self.input_data_d)
        box.add_widget(self.input_data_f)

        box.add_widget(self.button)
        box.add_widget(self.lable_2)

        # box.add_widget(self.button)


        return box

    def on_press_button(self, instance):

        self.lable_2.text = calculation(self.input_data_a,self.input_data_b,self.input_data_c,
                          self.input_data_d,self.input_data_f)


if __name__ == '__main__':
    app = MainApp()
    app.run()