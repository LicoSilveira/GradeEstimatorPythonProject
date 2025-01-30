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
