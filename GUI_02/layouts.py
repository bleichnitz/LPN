import PySimpleGUI as Sg

from class_create_new import parse_new_class_info

root_directory = "/Users/work/OneDrive - Peel District School Board/OneDrive Desktop/GradeBook V3"

# Colour Generator: http://colormind.io/bootstrap/
colours = {"light": "#ebf4f6",
           "light_accent": "#bdeaee",
           "main": " #76b4bd",
           "dark_accent": "#58668b",
           "dark": "#5e5656",
           "text field grey": "#4f4d4d",
           "white": "#000000"}

# --- frames ---
frame_header_font_large = ("Arial Bold", 18)
frame_header_font_small = ("Arial Bold", 16)
frame_font_colour = colours["dark"]

# --- text labels ---
text_font = ("Arial", 15)
text_font_emphasis = ("Arial Italic", 12)
text_box_size_small = (20, 2)
text_box_padding = (5, 5)
text_box_background = colours["light"]
text_sub_header_colour = colours["dark"]
text_sub_header_font = ("Arial", 17)

# --- buttons ---
button_font = ("Arial", 13)
button_size = (20, 1)
button_padding = (10, 10)
button_colour = colours["main"]

# --- radio boxes ---
radio_font = ("Arial", 13)
radio_size_small = (25, 1)
radio_size_large = (35, 1)
radio_padding = (5, 5)
radio_background_colour = colours["light"]

# --- checkboxes ---
checkbox_font = ("Arial", 13)
checkbox_size = (25, 1)
checkbox_padding = (5, 5)
checkbox_background_colour = colours["light"]

# --- input field ---
input_field_background_colour = colours["light_accent"]
input_filed_text_colour = colours["text field grey"]
input_field_font = ("Arial", 15)

# --- combo box / drop down ---
combo_background_colour = colours["light_accent"]


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

def edit_cell(window, key, row, col, justify="left"):
    global edit
    global text_variable

    def callback(event, row, col, text, key):
        global edit
        widget = event.widget
        if key == "Focus_Out":
            text = widget.get()
        widget.destroy()
        widget.master.destroy()

        values = list(table.item(row, 'values'))
        values[col] = text
        table.item(row, values=values)
        edit = False

    if edit or row <=0:
        # allows for single cell editing
        return

    edit = True
    root = window.TKroot
    table = window[key].Widget
    text = table.item(row, "values")[col]
    x, y, width, height = table.bbox(row, col)

    frame = Sg.tk.Frame(root)
    x += 481
    y += 247
    frame.place(x=x, y=y, anchor="nw", width=width, height=height)

    text_variable = Sg.tk.StringVar()
    text_variable.set(text)

    entry = Sg.tk.Entry(frame, textvariable=text_variable, justify=justify)
    entry.pack()
    entry.select_range(0, Sg.tk.END)
    entry.icursor(Sg.tk.END)
    entry.focus_force()

    entry.bind("<FocusOut>", lambda e, r=row, c=col, t=text, k="Focus_Out": callback(e, r, c, t, k))

def layouts():

    #Sg.set_options(dpi_awareness=True)
    global edit
    edit = False

    header_layout = [
        [Sg.Image("GUI_01/GUI_images/long_header.png")
         ],
        [Sg.Button(button_text="Create New Class",
                   key="-NEW_CLASS-", tooltip="create a new spreading sheet",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
         Sg.Button(button_text="Open Classes",
                   key="-OPEN_CLASS-", tooltip="work with an existing class",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
         Sg.Button(button_text="Work with Standards",
                   key="-OPEN_STANDARDS-",
                   tooltip="edit / revise / add standards",
                   size=button_size, font=button_font, pad=button_padding, button_color=button_colour)
         ]
    ]

    directory_layout = [
        [Sg.Input(key="-ROOT_DIRECTORY-",
                  default_text=root_directory, font=input_field_font, text_color=input_filed_text_colour,
                  justification="left", size=(100, 1),
                  background_color=input_field_background_colour, visible=True),
         Sg.FolderBrowse(button_text="Browse Directories",
                         key="-BROWSE_DIRECTORIES-",
                         tooltip="search your system for a save folder",
                         size=button_size, font=button_font,
                         pad=button_padding, button_color=button_colour)
         ]
    ]

    copyright_layout = [
        # [Sg.Button(button_text="SAVE SETTINGS",
        #            key="-SAVE_SETTINGS-",
        #            size=button_size, font=button_font, pad=button_padding, button_color=button_colour),
        #  Sg.Button(button_text="QUIT",
        #            key="-QUIT-", size=button_size, font=button_font,
        #            pad=button_padding, button_color=button_colour)
        #  ],
        [Sg.Text(text="Ⓒ 2023  -- Learning Progression Notebook v1.0", pad=(20, 10),
                 background_color=colours["dark_accent"])
         ]
    ]

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    create_class_default_text = {"Course Codes": ["AVI1O0", "AVI2O0", "AVI3M0", "AVI4M0"],
                                 "Section": ["A", "B", "C", "D", "E", "F", "G"],
                                 "Period": ["1", "2", "3", "4", "5"],
                                 "School Year": ["2022-2023", "2023-2024"],
                                 "Semester": ["1", "2"],
                                 "Teacher": ["Copeland", "Kelly", "Leichnitz"]
                                 }

    ccl_col1 = [[Sg.Text(text="Course Code:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["Course Codes"],
                          key="-COURSE_CODE-",
                          size=(10, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="Section:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["Section"],
                          key="-SECTION-",
                          size=(10, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="Period:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["Period"],
                          key="-PERIOD-",
                          size=(10, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="School Year:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["School Year"],
                          key="-SCHOOL_YEAR-",
                          size=(19, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="Semester:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["Semester"],
                          key="-SEMESTER-",
                          size=(10, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right')],
                [Sg.Text(text="Teacher:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=create_class_default_text["Teacher"],
                          key="-TEACHER-",
                          size=(19, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="Teacher Email:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Input(default_text="",
                          key="-TEACHER_EMAIL-",
                          size=(20, 1), font=text_font)
                 ],
                [Sg.Text(text="Email Password:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Input(default_text="",
                          key="-TEACHER_PSWD-",
                          size=(20, 1), font=text_font)
                 ],
                [Sg.Text(text="2 Factor Identification Code:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Input(default_text="",
                          key="-TEACHER_2FACTOR_PSWD-",
                          size=(20, 1), font=text_font)
                 ],
                [Sg.Text(text="", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='left')],
                ]

    class_list_header = ["Student #", "First Name", "Last Name", "Email", "Google ID"]

    class_list_data = [
        ["p0072841", "Brian", "Leichnitz", "p0072841@pdsb.net", "BL - p0072841"],
        ["p0072841", "Brian", "Leichnitz", "p0072841@pdsb.net", "BL - p0072841"],
        ["p0072841", "Brian", "Leichnitz", "p0072841@pdsb.net", "BL - p0072841"],
        ["p0072841", "Brian", "Leichnitz", "p0072841@pdsb.net", "BL - p0072841"],
    ]

    ccl_col2 = [[Sg.Input(key="-CLASS_LIST_CSV-",
                          default_text="", font=input_field_font, text_color=input_filed_text_colour,
                          justification="left", size=(43, 1),
                          background_color=input_field_background_colour, visible=True),
                Sg.FileBrowse(button_text="Browse Class List CSV",
                              key="-BROWSE_CLASS_LIST-",
                              tooltip="search your system for class list as CSV file",
                              size=button_size, font=button_font,
                              pad=button_padding, button_color=button_colour)],
                [Sg.Text(text="Class List Preview:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(32, 1), justification='left')],
                [Sg.Table(values=class_list_data,
                          headings=class_list_header,
                          max_col_width=40,
                          auto_size_columns=True,
                          row_height=25,
                          font=text_font,
                          justification="center",
                          key="-FREQUENCY TABLE-",
                          enable_click_events=True,)],
                ]

    ccl_columns = [[Sg.Column(layout=ccl_col1, background_color=colours["dark_accent"],
                              pad=(20, 20), scrollable=False,
                              vertical_alignment="top",
                              size=(400, 325)),
                   Sg.Column(layout=ccl_col2, background_color=colours["dark_accent"],
                             pad=(20, 20), scrollable=False,
                             vertical_alignment="top",
                             size=(650, 325))],
                   [Sg.Text(text="", font=text_font, background_color=colours["dark_accent"],
                            size=(87,1)),
                    Sg.Button(button_text="Create Class",
                               key="-CREATE_CLASS-",
                               size=(30,1), font=button_font,
                               pad=button_padding, button_color=button_colour)]
                   ]

    create_class_layout = [[Sg.Frame(title="Create New Class", title_color=colours["white"],
                                     font=frame_header_font_large,
                                     layout=ccl_columns, size=(1090, 450),
                                     background_color=colours["dark_accent"])],
                           ]

    # ------------------------------------------------------------------------------------------------------------------


    report_options = {"Sort": ["Alpha by Last Name", "GoogleID"],
                      "Reporting Cycle": ["Progress Report", "Mid-Term", "End of Term"],
                      "Filter": ["OLG", "SC", "KTCA"]}

    crl_col1 = [[Sg.Text(text="Choose Class:", font=text_sub_header_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(17, 1), justification='left')
                 ],
                 [Sg.Combo(values=create_class_default_text["Course Codes"],
                          key="-REPORT_COURSE-",
                          size=(37, 1), font=text_font,
                          background_color=combo_background_colour)
                 ],
                [Sg.Text(text="", font=text_sub_header_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='left')],
                [Sg.Text(text="Report Options:", font=text_sub_header_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='left')],
                [Sg.Text(text="Sort Student Data:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                Sg.Combo(values=report_options["Sort"],
                         key="-SORT_METHOD-",
                         size=(15, 1), font=text_font,
                         background_color=combo_background_colour)],
                [Sg.Text(text="Reporting Cycle:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=report_options["Reporting Cycle"],
                          key="-REPORT_CYCLE-",
                          size=(15, 1), font=text_font,
                          background_color=combo_background_colour)],
                [Sg.Text(text="Filter Data By:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Combo(values=report_options["Filter"],
                          key="-FILTER_TYPE-",
                          size=(15, 1), font=text_font,
                          background_color=combo_background_colour)],
                [Sg.Text(text="Include Elements in Report:", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Check(text="Include Graph", font=text_font,
                          key="-INCLUDE_GRAPH-",
                          background_color=colours["dark_accent"])
                 ],
                [Sg.Text(text="", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Check(text="Include Achievement Zone", font=text_font,
                          key="-INCLUDE_ZONE-",
                          background_color=colours["dark_accent"])
                 ],
                [Sg.Text(text="", font=text_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(20, 1), justification='right'),
                 Sg.Check(text="Include Percentages", font=text_font,
                          key="-INCLUDE_PERCENT-",
                          background_color=colours["dark_accent"])]

    ]

    frequency_table_headers = ["Criteria", "B","D","P","C","E"]
    frequency_table_data = [["Process", 3, 3, 2, 2, 1],
                            ["Decisions", 3, 3, 2, 1, 1],
                            ["Responsibility", 3, 3, 2, 1, 1],
                            ["Techniques", 3, 3, 2, 1, 1],
                            ["Connections", 3, 3, 2, 2, 1],
                            ["CAP", 3, 3, 1, 1, 1],
                            ["Vocabulary", 3, 3, 3, 1, 1]]

    crl_col2 = [[Sg.Text(text="Set Achievement Frequency:", font=text_sub_header_font, pad=text_box_padding,
                         background_color=colours["dark_accent"],
                         size=(40, 1), justification='left')],
                [Sg.Table(values=frequency_table_data,
                          headings=frequency_table_headers,
                          max_col_width=40,
                          auto_size_columns=False,
                          row_height=25,
                          font=text_font,
                          justification="center",
                          key="-FREQUENCY_TABLE-",
                          enable_click_events=True,)],
                ]

    crl_columns = [[Sg.Column(layout=crl_col1, background_color=colours["dark_accent"],
                              pad=(20, 20), scrollable=False,
                              vertical_alignment="top",
                              size=(400, 325)),
                    #Sg.VerticalSeparator(),
                    Sg.Column(layout=crl_col2, background_color=colours["dark_accent"],
                             pad=(20, 20), scrollable=False,
                             vertical_alignment="top",
                              size=(600, 325))],
                   [Sg.Text(text="", font=text_font, background_color=colours["dark_accent"],
                            size=(55,1)),
                    Sg.Button(button_text="Sort Spreadsheet",
                              key="-SORT_SPREADSHEET-",
                              size=(30, 1), font=button_font,
                              pad=button_padding, button_color=button_colour),
                    Sg.Button(button_text="Run Report",
                               key="-RUN_REPORT-",
                               size=(30,1), font=button_font,
                               pad=button_padding, button_color=button_colour)],
                   ]

    reports_layout = [[Sg.Frame(title="Class Achievement Analysis", title_color=colours["white"],
                                     font=frame_header_font_large,
                                     layout=crl_columns, size=(1090, 450),
                                     background_color=colours["dark_accent"])],
                      ]

    run_layout = [
        [Sg.Frame(title="",
                  layout=header_layout,
                  background_color=colours["dark_accent"], border_width=0,
                  visible=True)],
        [Sg.Column(layout=create_class_layout, key="-WINDOW1-", visible=True,
                   background_color=colours["dark_accent"]),
         Sg.Column(layout=reports_layout, key="-WINDOW2-", visible=False,
                   background_color=colours["dark_accent"])
         ],
        [Sg.Frame(title="Save Directory",
                  layout=directory_layout,
                  font=frame_header_font_large,
                  title_color="black",
                  background_color=colours["dark_accent"], border_width=1,
                  visible=True)],
        [Sg.Frame(title="",
                  layout=copyright_layout,
                  background_color=colours["dark_accent"], border_width=0,
                  visible=True)],
    ]

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    current_layout = 1
    window = Sg.Window(title="Learning Progression Notebook", layout=run_layout,
                       background_color=colours["dark_accent"],
                       resizable=True,
                       finalize=True
                       )
    while True:
        event, values = window.read()
        #print(event, values)
        if event in (None, 'Exit', Sg.WIN_CLOSED):
            break

        if event == "-CREATE_CLASS-":
            window[f'-WINDOW{current_layout}-'].update(visible=False)
            current_layout = 1
            window[f'-WINDOW{current_layout}-'].update(visible=True)
        elif event == "-OPEN_CLASS-":
            window[f'-WINDOW{current_layout}-'].update(visible=False)
            current_layout = 2
            window[f'-WINDOW{current_layout}-'].update(visible=True)

        #--- edit achievement frequency table ---
        if isinstance(event, tuple):
            if isinstance(event[2][0], int) and event[2][0] > -1:
                cell = row, col = event[2]
            edit_cell(window, '-FREQUENCY_TABLE-', row+1, col, justify="right")

        if event == "-CREATE_CLASS-":
            parse_new_class_info(values=values)

    window.close()
