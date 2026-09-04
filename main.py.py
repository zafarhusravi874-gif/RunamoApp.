import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

class Screen1(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="РУНАМО", halign="center", font_style="H4", theme_text_color="Primary")
        subtitle = MDLabel(text="ЁВАРИ РАҚАМИИ ОМӮЗГОР", halign="center", font_style="Subtitle1")
        desc = MDLabel(text="Барнома барои автоматикунонии\nнақшаи дарс ва намоиши дарсӣ", halign="center")
        
        author = MDLabel(text="Тарроҳ ва таҳиягар: Отахонзода Хусрав\nдонишҷӯи факултети информатика", halign="center")
        note = MDLabel(text="Тақвияти саводнокӣ бо технологияҳои нав", halign="center", theme_text_color="Secondary")
        
        btn_start = MDRaisedButton(
            text="ОҒОЗ КАРДАН",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen2')
        )
        
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(desc)
        layout.add_widget(author)
        layout.add_widget(note)
        layout.add_widget(btn_start)
        self.add_widget(layout)

class Screen2(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="РУНАМО - СОХТАНИ МАВОДИ ДАРСӢ", halign="center", font_style="Subtitle1")
        
        subject_input = MDTextField(hint_text="Фанни таълимӣ", text="Биология")
        class_input = MDTextField(hint_text="Синф", text="5 ум")
        topic_input = MDTextField(hint_text="Мавзӯи дарс", text="Растаниҳо")
        
        btn_gen_plan = MDRaisedButton(
            text="ГЕНЕРАТСИЯИ НАҚШАИ ДАРС",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen5')
        )
        btn_gen_sld = MDRaisedButton(
            text="ГЕНЕРАТСИЯИ НАМОИШИ ДАРСӢ",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen5')
        )
        
        status_label = MDLabel(text="Коркарди маълумот...", halign="center", theme_text_color="Secondary")
        
        layout.add_widget(title)
        layout.add_widget(subject_input)
        layout.add_widget(class_input)
        layout.add_widget(topic_input)
        layout.add_widget(btn_gen_plan)
        layout.add_widget(btn_gen_sld)
        layout.add_widget(status_label)
        self.add_widget(layout)

class Screen3(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="ИНТЕГРАТСИЯИ ЗЕҲНИ СУНЪӢ (AI)", halign="center", font_style="H6")
        desc = MDLabel(text="• Таҳлили барномаҳои таълимӣ\n• Генерацияи нақшаи дарс\n• Генерацияи намоиши дарсӣ\n• Ҷустуҷӯи маводи мултимедиявӣ", halign="center")
        
        btn_next = MDRaisedButton(
            text="Генератсияи Нақшаи Дарс",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen4')
        )
        btn_back = MDFlatButton(
            text="Ба қафо гаштан",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen2')
        )
        
        layout.add_widget(title)
        layout.add_widget(desc)
        layout.add_widget(btn_next)
        layout.add_widget(btn_back)
        self.add_widget(layout)
class Screen4(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="КОРКАРДИ СИСТЕМА (AI Search)", halign="center", font_style="H6")
        info = MDLabel(text="1. Маълумоти воридӣ (Синф, Мавзӯъ)\n2. Коркарди система ва таҳлили мавод\n3. Ҷустуҷӯи мақолаҳо ва галереяи суратҳо", halign="center")
        
        btn_next = MDRaisedButton(
            text="ИНТИЗОРИИ КОРКАРД",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen5')
        )
        
        layout.add_widget(title)
        layout.add_widget(info)
        layout.add_widget(btn_next)
        self.add_widget(layout)

class Screen5(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=20, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="Лутфан, интизор шавед...\nКоркарди маълумот истодааст.", halign="center")
        progress = MDLabel(text="65%", halign="center", font_style="H3", theme_text_color="Primary")
        quote = MDLabel(text="Сабр ва такмили илм кафолати муваффақият аст", halign="center", theme_text_color="Secondary")
        
        btn_finish = MDRaisedButton(
            text="ДИДАНИ НАТИҶАИ НИҲОӢ",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen6')
        )
        
        layout.add_widget(title)
        layout.add_widget(progress)
        layout.add_widget(quote)
        layout.add_widget(btn_finish)
        self.add_widget(layout)

class Screen6(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = MDLabel(text="ТАБРИК!", halign="center", font_style="H5", theme_text_color="Primary")
        desc = MDLabel(text="Нақшаи дарси кушод омода аст!\nБо вуруди муваффақият устод кушод!", halign="center")
        doc_info = MDLabel(text="Нақшаи дарси комил ва Намоиши дарсӣ омода аст", halign="center")
        
        btn_save = MDRaisedButton(text="ЗАХИРА КАРДАН", pos_hint={'center_x': 0.5})
        btn_share = MDFlatButton(text="ФИРИСТОДАН", pos_hint={'center_x': 0.5})
        btn_menu = MDFlatButton(
            text="Ба оғоз баргаштан",
            pos_hint={'center_x': 0.5},
            on_release=lambda x: setattr(self.manager, 'current', 'screen1')
        )
        
        layout.add_widget(title)
        layout.add_widget(desc)
        layout.add_widget(doc_info)
        layout.add_widget(btn_save)
        layout.add_widget(btn_share)
        layout.add_widget(btn_menu)
        self.add_widget(layout)

class RunamoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        sm = MDScreenManager()
        sm.add_widget(Screen1(name="screen1"))
        sm.add_widget(Screen2(name="screen2"))
        sm.add_widget(Screen3(name="screen3"))
        sm.add_widget(Screen4(name="screen4"))
        sm.add_widget(Screen5(name="screen5"))
        sm.add_widget(Screen6(name="screen6"))
        return sm

if __name__ == '__main__':
    RunamoApp().run()
