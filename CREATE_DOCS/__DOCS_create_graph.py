import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
# import matplotlib.ticker as ticker
import numpy as np
import statistics as stats

from __DOCS_settings import unpack_goal_array
# from __DOCS_settings import section_labels


def achievement_differential(maximum, minimum):
    differential_table = [[0, 0.00],
                          [1, 0.05],
                          [2, 0.10],
                          [3, 0.15],
                          [4, 0.20],
                          [5, 0.25]]
    d = maximum - minimum
    for i in range(0, len(differential_table)):
        if d <= differential_table[i][0]:
            return differential_table[i][1]
    return differential_table[5][1]


def set_bar_colours(consistency):
    colour = {"Consistent Colour": "#3103fc", "Inconsistent Colour": "#fc0303"}  # blue / red
    colour_set = []
    for item in consistency:
        if item is True:  # student is consistent in the category
            colour_set.append(colour["Consistent Colour"])
        else:  # student is inconsistent in the category
            colour_set.append(colour["Inconsistent Colour"])
    return colour_set


def create_graph(filter_type, targets, achievement, consistency, goal_labels, f_name, l_name, student_num, save_path):
    pass_threshold = 0.66
    level_three = 3

    file_name = f"{l_name}, {f_name} - {student_num}"

    if filter_type == "SC":
        unpacked_goals = unpack_goal_array(goals=goal_labels)
    else:
        unpacked_goals = goal_labels

    bar_colours = set_bar_colours(consistency=consistency)

    # make sure that all targets are set at or below level 3 (it is NOT an expectation
    #  that students must achieve higher than level 3 in Ontario, however, if for some reason
    #  it has not been possible to teach to hte level three standard, students should also not
    #  be expected to reach that standard (e.g. COVID recovery)

    adjusted_targets = []
    for t in range(0, len(targets)):
        if targets[t] > 3:
            adjusted_targets.append(3)
        else:
            adjusted_targets.append(targets[t])

    # the crux of this assessment and grade determination visualization is that students grades are determined
    #  in relation to how they have achieved in relation to each of the target goals for the course; if the student
    #  meets the target, the calibration is set to 1, if the student is approaching the target the calibration
    #  is <1, and if the student is exceeding the target, the calibration is >1; by taking the averages of these
    #  calibrations we begin to ascertain a better general idea of overall achievement than by merely averaging out
    #  individual task performance; the calibration value is determined by taking the student achievement and dividing
    #  it by the target; if the target has not been taught, the goal is dropped from the calibration,
    #  esp. for mid-terms
    success_calibration = []
    included_targets = []
    labels_to_include = []
    averages = []

    for index in range(0, len(adjusted_targets)):
        if adjusted_targets[index] != 0:
            labels_to_include.append(unpacked_goals[index])
            included_targets.append(adjusted_targets[index])
            success_calibration.append(round(achievement[index] / adjusted_targets[index], 2))
    calibration_data = np.array(success_calibration)
    averages.append(round(stats.mode(calibration_data), 2))
    averages.append(round(stats.mean(calibration_data), 2))
    averages.append(round(stats.median(calibration_data), 2))

    # this code determines the achievement zone by looking at the variance of the highest goal achievement
    #  and the lowest goal achievement; the greater the difference between the highest and lowest achievement
    #  the broader the potential zone of grade determination is (i.e. the less accurate the data is in being able to
    #  determine the final grade - greater emphasis is placed on overall achievement throughout the semester
    #  and additional conversations with students should be occurring
    differential = achievement_differential(np.max(achievement), np.min(achievement))
    max_variance = round(np.max(averages) * 3 + differential, 2)
    min_variance = round(np.min(averages) * 3 - differential, 2)

    print(f"\t\t{file_name}")
    print(f"\t\t\tMode / Mean / Median: {averages}")
    print(f"\t\t\tMax: {np.max(achievement)} \t Max Variance: {max_variance}")
    print(f"\t\t\tMin: {np.min(achievement)} \t Min Variance: {min_variance}")

    max_grade = round((np.max(achievement) + max_variance) / 2.2, 2)
    min_grade = round((np.min(achievement) + min_variance) / 1.8, 2)
    print(f"\t\t\tMax Grade = {max_grade} \t Min Grade = {min_grade}")
    print(f"\t\t\tConsistency:  {consistency}")
    print(f"\t\t\tBar Colours:  {bar_colours}")

    # Create Graph
    threshold_bar = []
    fail_zone = []
    target_bar = []
    min_line = []
    max_line = []
    achievement_zone = []

    # adjust arrays so that there is blank data at the beginning and end of the arrays in order to create threshold
    #  bars more accurately

    for i in range(0, len(included_targets)):
        # main included target array length is set
        # main achievement array length is set
        # labels to include array length is set
        threshold_bar.append(pass_threshold)
        fail_zone.append(pass_threshold / 2)
        target_bar.append(level_three)  # I am pretty sure I have done this using a zone tool
        min_line.append(min_grade)
        max_line.append(max_grade)
        achievement_zone.append((max_grade + min_grade / 2))  # I am pretty sure I have done this using a zone tool

    included_targets.insert(0, 0)
    achievement.insert(0, 0)
    labels_to_include.insert(0, "")
    threshold_bar.append(pass_threshold)
    min_line.append(min_grade)
    max_line.append(max_grade)
    achievement_zone.append((max_grade + min_grade / 2))  # I am pretty sure I have done this using a zone tool

    included_targets.append(0)
    achievement.append(0)
    labels_to_include.append("")
    threshold_bar.append(pass_threshold)
    min_line.append(min_grade)
    max_line.append(max_grade)
    achievement_zone.append((max_grade + min_grade / 2))  # I am pretty sure I have done this using a zone tool

    x = np.arange(len(labels_to_include))
    width = 0.35

    fig, ax = plt.subplots(layout="constrained")

    fig.set_size_inches(7.5, 7.5)

    y_labels = ["", "Beginning  ", "Developing  ", "Proficient  ", "Comprehensive  ", "Exemplary  ", ""]
    ax.set_yticklabels(y_labels, rotation=90)

    ax2 = ax.twinx()
    ax2.grid(which="major", axis="y", color="#FFFFFF", linewidth=0.01)
    ax2.yaxis.set_major_locator(MultipleLocator(1 / 15))
    y2_labels = ["",
                 "50%",
                 "53%", "56%", "59%",
                 "63%", "66%", "69%",
                 "73%", "76%", "79%",
                 "83%", "86%", "89%",
                 "93%", "96%", "100%",
                 ""]
    ax2.set_yticklabels(y2_labels)

    bg_alpha = 0.25
    ax.axhspan(4, 5, color="#3b83ff", alpha=bg_alpha)  # this creates the pass threshold zone in the graph
    ax.axhspan(3, 4, color="#8db2f2", alpha=bg_alpha)  # this creates the pass threshold zone in the graph
    ax.axhspan(2, 3, color="#3ea34d", alpha=bg_alpha)  # this creates the pass threshold zone in the graph
    ax.axhspan(1, 2, color="#ffa74f", alpha=bg_alpha)  # this creates the pass threshold zone in the graph
    ax.axhspan(0, 1, color="#fc97f6", alpha=bg_alpha)  # this creates the pass threshold zone in the graph

    # --- !!! CURRENTLY STUDENT ACHIEVEMENT ZONE IS DISABLED !!! ---
    # if differential < 0.15:
    #   ax.axhspan(min_grade, max_grade, color="WHITE", alpha=0.10)

    # target bars
    ax.bar(x - width / 2, included_targets, width, label="Learning Targets", color="grey")
    # achievement bars
    ax.bar(x + width / 2, achievement, width, label="Student Achievement", color=bar_colours)

    ax.set_title(f"Achievement Summary for {file_name}", weight="bold", fontsize=16)
    ax.set_xlabel("Course Success Criteria", weight="bold", fontsize=13)
    ax.set_ylabel("Learning Progression", weight="bold", fontsize=13)

    ax.set_xticks(x, labels_to_include, rotation=15)
    ax.set_ylim([0, 5.0])

    # plt.show()

    # goal_labels.pop(0)
    # goal_labels.pop()
    # adjusted_targets.pop(0)
    # adjusted_targets.pop()

    graph_file_path = f"{save_path}/{file_name}.png"
    plt.savefig(graph_file_path)
    plt.close()

    return graph_file_path
