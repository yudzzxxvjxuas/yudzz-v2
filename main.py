from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    
    FitImage:
        source: "https://media.tenor.com/S_vT-K9lX2QAAAAC/gojo-satoru-jujutsu-kaisen.gif"
        opacity: 0.6

    MDLabel:
        text: "YUDZZ V2 - BUG ENGINE"
        halign: "center"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        bold: True

    MDTextField:
        id: target_num
        hint_text: "Nomor Target (Contoh: 628xxx)"
        mode: "fill"
        fill_color_normal: 1, 1, 1, .1
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8

    MDRaisedButton:
        text: "KIRIM BUG GANAS"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: app.kirim_bug()

    MDLabel:
        text: "Status: Ready to Void"
        id: status_label
        halign: "center"
        pos_hint: {"center_y": .3}
        theme_text_color: "Secondary"
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def kirim_bug(self):
        target = self.root.ids.target_num.text
        if target:
            self.root.ids.status_label.text = f"Mengirim Bug ke {target}..."
            # Logika payload bug wa simulasi
        else:
            self.root.ids.status_label.text = "Isi nomor dulu, Bos!"

MainApp().run()
        
