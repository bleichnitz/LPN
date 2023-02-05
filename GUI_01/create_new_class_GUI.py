import PySimpleGUI as Sg  # PySimpleGUI Call Reference: https://www.pysimplegui.org/en/latest/call%20reference/

# ----- Theme Variables -----

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

def create_new_class():

    entry_layout = [
        # row 1
        [Sg.Text(text="Course Code", font=text_font, background_color=text_box_background,
                 size=(15, 1), justification="right"),
        Sg.Input(key="-COURSE_CODE-",
                  default_text="",
                  font=input_field_font, text_color=input_filed_text_colour,
                  justification="center", size=(6, 1),
                  background_color=input_field_background_colour, visible=True),
        Sg.Text(text="Section", font=text_font, background_color=text_box_background,
                size=(8, 1), justification="right"),
        Sg.Combo(key="-SECTION-",
                  values=["A","B","C","D","E","F"],
                  font=input_field_font, text_color=input_filed_text_colour,
                  size=(5, 1),
                  background_color=input_field_background_colour,
                  button_background_color=colours["dark_accent"],
                  visible=True),
        Sg.Text(text="", font=text_font, background_color=text_box_background,
                size=(10, 1), justification="right"),

        Sg.Text(text="Course Name", font=text_font, background_color=text_box_background,
                size=(15, 1), justification="right"),
        Sg.Input(key="-COURSE_NAME-",
             default_text="",
             font=input_field_font, text_color=input_filed_text_colour,
             justification="center", size=(30, 1),
             background_color=input_field_background_colour, visible=True),

        Sg.Text(text="Grade", font=text_font, background_color=text_box_background,
                size=(40, 1), justification="right"),
        Sg.Combo(key="-Grade-",
                 values=["9", "9/10", "10", "11", "11/12", "12"],
                 font = input_field_font, text_color = input_filed_text_colour,
                 size = (5, 1),
                 background_color = input_field_background_colour,
                 button_background_color=colours["dark_accent"],
                 visible = True)]
    ]

    return entry_layout