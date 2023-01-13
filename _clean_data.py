import openpyxl as openpyxl
from openpyxl.styles import Alignment
import warnings as warnings
from pathlib import Path
from operator import itemgetter

# constants used throughout data cleaning
NUM_CLASS_LIST_COLS = 11
NUM_ACTIVITY_HEADER_COLS = 7
NUM_MAX_STUDENTS = 32


def load_file(full_file_path):
    """ Load data from an Excel file. NOTE: the load typically throws this error "UserWarning: Data Validation
    extension is not supported and will be removed warn(msg)", as openpyxl does not support data validation
    (see dropdown OLG and SC columns on 'Tracking Sheet') but should NOT affect overall functioning of this program.
    The 'warnings' module removes the warning from printing in the turn terminal to minimize confusion.
    :param full_file_path: file path to document to open
    :return: opened workbook
    """
    file_path = Path(str(full_file_path))
    file_name = file_path.name
    warnings.simplefilter(action='ignore', category=UserWarning)
    # print(f"\t\tFile <{str(file_name)}> has loaded successfully.")
    return openpyxl.load_workbook(full_file_path, data_only=True)


def class_data_set(file_path):
    """
    Opens the class data file that contains multiple sheets. Opens the class_list sheet and converts data
    to an array for data analysis and manipulation. Opens the assessment_data sheet and converts data to
    an array for data analysis and manipulation
    :param file_path: file path to find tracking document
    :return: data[0] = class_list, data[1] = assessment data
    """
    wb = load_file(full_file_path=file_path)
    profile_sheet = wb["Student_List"]
    class_list = []
    for row in profile_sheet.values:
        if row[0] is not None:
            student_data = []
            for col in range(0, NUM_CLASS_LIST_COLS):
                student_data.append(row[col])
            class_list.append(student_data)
    class_list.pop(0)  # remove header row so all that remains is raw data

    assessment_sheet = wb["Tracking"]
    assessment_data = []
    for row in assessment_sheet.values:
        if row[0] is not None:
            activity_data = []
            for col in range(0, NUM_ACTIVITY_HEADER_COLS + len(class_list)):
                activity_data.append(row[col])
            assessment_data.append(activity_data)
    assessment_data.pop(0)  # remove header row so that all that remains is raw data

    standards_sheet = wb["Standards"]
    standards_data = []
    for row in standards_sheet.values:
        if row[0] is not None:
            standards_data.append(row)
    #standards_data.pop(0)

    previous_olg = ""
    previous_sc = ""
    num_olg = 0
    num_sc = 0
    olg_codes = []
    sc_codes = []
    for row in standards_data:
        current_olg = row[7]
        current_sc = row[8]
        if current_olg != previous_olg:
            num_olg += 1
            olg_codes.append(current_olg)
        if current_sc != previous_sc:
            num_sc += 1
            sc_codes.append(current_sc)
        previous_olg = current_olg
        previous_sc = current_sc
    olg_codes.pop(0)
    sc_codes.pop(0)

    teacher_info_sheet = wb["Teacher_Info"]
    teacher_info = {}
    for row in teacher_info_sheet.values:
        teacher_info[row[0]]=row[1]

    data = {"class list":class_list,                    # array
            "assessment data":assessment_data,          # array
            "standards data":standards_data,            # array
            "number of olg":num_olg,                    # int
            "number of sc":num_sc,                      # int
            "olg codes":olg_codes,                      # array
            "sc codes":sc_codes,                        # array
            "teacher info":teacher_info                 # dictionary
            }

    return data


def final_eval_question_doc(root_directory):
    question_bank_path = f"{root_directory}/Final Evaluation Prompts.xlsx"
    wb = load_file(full_file_path=question_bank_path)
    courses = wb.sheetnames
    print("")
    print("Final Evaluation Question Bank")
    print(">> Which question bank are you accessing?")
    for c in range (0, len(courses)):
        print(f"\t {c+1}) {courses[c]}")
    valid_entry = False
    while valid_entry is False:
        ua = int(input("\tINPUT >>> "))
        if ua >= 1 and ua <= len(courses):
            valid_entry = True
        else:
            print("\t\t\t\t <<<Invalid Entry>>>")

    course_sheet = wb[courses[ua-1]]

    question_bank = []
    for row in course_sheet.values:
        if row[0] is not None:
            question_data = []
            #for col in range(0, 6):
            #    question_data.append(row[col])
            question_bank.append(row)
    #question_bank.pop(0)  # remove header row so all that remains is raw data

    return question_bank




