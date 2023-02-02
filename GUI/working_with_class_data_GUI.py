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

def working_with_class_data():
    # ----- ZONE 2.1 (working with classes - left column: select select) -----
    courses = ["AVI1O0B", "AVI2O0A", "AVI3M0B", "AVI1O0A"]  # TODO: to be sourced from file system
    class_list_layout = [[Sg.Text(text="Choose Class...", text_color=text_sub_header_colour, font=text_sub_header_font,
                                  background_color=text_box_background)],
        *[[Sg.Radio(text=course, group_id="courses", size=radio_size_small,
                    key=f"-{course.upper()} KEY-",
                    font=radio_font, pad=radio_padding,
                    background_color=radio_background_colour), ] for course in courses]
    ]

    # ----- ZONE 2.2 (working with classes - middle column: report options) -----
    work_with_classes_layout = [
        [Sg.Text(text="Select Report Options...", text_color=text_sub_header_colour, font=text_sub_header_font,
                 background_color=text_box_background)],
        [Sg.Text(text="Sort Student Data:", font=text_font, background_color=text_box_background,
                 size=(25, 1), justification="left")],
        [Sg.Radio(text="Alpha by Last Name", group_id="sort_type", size=radio_size_large,
                  key="-ALPHA-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
        [Sg.Radio(text="By Google ID", group_id="sort_type", size=radio_size_large,
                  key="-GOOGLE_ID-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour),
         ],  # end section 1
        [Sg.HorizontalSeparator()],
        [Sg.Text(text="Reporting Cycle:", font=text_font, background_color=text_box_background,
                 size=(25, 1), justification="left")],
        [Sg.Radio(text="Progress Report", group_id="reporting_cycle", size=radio_size_small,
                  key="-PROGRESS_REPORT-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
        [Sg.Radio(text="Mid-Term", group_id="reporting_cycle", size=radio_size_small,
                  key="-MID_TERM_REPORT-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
         [Sg.Radio(text="Final Term", group_id="reporting_cycle", size=radio_size_small,
                  key="-FINAL_TERM_REPORT-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
        [Sg.HorizontalSeparator()],
        [Sg.Text(text="Filter Achievement Data by:", font=text_font, background_color=text_box_background,
                 size=(25, 1), justification="left")],
        [Sg.Radio(text="OLG", group_id="filter_type", size=radio_size_small,
                  key="-OLG_FILTER-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
         [Sg.Radio(text="SC (Success Criteria)", group_id="filter_type", size=radio_size_small,
                  key="-SC_FILTER-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
         [Sg.Radio(text="KTCA (Achievement Chart Categories)", group_id="filter_type", size=radio_size_small,
                  key="-KTCA_FILTER-",
                  font=radio_font, pad=radio_padding,
                  background_color=radio_background_colour)],
        [Sg.HorizontalSeparator()],
        [Sg.Text(text="Include Elements in Report:", font=text_font, background_color=text_box_background,
                 size=(25, 1), justification="left")],
        [Sg.Checkbox(text="Include Graph ", size=checkbox_size,
                     key="-INCLUDE_GRAPH-",
                     font=checkbox_font, pad=checkbox_padding,
                     background_color=checkbox_background_colour)]
    ]
    # TODO: add secondary column here for frequency of criteria in grade determination
    frequency_categories = ["Knowledge", "Thinking", "Communication", "Application"]
    achievement_explanation = "Achievement Frequency refers to the number of times that the student must demonstrate " \
                              "PROFICIENCY in a given category in order to fully demonstrate that they have mastered the " \
                              "criteria. The value in a given category should be proportionate to the number of " \
                              "opportunities that the students have to demonstrate their learning."
    frequency_layout = [
        [Sg.Text(text="Set Frequency Requirements...", text_color=text_sub_header_colour, font=text_sub_header_font,
                 background_color=text_box_background)],
        [Sg.Text(text=achievement_explanation, size=(55,6), font=text_font_emphasis, text_color="black",
         background_color=text_box_background)],
        *[[Sg.Input(key=f"-{cat} Frequency Key-",
                    default_text=1,
                    font=input_field_font, text_color=input_filed_text_colour,
                    justification="center", size=(5, 1),
                    background_color=input_field_background_colour, visible=True),
           Sg.Text(text=cat, font=text_font, background_color=text_box_background)] for cat in frequency_categories]
    ]
    # ---- ZONE 3.3 (working with classes - right column: actions to be taken

    # ----- ZONE 2.3 (working with classes - right column: user actions) -----
    user_actions_layout = [
        [Sg.Button(button_text="Sort Student Data",
                   key="-GOOGLE_ID-",
                   tooltip=" sort selected class MS Excel data by Google Id ",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)],
        [Sg.Button(button_text="Missing Work Summary",
                   key="-MISSING_WORK-",
                   tooltip="print missing work summaries for selected class",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)],
        [Sg.Button(button_text="Achievement Summary",
                   key="-ACHIEVEMENT_SUMMARIES-",
                   tooltip="create achievement summary based on selected class and parameters",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)],
        [Sg.Button(button_text="Achievement Graphs",
                   key="-ACHIEVEMENT_GRAPHS-",
                   tooltip="view achievement graphs",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)],
        [Sg.Button(button_text="FE Prompts",
                   key="-FE_PROMPTS-",
                   tooltip="create final evaluation documents for students in selected class",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)]
    ]


    # ----- ZONE 2 COLUMNS -----
    options_background_colour=colours["light"]

    options_layout=[[Sg.Column(layout=class_list_layout, size=(250, 550), pad=(5,5),
                               background_color=options_background_colour,
                               scrollable=False, visible=True, vertical_alignment="top"),
                    Sg.VerticalSeparator(),
                    Sg.Column(layout=work_with_classes_layout, size=(400, 550), pad=(5,5),
                              background_color=options_background_colour,
                              scrollable=False, visible=True, vertical_alignment="top"),
                    Sg.Column(layout=frequency_layout, size=(400, 550), pad=(5,5),
                              background_color=options_background_colour,
                              scrollable=False, visible=True, vertical_alignment="top"),
                    Sg.VerticalSeparator(),
                    Sg.Column(layout=user_actions_layout, size=(250, 550), pad=(5,5),
                              background_color=options_background_colour,
                              scrollable=False, visible=True, vertical_alignment="top")]]

    return options_layout
