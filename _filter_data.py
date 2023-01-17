def choose_filter_type():
    filter_type = {1: "OLG",
                   2: "SC",
                   3: "KTCA"}
    valid_entry = False
    while valid_entry is False:
        print("How do you want to filter the data?")
        print("\t 1. Overarching Learning Goals")
        print("\t 2. Success Criteria")
        print("\t 3. Achievement Chart Categories (KTCA)")
        ua = int(input("\tINPUT >>> "))
        if ua >= 1 and ua <= 3:
            valid_entry = True

    return filter_type[ua]


def value_conversion(val, conversion_type):

    letters = [["INC", "Incomplete", 0],
               ["n/a", "Not Required", 0],
               ["V", "Vacation", 0],
               ["A", "Absent", 0],
               ["BG", "Significant Learning Gaps", 0.25],
               ["RT", "Re-try", 0.5],
               ["B", "Beginning", 1],
               ["D", "Developing", 2],
               ["P", "Proficient", 3],
               ["C", "Comprehensive", 4],
               ["E", "Exemplary", 5]]

    search_index = 0
    return_index = 0
    if conversion_type == "letter_to_number":
        search_index = 0
        return_index = 2
    elif conversion_type == "number_to_letter":
        search_index = 2
        return_index = 0
    elif conversion_type == "letter_to_word":
        search_index = 0
        return_index = 1
    elif conversion_type == "number_to_word":
        search_index = 2
        return_index = 1

    if conversion_type == "letter_to_word" or conversion_type == "letter_to_number":
        for letter in letters:
            if letter[search_index] == val:
                return letter[return_index]
    elif conversion_type == "number_to_word":
        if val == 0:
            return "Incomplete"
        elif val > 0 and val < 0.3:
            return "BG"
        elif val >= 0.3 and val < 1:
            return "Re-Try"
        elif val == 1:
            return "Beginning"
        elif val > 1 and val < 2:
            return "Working towards Developing"
        elif val == 2:
            return "Developing"
        elif val > 2 and val < 3:
            return "Working towards Proficiency"
        elif val == 3:
            return "Proficient"
        elif val > 3 and val < 4:
            return "Working towards Comprehensive"
        elif val == 4:
            return "Comprehensive"
        elif val > 4 and val < 4.6:
            return "Working towards Exemplary"
        else:
            return "Exemplary"
    elif conversion_type == "number_to_letter":
        if val == 0:
            return "Inc"
        elif val > 0 and val < 0.3:
            return "BG"
        elif val >= 0.3 and val < 1:
            return "RT"
        elif val >= 1 and val < 1.8:
            return "B"
        elif val >= 1.8 and val < 2.8:
            return "D"
        elif val >= 2.8 and val < 3.8:
            return "P"
        elif val >= 3.8 and val < 4.8:
            return "C"
        else:
            return "E"

    return 0


def convert_data(data_to_convert, num_students, conversion_type):
    for row in range(0, len(data_to_convert)):
        # convert the learning target

        data_to_convert[row][5] = value_conversion(val=data_to_convert[row][5],
                                                   conversion_type=conversion_type)
        if data_to_convert[row][5] > 3:
            val = 3
        else:
            val = data_to_convert[row][5]
        data_to_convert[row][5] = val

        # convert student achievement
        for s in range(0, num_students):
            student = 7 + s  # 7 = number of header cols in each row
            data_to_convert[row][student] = value_conversion(val=data_to_convert[row][student],
                                                             conversion_type=conversion_type)
    return data_to_convert


def filtering_data(filter_type, data_to_filter, olg_codes, sc_codes, alpha_numeric):

    if str(filter_type) == "OLG":
        filter_keys = olg_codes
        key_column = 2
    elif str(filter_type) == "SC":
        filter_keys = sc_codes
        key_column = 3
    elif str(filter_type == "KTCA"):
        filter_keys = ["K", "T", "C", "A"]
        key_column = 6

    # filter the data
    print(f"\t\tNum of Categories to filter and convert ({alpha_numeric}): {len(filter_keys)}")
    filtered_data = []
    for f in range(0, len(filter_keys)):
        current_criteria = []
        for row in data_to_filter:
            if row[key_column] == filter_keys[f]:
                current_criteria.append(row)
        filtered_data.append(current_criteria)

    return filtered_data


def highest_learning_targets(data_to_analyze):
    num_categories = len(data_to_analyze)
    targets = []
    for category in range(0, num_categories):
        category_targets = []
        for activity in range(0, len(data_to_analyze[category])):
            if data_to_analyze[category][activity][5] > 3:
                target = 3
            else:
                target = data_to_analyze[category][activity][5]
            category_targets.append(target)  # targets are in col 6 aka index 5
            # print(category_targets)
        max_val = max(category_targets)
        print(max_val)
        targets.append(max_val)
    print(f"\t\tCategory learning targets: {targets}")
    return targets


def achievement_frequency(filter_type, olg_codes, sc_codes):

    num_categories = 0
    frequencies = []
    if filter_type == "OLG":
        num_categories = len(olg_codes)
        category_type = olg_codes
    elif filter_type == "SC":
        num_categories = len(sc_codes)
        category_type = sc_codes
    elif filter_type == "KTCA":
        num_categories = 4
        category_type = ["Knowledge", "Thinking", "Communication", "Application"]

    print("")

    # preset = input("\t\tPreset all category achievement frequency to student demonstrating only once? (y/n))     ")
    # if preset.lower() == "y":

    print("\t\tEnter the number of times student needs to demonstrate the following criteria at the PROFICIENCY "
          "level to earn the credit (frequency should be >= 1):")
    for index in range(0, num_categories):
        cat_frequency = []
        frequency = int(input(f"\t\t\t{category_type[index]}:     "))
        cat_frequency.append(frequency)       # Beginning
        cat_frequency.append(frequency)       # Developing
        cat_frequency.append(frequency)       # Proficient
        if frequency <= 1:
            cat_frequency.append(1)           # Comprehensive
            cat_frequency.append(1)           # Exemplary
        else:
            cat_frequency.append(frequency-1)     # Comprehensive
            cat_frequency.append(frequency-1)     # Exemplary
        frequencies.append(cat_frequency)
    print(f"\t\t\tSummary of Submissions [B,D,P,C,E]: {frequencies}")
    return frequencies


def evaluate_achievements(num_students, student_list, num_criteria, data_to_analyze):
    # print(num_students)
    # print(num_criteria)
    # print(len(data_to_analyze))
    # print(len(frequency))

    print("\t\t\tCascading Student Achievement Summaries:")

    class_criteria_achievement = []
    class_cascading_achievement = []
    for student in range(0, num_students):
        student_id = f"{student_list[student][1]}, {student_list[student][0]} ({student_list[student][2]})"
        student_index = student + 7
        student_achievement = []
        # student_cascading_achievement = []
        for criteria in range(0, num_criteria):
            # achievement_dict = {"INC": 0, "RT": 0.5, "B": 1, "D": 2, "P": 3, "C": 4, "E": 5}
            criteria_achievement = {"INC": 0, "RT": 0, "B": 0, "D": 0, "P": 0, "C": 0, "E": 0}
            for activity in range(0, len(data_to_analyze[criteria])):
                current_achievement = data_to_analyze[criteria][activity][student_index]
                key = get_key_from_value(current_achievement)
                criteria_achievement[key] += 1
            # print(f"{criteria_achievement}")
            student_achievement.append(criteria_achievement)

        student_cascade = cascade_achievement(student_achievement)
        print(f"\t\t\t\t{student_id} >>> {student_cascade}")

        class_criteria_achievement.append(student_achievement)
        class_cascading_achievement.append(student_cascade)

    return {"Criteria Achievement": class_criteria_achievement,
            "Cascading Achievement": class_cascading_achievement}


def get_key_from_value(val):
    achievement_dict = {"INC": 0, "RT": 0.5, "B": 1, "D": 2, "P": 3, "C": 4, "E": 5}
    for key, value in achievement_dict.items():
        if val == value:
            return key
    return 0


def cascade_achievement(student_achievement):
    # print("")
    # print(f"To cascade: {student_achievement}")
    student_cascade = []
    for category in range(0, len(student_achievement)):
        cascading_achievement = {"INC": 0, "RT": 0, "B": 0, "D": 0, "P": 0, "C": 0, "E": 0}
        dictionary = student_achievement[category]
        # print(dictionary)
        for key in reversed(dictionary):
            if str(key).upper() == "RT" or str(key).upper() == "INC":
                pass
            else:
                if key == "E":
                    cascading_achievement["E"] += dictionary["E"]
                    cascading_achievement["C"] += dictionary["E"]
                    cascading_achievement["P"] += dictionary["E"]
                    cascading_achievement["D"] += dictionary["E"]
                    cascading_achievement["B"] += dictionary["E"]
                elif key == "C":
                    cascading_achievement["C"] += dictionary["C"]
                    cascading_achievement["P"] += dictionary["C"]
                    cascading_achievement["D"] += dictionary["C"]
                    cascading_achievement["B"] += dictionary["C"]
                elif key == "P":
                    cascading_achievement["P"] += dictionary["P"]
                    cascading_achievement["D"] += dictionary["P"]
                    cascading_achievement["B"] += dictionary["P"]
                elif key == "D":
                    cascading_achievement["D"] += dictionary["D"]
                    cascading_achievement["B"] += dictionary["D"]
                elif key == "B":
                    cascading_achievement["B"] += dictionary["B"]
                # print(f"\t{key} / {dictionary[key]} >> {cascading_achievement[key]}")
        cascading_achievement["INC"] = dictionary["INC"]
        cascading_achievement["RT"] = dictionary["RT"]
        student_cascade.append(cascading_achievement)
        # print("")
    # print(f"Cascaded: {student_cascade}")
    # print("")
    # print("")
    # print(student_cascade)
    # print(student_cascade)
    return student_cascade


def determine_high_achievements(student_list, data_to_analyze, data_for_activity_count, frequency_requirements):
    # data_to_analyze is now organized by student [{},{},{}....]
    print(f"\t\t\tCategory High Achievements:")
    num_activities_in_cats = []
    for category in range(0, len(data_for_activity_count)):
        num_activities = len(data_for_activity_count[category])
        num_activities_in_cats.append(num_activities)

    class_high_achievements = []
    class_consistency = []
    for student in range(0, len(data_to_analyze)):
        student_id = f"{student_list[student][1]}, {student_list[student][0]} ({student_list[student][2]})"
        student_high_achievements = []
        student_consistency = []
        for category in range(0, len(data_to_analyze[student])):

            category_frequencies = frequency_requirements[category]
            category_dictionary = data_to_analyze[student][category]
            performance_data = analyze_achievement_dictionary(dictionary=category_dictionary,
                                                              category_frequency=category_frequencies,
                                                              activity_count=num_activities_in_cats[category])
            high_achievement = performance_data["High Achievement"]
            consistency = performance_data["Consistency"]

            student_high_achievements.append(high_achievement)
            student_consistency.append(consistency)
        print(f"\t\t\t\t{student_id}: Highest >>> {student_high_achievements}")
        print(f"\t\t\t\t{student_id}: Consistency >>> {student_consistency}")
        class_high_achievements.append(student_high_achievements)
        class_consistency.append(student_consistency)
    return {"High Achievements": class_high_achievements, "Consistency": class_consistency}


def analyze_achievement_dictionary(dictionary, category_frequency, activity_count):

    achievement_dict = {"INC": 0, "BG": 0.25, "RT": 0.5, "B": 1, "D": 2, "P": 3, "C": 4, "E": 5}
    # BG = big gaps in learning that are caused by both absenteeism,
    # incomplete work, work that does not meet expectations
    counter = 4

    threshold = 0.5
    percent_incomplete = round(dictionary["INC"] / activity_count, 2)

    if percent_incomplete > threshold:
        consistent = False
    else:
        consistent = True

    # if percent_incomplete >= threshold:
    #     return achievement_dict["INC"]
    # percent_retry = round(dictionary["RT"] / activity_count, 2)
    # if percent_retry >= threshold:
    #     return achievement_dict["RT"]
    # percent_combined = round((dictionary["INC"]+dictionary["RT"]) / activity_count, 2)
    # if percent_combined >= threshold:
    #     return achievement_dict["BG"]

    high_achievement = 0
    achievement_determined = False
    for key in reversed(dictionary):
        # if str(key).upper() == "RT" or str(key).upper() == "INC":
        #     pass
        # else:
        if dictionary[key] >= category_frequency[counter]:
            high_achievement = achievement_dict[key]
            achievement_determined = True
        elif dictionary[key] > 0:
            progress_adjustment = 1 - round(achievement_dict[key] / category_frequency[counter], 2)
            high_achievement = achievement_dict[key] - progress_adjustment
            achievement_determined = True
        if achievement_determined is True:
            return {"High Achievement": high_achievement, "Consistency": consistent}
        counter -= 1
    return 404


def achievement_category_status(student_data, targets, student_list):
    print(f"\t\t\tLearning Targets: {targets}")
    class_status = []
    count = 0
    for student in student_data:
        student_id = f"{student_list[count][1]}, {student_list[count][0]} ({student_list[count][2]})"
        student_status = []
        for category in range(0, len(student)):
            if student[category] == 0:
                status = "Insufficient Evidence"
            elif student[category] == 0.5:
                status = "Review Work"
            elif student[category] > targets[category]:
                status = "Exceeding Expectations"
            elif student[category] == targets[category]:
                status = "Meeting Expectations"
            elif student[category] < targets[category]:
                status = "Approaching Expectations"
            else:
                status = "!!!"
            student_status.append(status)
        print(f"\t\t\t\t{student_id} >>> {student_status}")
        class_status.append(student_status)
        count += 1
    return class_status
