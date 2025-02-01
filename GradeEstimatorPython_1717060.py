# Define initial names
first_name = {"Licurgo"}
last_name = {"Teixeira"}

# Display the formatted name with a greeting
print(f"Hello {last_name}, {first_name}")

# Variables for the points in Unit 1 activities
Unit1_discussion_points = 50  # Points earned in the discussion
Unit1_course_project_points = 50  # Points earned in the course project
Unit1_core_assessment_points = 40  # Points earned in the core assessment
task_maximum_points = 50  # Maximum points for each task

# Calculate the total points earned
total_points = (
    Unit1_discussion_points +
    Unit1_course_project_points +
    Unit1_core_assessment_points
)

# Display the total points
print(f"Total Points: {total_points}")

# Calculate the average points for Unit 1 activities
average_points = total_points / 3

# Display the average points
print(f"Average Points for Unit 1: {average_points}")

# Check and display if the maximum points were achieved for each task
print(f"Got maximum points for Unit 1 discussion? {Unit1_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 course project? {Unit1_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 core assessment? {Unit1_core_assessment_points == task_maximum_points}")

# Creating Dictionary with Unit Grades
unit_grades = {
    "Unit1": {
        "discussion_points": 50,
        "course_project_points": 40,
        "assignment_points": 50,
        },
    "Unit2": {
        "discussion_points": 50,
        "course_project_points": 50,
        "assignment_points": 00,
        },
    "Unit3": {
        "discussion_points": 50,
        "course_project_points": 50,
        "assignment_points": 50,
        },
}

task_maximum_points = 50  # Maximum points for each task

# Calculate the total points earned for each unit
def calculate_unit_scores(unit):
    if unit in unit_grades:
        discussion = unit_grades[unit]["discussion_points"]
        project = unit_grades[unit]["course_project_points"]
        assignment = unit_grades[unit].get("assignment_points", 00)  # Default to 00 if not present
        
        total_points = discussion + project + assignment
        average_points = total_points / 3
        
        print(f"{unit} Total Points: {total_points}")
        print(f"{unit} Average Points: {average_points:.2f}")
        
        print(f"Got maximum points for {unit} discussion? {discussion == task_maximum_points}")
        print(f"Got maximum points for {unit} course project? {project == task_maximum_points}")
        print(f"Got maximum points for {unit} assignment? {assignment == task_maximum_points}")
    else:
        print(f"{unit} not found in records.")

# Example queries
calculate_unit_scores("Unit1")
calculate_unit_scores("Unit2")
calculate_unit_scores("Unit3")

# Dictionary storing points for each category and unit
grades = {
    "Discussion": {"Unit1": 50, "Unit2": 50, "Unit3": 50},  
    "Course Project": {"Unit1": 40, "Unit2": 50, "Unit3": 50},  
    "Assignment": {"Unit1": 50, "Unit2": 00, "Unit3": 50}  
}

# Function to calculate total and average points for a given category
def get_total_points_by_category(category):
    if category in grades:
        total_points = sum(grades[category].values())  # Sum points for all units
        num_units = len(grades[category])  # Count number of units
        average_points = total_points / num_units  # Calculate average
        print(f"Total Points for {category}: {total_points}")
        print(f"Average Points for {category}: {average_points:.2f}")
    else:
        print(f"Category '{category}' not found.")

# Example Queries - Getting Points Information
get_total_points_by_category("Discussion")
get_total_points_by_category("Course Project")
get_total_points_by_category("Assignment")

# Checking if maximum points were achieved for each category
for category, units in grades.items():
    for unit, points in units.items():
        max_reached = points == task_maximum_points
        print(f"Got maximum points for {category} in {unit}? {max_reached}")

