from kivymd.app import MDApp
from kivy.lang import Builder
KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    FitImage:
        source: "https://media.tenor.com/S_vT-K9lX2QAAAAC/gojo-satoru-jujutsu-kaisen.gif"
        opacity: 0.7
    MDLabel:
        text: "YUDZZ V2\\nUNLIMITED VOID"
        halign: "center"
        font_style: "H4"
        theme_text_color: "Error"
        bold: True
'''
class MainApp(MDApp):
    def build(self): return Builder.load_string(KV)
MainApp().run()
