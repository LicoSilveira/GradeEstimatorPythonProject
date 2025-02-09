first_name = 'Licurgo'
last_name = 'Teixeira'

# Ask for the user's first name
first_name = input("Licurgo").strip()

# Ask for the user's last name
last_name = input("Teixeira").strip()

# Print the full name
print(f"Hello {last_name}, {first_name}")

# Explanatory comments
# 1. Asking the user to enter their first name and storing it in the variable first_name.
# 2. Asking the user to enter their last name and storing it in the variable last_name.
# 3. Printing the full name using an f-string to format the output.

# Format and display the full name with greeting
# Capitalizes the first letter of each name, ensures the rest is in lowercase, and displays in "Last, First" format with a greeting.
formatted_first_name = Licurgo.capitalize()
formatted_last_name = Teixeira.capitalize()
print(f"Hello {formatted_last_name}, {formatted_first_name}")

# Add variables for Unit 1 task points
# Assign the points you have earned for Unit 1 activities.
Unit1_discussion_points = 50  # Replace with your actual score if not the full 50
Unit1_course_project_points = 50  # Replace with your actual score
Unit1_core_assessment_points = 50  # Replace with your actual score
task_maximum_points = 50  # Maximum points possible for any task

# Calculate and display the total points for Unit 1
# Sums up all the points from Unit 1 activities and displays the total.
total_points = (Unit1_discussion_points +
                Unit1_course_project_points +
                Unit1_core_assessment_points)
print(f"Total Points: {total_points}")

# Check and display whether maximum points were achieved for each task
# Compares the points received for each task to the maximum points possible.
print(f"Got maximum points for Unit 1 discussion? {Unit1_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 course project? {Unit1_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 core assessment? {Unit1_core_assessment_points == task_maximum_points}")