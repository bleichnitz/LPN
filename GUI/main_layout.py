import PySimpleGUI as Sg  # PySimpleGUI Call Reference: https://www.pysimplegui.org/en/latest/call%20reference/

from working_with_class_data_GUI import working_with_class_data
from create_new_class_GUI import create_new_class

# ----- Theme Variables -----
def main_layout(selection=""):
    # Colour Generator: http://colormind.io/bootstrap/
    colours = {"light": "#A6A4A6",
               "light_accent": "#ADA88D",
               "main": "#E46F1C",
               "dark_accent": "#A37B5B",
               "dark": "#31615B",
               "text field grey": "#4f4d4d"}

    # --- frames ---
    frame_header_font_large = ("Arial Bold", 18)
    frame_header_font_small = ("Arial Bold", 16)
    frame_font_colour = colours["dark"]

    # --- text labels ---
    text_font = ("Arial", 15)
    text_font_emphasis = ("Arial Italic", 12)
    text_box_size_small = (20, 2)
    text_box_padding = (5,5)
    text_box_background = colours["light"]
    text_sub_header_colour = colours["dark"]
    text_sub_header_font = ("Arial", 17)

    # --- buttons ---
    button_font = ("Arial", 13)
    button_size = (20, 1)
    button_padding = (10, 20)
    button_colour = colours["main"]

    # --- radio boxes ---
    radio_font = ("Arial", 13)
    radio_size_small = (25, 1)
    radio_size_large = (35, 1)
    radio_padding = (5,5)
    radio_background_colour = colours["light"]

    # --- checkboxes ---
    checkbox_font = ("Arial", 13)
    checkbox_size = (25,1)
    checkbox_padding = (5,5)
    checkbox_background_colour = colours["light"]

    # --- input field ---
    input_field_background_colour = colours["light_accent"]
    input_filed_text_colour = colours["text field grey"]
    input_field_font = ("Arial", 15)


    # --- LAYOUT ELEMENTS -------------------------------------------------------------------------------------------------

    # ----- ZONE 1 (header) -----
    header_layout = [[Sg.Image("/Users/brian/PycharmProjects/pythonProject/GUI_LAYOUTS_IMAGES/long_header.png")],
               [Sg.Button(button_text="Create New Class",
                          key="-CREATE_CLASS-", tooltip="create a new spreading sheet",
                          size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
                Sg.Button(button_text="Open Classes",
                          key="-OPEN_CLASS-", tooltip="work with an existing class",
                          size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
                Sg.Button(button_text="Work with Standards",
                          key="-OPEN_STANDARDS-",
                          tooltip="edit / revise / add standards",
                          size=button_size, font=button_font, pad=button_padding, button_color=button_colour)]]

    # ----- ZONE 2 (user work space) -----

    #options_layout = working_with_class_data()
    options_layout = create_new_class()

    # ----- ZONE 3 (save directory) -----
    root_directory = "    ...no save folder currently selected..."
    directory_layout = [[Sg.Input(key="-ROOT_DIRECTORY-",
                                  default_text=root_directory,
                                  font=input_field_font, text_color=input_filed_text_colour,
                                  justification="left", size=(100,1),
                                  background_color=input_field_background_colour, visible=True),
                         Sg.FolderBrowse(button_text="Browse Directories",
                                         key="-BROWSE_DIRECTORIES-",
                                         tooltip="search your system for a save folder",
                                         size=button_size, font=button_font,
                                         pad=button_padding, button_color=button_colour)]]




    # ----- ZONE 4 (save, exit, copyright) -----
    copyright_layout = [[Sg.Button(button_text="SAVE SETTINGS",
                                   key="-SAVE_SETTINGS-",
                                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
                        Sg.Button(button_text="QUIT",
                                  key="-QUIT-",size=button_size, font=button_font,
                                  pad=button_padding, button_color=button_colour)],
                        [Sg.Text(text="Ⓒ 2023  -- Learning Progression Notebook v1.0", pad=(20, 10),
                                 background_color=text_box_background)]]


    # --- CREATE LAYOUT ----------------------------------------------------------------------------------------------------

    frame_header_colour = colours["dark"]
    frame_padding = (5,5)
    frame_background_colour = colours["light"]

    layout = [[Sg.Frame(layout=header_layout, size=(1400, 180), background_color=frame_background_colour, pad=frame_padding,
                       title="", title_color=frame_header_colour, font=frame_header_font_large,
                       visible=True, vertical_alignment="top")],
              [Sg.Frame(layout=options_layout, size=(1400, 500), background_color=frame_background_colour, pad=frame_padding,
                       title="Work with Classes", title_color=frame_header_colour, font=frame_header_font_large,
                       visible=True, vertical_alignment="top")],
              [Sg.Frame(layout=directory_layout, size=(1400, 100), background_color=frame_background_colour, pad=frame_padding,
                       title="Save Directory", title_color=frame_header_colour, font=frame_header_font_large,
                       visible=True, vertical_alignment="top")],
              [Sg.Frame(layout=copyright_layout, size=(1400, 120), background_color=frame_background_colour, pad=frame_padding,
                       title="", title_color=frame_header_colour, font=frame_header_font_large,
                       visible=True, vertical_alignment="top")]]

    return layout

