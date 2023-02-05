def parse_new_class_info(values):
    class_info = {"code": values["-COURSE_CODE-"],
                  "section": values["-SECTION-"],
                  "period": values["-PERIOD-"],
                  "year": values["-SCHOOL_YEAR-"],
                  "semester": values["-SEMESTER-"],
                  "teacher": values["-TEACHER-"],
                  "email": values["-TEACHER_EMAIL-"],
                  "password": values["-TEACHER_PSWD-"],
                  "2 factor": values["-TEACHER_2FACTOR_PSWD-"],
                  "class list": values["-CLASS_LIST_CSV-"],
                  "save directory": values["-ROOT_DIRECTORY-"]
                  }
    for value in class_info:
        print(value)
    return class_info
