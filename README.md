# GradeEstimatorPythonProject
Repository for the python project

# Define student name
first_name = "Licurgo"
last_name = "Teixeira"

# Display the formatted name with a greeting
print(f"Hello {last_name}, {first_name}")

# Define the structure for storing scores using lists
units = ["Unit1", "Unit2", "Unit3", "Unit4"]
discussion_points = [50, 50, 50, 0]  # Unit 4 yet to be completed
course_project_points = [40, 50, 50, 0]
assignment_points = [50, 0, 50, 0]

# Maximum points for each category
task_maximum_points = 50
discussions_max = 400
course_projects_max = 400
assignments_max = 200

def display_unit_scores(unit_index):
    """Display total and average points for a given unit."""
    unit = units[unit_index]
    total = discussion_points[unit_index] + course_project_points[unit_index] + assignment_points[unit_index]
    average = total / 3  # Since each unit has 3 categories
    print(f"{unit} Total Points: {total}")
    print(f"{unit} Average Points: {average:.2f}")
    print(f"Got maximum points for {unit} discussion? {discussion_points[unit_index] == task_maximum_points}")
    print(f"Got maximum points for {unit} course project? {course_project_points[unit_index] == task_maximum_points}")
    print(f"Got maximum points for {unit} assignment? {assignment_points[unit_index] == task_maximum_points}")
    print("-" * 40)

# Display scores for each completed unit
for i in range(3):  # Unit 4 is not yet completed
    display_unit_scores(i)

# Function to calculate total and average points for each category
def get_total_points_by_category(category, points_list, max_points):
    total_points = sum(points_list)
    average_points = total_points / len(points_list)
    print(f"Total Points for {category}: {total_points} out of {max_points}")
    print(f"Average Points for {category}: {average_points:.2f}")
    print("-" * 40)

# Display category-based performance
get_total_points_by_category("Discussion", discussion_points, discussions_max)
get_total_points_by_category("Course Project", course_project_points, course_projects_max)
get_total_points_by_category("Assignment", assignment_points, assignments_max)

# Check if maximum points were achieved per category
def check_maximum_points(grades, category_name):
    if all(grade == task_maximum_points for grade in grades if grade > 0):
        print(f"Congrats! You got maximum points for ALL {category_name} so far!")
    else:
        print(f"Unfortunately, you did not get maximum points for ALL {category_name}.")
    print("-" * 40)

check_maximum_points(discussion_points, "Discussions")
check_maximum_points(course_project_points, "Course Projects")
check_maximum_points(assignment_points, "Assignments")

# Prepare Unit 4 for input (Placeholder for future updates)
print("Prepare to input scores for Unit 4!")
# End of the script so far
