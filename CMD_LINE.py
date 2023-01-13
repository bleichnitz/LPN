from _date_time import today_date, current_time
from _file_directory import list_files_in_root_directory, create_new_class, create_class_sub_folder, \
    open_class, create_subfolder
from _clean_data import class_data_set
from _sort_data import sort_class_data
from _filter_data import choose_filter_type, convert_data, filtering_data, highest_learning_targets
from _filter_data import achievement_frequency, evaluate_achievements, determine_high_achievements
from _filter_data import achievement_category_status

from __DOCS_settings import section_labels
from __DOCS_summary_sheet import create_midterm_summaries
from __DOCS_missing_work import missing_work_summaries
from __DOCS_create_graph import create_graph
from __DOCS_final_eval_questions import final_eval_question_doc, final_evaluation_questions


def print_hr():
    print("")
    print("----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------")
    print("")
    return 0


def cmd_line():
    # confirm that the root directory is correct; lists files and sub_folders
    print_hr()
    print(f"Run Time: {today_date()}  {current_time()}")
    print_hr()
    # TODO: create config file for root directory work
    root_directory = "/Users/work/OneDrive - Peel District School Board/OneDrive Desktop/GradeBook V4"
    root_directory = list_files_in_root_directory(root_directory)
    print_hr()

# open existing or create new class
    valid_entry = False
    while valid_entry is False:
        print("Do you want to:")
        print("\t 1) create a new class")
        print("\t 2) open existing class")
        ua = int(input("\tINPUT >>> "))
        print("")
        if ua == 1:
            # create new class
            valid_entry = True
            create_new_class(directory=root_directory["directory"])
            return 0
        elif ua == 2:
            # choose class to work with
            course_path = open_class(directory=root_directory["directory"])
            valid_entry = True

    print_hr()

    # working with classes
    valid_entry = False
    cleaned_data = class_data_set(file_path=course_path)
    print("")

    student_list = cleaned_data["class list"]
    assessment_data = cleaned_data["assessment data"]
    standards_data = cleaned_data["standards data"]
    num_olg = cleaned_data["number of olg"]
    num_sc = cleaned_data["number of sc"]
    olg_codes = cleaned_data["olg codes"]
    sc_codes = cleaned_data["sc codes"]
    teacher_info = cleaned_data["teacher info"]

    numeric_data = convert_data(data_to_convert=assessment_data,
                                num_students=len(student_list),
                                conversion_type="letter_to_number")
    filter_criteria = choose_filter_type()

    alpha_filtered_data = filtering_data(filter_type=filter_criteria,
                                         data_to_filter=assessment_data,
                                         olg_codes=olg_codes,
                                         sc_codes=sc_codes,
                                         alpha_numeric="alpha")

    numeric_filtered_data = filtering_data(filter_type=filter_criteria,
                                           data_to_filter=numeric_data,
                                           olg_codes=olg_codes,
                                           sc_codes=sc_codes,
                                           alpha_numeric="numeric")

    print(f"Number of Cats Data Sorted into: {len(numeric_filtered_data)}")

    learning_targets = highest_learning_targets(data_to_analyze=numeric_filtered_data)

    criteria_frequency = achievement_frequency(filter_type=filter_criteria,
                                               olg_codes=olg_codes,
                                               sc_codes=sc_codes)

    # print_hr()

    achievements = evaluate_achievements(num_students=len(student_list),
                                         student_list=student_list,
                                         num_criteria=len(numeric_filtered_data),
                                         data_to_analyze=numeric_filtered_data)

    criteria_achievements = achievements["Criteria Achievement"]
    cascading_achievements = achievements["Cascading Achievement"]

    highest_category_achievements = determine_high_achievements(num_students=len(student_list),
                                                                student_list=student_list,
                                                                data_to_analyze=cascading_achievements,
                                                                data_for_activity_count=numeric_filtered_data,
                                                                frequency_requirements=criteria_frequency)

    achievement_status = achievement_category_status(student_data=highest_category_achievements,
                                                     targets=learning_targets,
                                                     student_list=student_list)

    # TODO: for some reason there is some sort of mis-determination of high achievement /
    #  achievement status showing up on mid-term summary

    print_hr()

    while valid_entry is False:
        print("Do you want to:")
        print("\t1) clean_sort students by alpha")
        print("\t2) clean_sort students by GoogleID")
        print("\t3) print missing work summary")
        print("\t4) create mid-term progress summary")
        print("\t5) create end-of-term progress summary")
        print("\t6) create summary graphs")
        print("\t7) create individualized final evaluation prompts")
        ua = int(input("\tINPUT >>> "))
        if ua == 0:
            break
        if ua >= 1 and ua <= 7:
            valid_entry = True
            if ua >= 1 and ua <= 2:
                # sort data
                if ua == 1:
                    sort_class_data(sort_method="alpha",
                                    file_path=course_path,
                                    class_list=student_list,
                                    assessment_data=assessment_data)
                elif ua == 2:
                    sort_class_data(sort_method="googleID",
                                    file_path=course_path,
                                    class_list=student_list,
                                    assessment_data=assessment_data)
            elif ua >= 3 and ua <= 7:
                # create new subfolder within the class folder for
                new_folder_name = {3: "Missing Work Lists",
                                   4: "Mid-Term Summaries",
                                   5: "End-of-Term Summaries",
                                   6: "Graphed Achievement",
                                   7: "Final Evaluation Questions"}
                created_doc_folder = create_subfolder(course_file_path=course_path,
                                                      new_subfolder_name=new_folder_name[ua])
                print("")

                if ua == 3:
                    missing_work_summaries(num_students=len(student_list),
                                           student_info=student_list,
                                           raw_data=assessment_data,
                                           teacher_info=teacher_info,
                                           save_directory=created_doc_folder,
                                           root_directory=root_directory["directory"])
                if ua == 4:
                    graph_choice = ask_to_inluce_graph()
                    create_midterm_summaries(reporting_cycle="mid-term",
                                             num_students=len(student_list),
                                             student_info=student_list,
                                             filter_type=filter_criteria,
                                             standards_data=standards_data,
                                             achievement_data=numeric_filtered_data,
                                             learning_targets=learning_targets,
                                             highest_achievements=highest_category_achievements,
                                             achievement_status=achievement_status,
                                             include_graph=graph_choice,
                                             teacher_info=teacher_info,
                                             save_directory=created_doc_folder,
                                             root_directory=root_directory["directory"])
                if ua == 5:
                    graph_choice = ask_to_inluce_graph()
                    create_midterm_summaries(reporting_cycle="end-of-term",
                                             num_students=len(student_list),
                                             student_info=student_list,
                                             filter_type=filter_criteria,
                                             standards_data=standards_data,
                                             achievement_data=numeric_filtered_data,
                                             learning_targets=learning_targets,
                                             highest_achievements=highest_category_achievements,
                                             achievement_status=achievement_status,
                                             include_graph=graph_choice,
                                             teacher_info=teacher_info,
                                             save_directory=created_doc_folder,
                                             root_directory=root_directory["directory"])
                if ua == 6:
                    # determine x-axis labels
                    labels = section_labels(filter_type=filter_criteria,
                                            olgs_sc_data_set=standards_data)
                    if filter_criteria == "OLG" or filter_criteria == "KTCA":
                        x_axis = labels["Category Names"]
                    else:
                        x_axis = labels["Sub-Category Names"]

                    # print summary graphs
                    for student in range(0, len(student_list)):
                        create_graph(filter_type=filter_criteria,
                                     targets=learning_targets,
                                     achievement=highest_category_achievements[student],
                                     goal_labels=x_axis,
                                     f_name=student_list[student][0],
                                     l_name=student_list[student][1],
                                     student_num=student_list[student][2],
                                     save_path=created_doc_folder)

                if ua == 7:
                    final_evaluation_questions(num_students=len(student_list),
                                               student_list=student_list,
                                               teacher_info=teacher_info,
                                               achievement_data=highest_category_achievements,
                                               standards_data=standards_data,
                                               olg_codes=sc_codes,
                                               sc_codes=sc_codes,
                                               save_directory=created_doc_folder,
                                               root_directory=root_directory["directory"])

    print("")
    print("")

    return 0


def ask_to_inluce_graph():
    v_entry = False
    while v_entry is False:
        ask_graph = input(f"\t\tDo you want to include a graph of student achievement in the "
                          f"summary doc? (y/n)\t")
        if ask_graph.lower() == "y":
            graph_choice = True
            v_entry = True
        elif ask_graph.lower() == "n":
            graph_choice = False
            v_entry = True
    return graph_choice