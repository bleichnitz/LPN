from pathlib import Path
import shutil as shutil


def list_files_in_root_directory(directory):
    """
    LIST FILES IN ROOT DIRECTORY
    :param directory:
    :return: directory_contents ([0] = root directory [1] = files [2] = folders
    """

    directory_contents = {"directory": "",
                          "files": "",
                          "sub directories": ""
                          }

    root_directory = ""
    valid_path = False
    while valid_path is False:
        rd_confirmation = input(f"Confirm root directory: <<{directory}>> (Y/N): \t")
        if rd_confirmation.lower() == "y":
            # root_directory is correct
            root_directory = directory
            valid_path = True
        elif rd_confirmation.lower() == "n":
            # root_directory is incorrect and will be reassigned
            root_directory = input("\tInput root directory for save folder:\n\t>>>")
            # TODO: how to get this new directory to be remembered so that it does not need to be re-entered each time
            # TODO: need error handling to ensure valid directory
            valid_path = True
        if valid_path is True:
            save_folder = Path(root_directory)
            sub_folders = []
            files = []
            print(f"\tFILES:")
            for item in save_folder.iterdir():
                if item.name != ".DS_Store" and item.is_file():
                    files.append(item.name)
                    print(f"\t\t{item.name}")
            print(f"\tSUB_FOLDERS:")
            for item in save_folder.iterdir():
                if item.is_dir():
                    sub_folders.append(item.name)
                    print(f"\t\t{item.name}")
            directory_contents = {"directory": root_directory,
                                  "files": files,
                                  "sub directories": sub_folders
                                  }
        else:
            directory_contents = {"directory": "",
                                  "files": "",
                                  "sub directories": ""
                                  }
    return directory_contents


def create_new_class(directory):
    """
    1) CALL THE 'create_class_sub_folder' FUNCTION TO CREATE A CLASS FOLDER AND DUPLICATES 'gradebook.xlsx'
    TEMPLATE FILE
    2) OPENS THE OLG / SC STANDARDS FILE, LISTS SHEETS, SO THAT YOU CAN CHOOSE THE STANDARDS TO COPY INTO THE NEW FILE
    :param directory:
    :return: the path to the new file
    """
    directory = f"{directory}"
    print("\n Create new class:")
    course_code = input(f"\t\tCourse Code: \t")
    period = input(f"\t\tPeriod: \t")
    teacher = input(f"\t\tTeacher: \t")
    sub_directory_name = f"{course_code} - Period {period} ({teacher})"
    new_directory = create_class_sub_folder(directory=directory,
                                            sub_directory_name=sub_directory_name)
    src_file = str(f"{directory}/_templates/work_book_template.xlsx")
    dst_file = str(f"{new_directory}/{sub_directory_name} Gradebook.xlsx")
    new_file = shutil.copyfile(src=str(src_file), dst=str(dst_file))
    # TODO: open standards workbook
    # TODO: list all the sheets that have standards data
    # TODO: user selects data
    # TODO: copy data from the standards workbook to the standards sheet in the class workbook
    # TODO: save and close file
    # TODO: save teacher data to a metadata file
    return new_file


def create_class_sub_folder(directory, sub_directory_name):
    """
    CREATE SUB-FOLDERS FOR EACH CLASS THAT YOU CREATE
    :param directory:
    :param sub_directory_name:
    :return:
    """
    save_folder = Path(directory)
    new_path = save_folder.joinpath(f"{directory}/_classes/{sub_directory_name}")
    if not new_path.exists():
        new_path.mkdir(parents=True, exist_ok=True)
    new_folder_path = new_path.joinpath(new_path)
    return new_folder_path


def open_class(directory):
    """
    OPEN A CLASS AND LOAD THE XLSX TO EXTRACT DATA
    :param directory:
    :return:
    """
    print("Choose class file to work with (select #):")
    classes = []
    class_directory = Path(f"{directory}/_classes")
    c = 1
    for item in class_directory.iterdir():
        if item.is_dir():
            classes.append(item.name)
            print(f"\t{c}.  {item.name}")
            c += 1
    selection = int(input(f"\tINPUT > "))
    selected_class_workbook_path = f"{class_directory}/{classes[selection-1]}"
    files = []
    folders = []
    for item in Path(selected_class_workbook_path).iterdir():
        if item.is_file():
            files.append(item.name)
            # print(f"\t\t\tFile: {item.name}")
    for item in Path(selected_class_workbook_path).iterdir():
        if item.is_dir():
            folders.append(item.name)
            # print(f"\t\t\tFolder: {item.name}")
    file_path = f"{selected_class_workbook_path}/{classes[selection-1]} Gradebook.xlsx"
    # print(f"\t\t\tPath: {file_path}")
    # TODO: open file with openpyxl
    # TODO: extract student list data
    # TODO: clean student list data
    # TODO: extract student achievement data
    # TODO: clean student achievement data
    return file_path


def create_subfolder(course_file_path, new_subfolder_name):

    file = Path(course_file_path)
    course_save_folder = file.parent
    save_folder = Path(course_save_folder)

    new_path = f"{save_folder}/{new_subfolder_name}"
    new_path = save_folder.joinpath(new_path)
    if not new_path.exists():
        new_path.mkdir(parents=True, exist_ok=True)
        print(f"Created subfolder: {new_path}")
    new_folder_path = new_path.joinpath(new_path)
    return new_folder_path
