import PySimpleGUI as Sg
from main_layout import main_layout
from working_with_class_data_GUI import working_with_class_data


colours = {"light": "#A6A4A6",
               "light_accent": "#ADA88D",
               "main": "#E46F1C",
               "dark_accent": "#A37B5B",
               "dark": "#31615B",
               "text field grey": "#4f4d4d"}

# --- CREATE GUI -------------------------------------------------------------------------------------------------------

layout = main_layout(selection="")

window = Sg.Window(title="Learning Progression Notebook",
                   layout=layout,
                   size=(1400, 1100),
                   background_color=colours["light"],
                   resizable=True,
                   finalize=False)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break