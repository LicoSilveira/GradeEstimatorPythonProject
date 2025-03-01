# Define student name
first_name = "Licurgo"
last_name = "Teixeira"

# Display the formatted name with a greeting
print(f"Hello {last_name}, {first_name}")

#Points earned for unit 1 discussion
Unit1_discussion_points = 50 #full points for unit 1 discussion

#Points earned for unit 1 course project
Unit1_course_project_points = 40 #full points for unit 1 discussion

#Points earned for unit 1 core assessment
Unit1_core_assessment_points = 50 #full points for unit 1 discussion

#Maximum points for each task
task_maximum_points = 50

#Calculate total points for unit 1
total_points_unit1 = (Unit1_discussion_points + 
                      Unit1_course_project_points + 
                      Unit1_core_assessment_points)

#Display total points for unit 1
print(f"Unit 1 Total Points: {total_points_unit1}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 1 discussion? {Unit1_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 course project? {Unit1_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 1 core assessment? {Unit1_core_assessment_points == task_maximum_points}")

#Unit 2 points earned
Unit2_discussion_points = 50 #full points for unit 2 discussion
Unit2_course_project_points = 50 #full points for unit 2 course project
Unit2_core_assessment_points = 0 #full points for unit 2 core assessment

#Calculate total points for unit 2
total_points_unit2 = (Unit2_discussion_points + 
                      Unit2_course_project_points + 
                      Unit2_core_assessment_points)

#Display total points for unit 2
print(f"Unit 2 Total Points: {total_points_unit2}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 2 discussion? {Unit2_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 2 course project? {Unit2_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 2 core assessment? {Unit2_core_assessment_points == task_maximum_points}")

#Unit 3 points earned
Unit3_discussion_points = 50 #full points for unit 3 discussion
Unit3_course_project_points = 40 #full points for unit 3 course project
Unit3_core_assessment_points = 50 #full points for unit 3 core assessment

#Calculate total points for unit 3
total_points_unit3 = (Unit3_discussion_points + 
                      Unit3_course_project_points + 
                      Unit3_core_assessment_points)

#Display total points for unit 3
print(f"Unit 3 Total Points: {total_points_unit3}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 3 discussion? {Unit3_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 3 course project? {Unit3_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 3 core assessment? {Unit3_core_assessment_points == task_maximum_points}")

#Unit 4 points earned
Unit4_discussion_points = 50 #full points for unit 4 discussion
Unit4_course_project_points = 35 #full points for unit 4 course project
Unit4_core_assessment_points = 0 #full points for unit 4 core assessment

#Calculate total points for unit 4
total_points_unit4 = (Unit4_discussion_points + 
                      Unit4_course_project_points + 
                      Unit4_core_assessment_points)

#Display total points for unit 4
print(f"Unit 4 Total Points: {total_points_unit4}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 4 discussion? {Unit4_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 4 course project? {Unit4_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 4 core assessment? {Unit4_core_assessment_points == task_maximum_points}")

#Unit 5 points earned
Unit5_discussion_points = 50 #full points for unit 5 discussion
Unit5_course_project_points = 50 #full points for unit 5 course project
Unit5_core_assessment_points = 50 #full points for unit 5 core assessment

#Calculate total points for unit 5
total_points_unit5 = (Unit5_discussion_points + 
                      Unit5_course_project_points + 
                      Unit5_core_assessment_points)

#Display total points for unit 5
print(f"Unit 5 Total Points: {total_points_unit5}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 5 discussion? {Unit5_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 5 course project? {Unit5_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 5 core assessment? {Unit5_core_assessment_points == task_maximum_points}")

#Unit 6 points earned
Unit6_discussion_points = 50 #full points for unit 6 discussion
Unit6_course_project_points = 50 #full points for unit 6 course project
Unit6_core_assessment_points = 50 #full points for unit 6 core assessment

#Calculate total points for unit 6
total_points_unit6 = (Unit6_discussion_points + 
                      Unit6_course_project_points + 
                      Unit6_core_assessment_points)

#Display total points for unit 5
print(f"Unit 6 Total Points: {total_points_unit6}")

#Check if maximum points were achieved for each task
print(f"Got maximum points for Unit 6 discussion? {Unit6_discussion_points == task_maximum_points}")
print(f"Got maximum points for Unit 6 course project? {Unit6_course_project_points == task_maximum_points}")
print(f"Got maximum points for Unit 6 core assessment? {Unit6_core_assessment_points == task_maximum_points}")

#Lists to store points earned for each assignment
total_discussion_points = [Unit1_discussion_points, Unit2_discussion_points, Unit3_discussion_points, Unit4_discussion_points, Unit5_discussion_points, Unit6_discussion_points]
total_course_project_points = [Unit1_course_project_points, Unit2_course_project_points, Unit3_course_project_points, Unit4_course_project_points, Unit5_course_project_points, Unit6_course_project_points]
total_core_assessment_points = [Unit1_core_assessment_points, Unit3_core_assessment_points, Unit5_core_assessment_points]

#Class definitions for Assignments and Grades
class Discussion:
    maximum_points_per_task = 50
    tasks_per_course = 8
    display_name = "Discussion"

class CourseProject:
    maximum_points_per_task = 50
    tasks_per_course = 8
    display_name = "Course Project"

class CoreAssessment:
    maximum_points_per_task = 50
    tasks_per_course = 4
    display_name = "Core Assessment"

#Function to calculate if maximum points were achieved in all tasks
def check_maximum_points(points, max_points, category_name):
    if all(points == task_maximum_points for points in points if points > 0):
        print(f"Congrats! You got maximum points for ALL {category_name} so far!")
    else:
        print(f"Unfortunately, you did not get maximum points for ALL {category_name}.")
    print("-" * 40)

#Check if maximum points were achieved for each category
sum_discussion_points = sum(total_discussion_points)
sum_course_project_points = sum(total_course_project_points)
sum_core_assessment_points = sum(total_core_assessment_points)

#Calculate maximum possible points using class attributes
max_discussion_points = Discussion.maximum_points_per_task * Discussion.tasks_per_course
max_course_project_points = CourseProject.maximum_points_per_task * CourseProject.tasks_per_course
max_core_assessment_points = CoreAssessment.maximum_points_per_task * CoreAssessment.tasks_per_course

#Print total points for each category
print ("Currently you have {} points for discussions out of {} possible points".format(sum_discussion_points, max_discussion_points))
print ("Currently you have {} points for course projects out of {} possible points".format(sum_course_project_points, max_course_project_points))
print ("Currently you have {} points for core assessments out of {} possible points".format(sum_core_assessment_points, max_core_assessment_points))

#Check if maximum points were achieved for each category
check_maximum_points(total_discussion_points, task_maximum_points, Discussion.display_name)
check_maximum_points(total_course_project_points, task_maximum_points, CourseProject.display_name)
check_maximum_points(total_core_assessment_points, task_maximum_points, CoreAssessment.display_name)

import json  # Import JSON module to read the file

# Define the TaskType class
class TaskType:
    def __init__(self, name, display_name, num_tasks, max_points):
        """
        Constructor for the TaskType class.
        Initializes attributes with provided values.
        """
        self.name = name  # Internal task name
        self.display_name = display_name  # Display name of the task
        self.num_tasks = num_tasks  # Number of times the task occurs per semester
        self.max_points = max_points  # Maximum points per task

# Path to the JSON file containing task data
json_file_path = "assignments.json"

# Try to open and load the JSON file
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Load JSON data
        assignments_data = data.get("assignments", [])  # Extract the list of assignments
except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")  # Handle missing file
    assignments_data = []  # Set an empty list to avoid errors
except json.JSONDecodeError:
    print(f"Error: The file {json_file_path} contains invalid JSON.")  # Handle malformed JSON
    assignments_data = []

# List to store TaskType objects
task_types = []

# Ensure that the loaded data is a list before iterating
if isinstance(assignments_data, list):
    for assignment in assignments_data:
        if isinstance(assignment, dict):  # Check if each item is a dictionary
            # Create a TaskType object using values from the JSON
            task_type = TaskType(
                assignment.get("name", "Unknown"),  # Task name
                assignment.get("display_name", "Unknown"),  # Display name
                assignment.get("num_tasks", 0),  # Number of tasks per semester
                assignment.get("max_points", 0)  # Maximum points per task
            )
            # Add the object to the task_types list
            task_types.append(task_type)
else:
    print("Error: `assignments_data` is not a valid list.")  # Error message if JSON format is incorrect

# Calculate the total maximum points a student can earn
total_maximum_points = sum(task.num_tasks * task.max_points for task in task_types)

# Display the final result
print(f"Maximum grade you can get for this class is: {total_maximum_points}")

# Optionally, display details of each task
for task in task_types:
    print(f"Task: {task.display_name}, Max Points per Semester: {task.num_tasks * task.max_points}")

import requests  # Import the requests library to make HTTP requests
from datetime import datetime

# Step 1: Get the response from the API
response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
data = response.json()

# Step 2: Extract information
client_ip = data.get("client_ip", "N/A")
day_of_year = data["day_of_year"]
utc_datetime = data["utc_datetime"]

# Display information
print(f"Client IP: {client_ip}")
print(f"Day of Year: {day_of_year}")
print(f"UTC DateTime: {utc_datetime}")

# Step 3: Define the course start date
begin_course_day = datetime(2025, 1, 12).timetuple().tm_yday

# Step 4: Get the current date using the unixtime from the API
now_date = datetime.utcfromtimestamp(data["unixtime"])

# Step 5: Convert the current date to the day of the year
now_day = now_date.timetuple().tm_yday

# Step 6: Calculate the difference in days
days_passed = now_day - begin_course_day

# Step 7: Convert days into 7-day Units
units_completed = days_passed // 7  # Integer division

# Step 8: Display the number of completed units
total_units = 8  # the course has 8 units
print(f"You have completed {units_completed} Units of {total_units}.")

# Function to get the current world time using the World Time API
def get_world_time(timezone="Etc/UTC"):
    url = f"http://worldtimeapi.org/api/timezone/{timezone}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        return data.get("datetime", "Time not available")
    except requests.exceptions.RequestException as e:
        return f"Error fetching world time: {e}"

# Fetch and display the current UTC time
current_time = get_world_time()
print(f"Current UTC Time: {current_time}")

import pandas as pd

# First, let's recreate the grades.csv from the first document
# Create a dictionary with the grade data
grade_data = {
    'Week 1': [50, 40, 50],
    'Week 2': [50, 50, 0],
    'Week 3': [50, 40, 50],
    'Week 4': [50, 35, 0],
    'Week 5': [50, 50, 50],
    'Week 6': [50, -40, 0],
    'Week 7': [50, 100, 50],
    'Week 8': [50, 50, 0]
}

# Create index for the DataFrame
index = ['Discussion', 'Course Projects', 'Core Assessments']

# Create DataFrame from the data
df = pd.DataFrame(grade_data, index=index)

# Save to CSV file (this simulates what you did in Unit 7)
df.to_csv('grades.csv')

# Read the grades.csv file we just created
grades_df = pd.read_csv('grades.csv', index_col=0)  # index_col=0 uses first column as index

# Display contents of grades.csv
print("Complete contents of grades.csv:")
print(grades_df)
print("\n")

# Display all grades just for discussions
print("Discussion grades only:")
print(grades_df.loc['Discussion'])  # .loc accesses rows by label
print("\n")

# Display grades for Unit 1 (Week 1) only for all types of homework
print("Unit 1 (Week 1) grades for all assignment types:")
print(grades_df['Week 1'])  # Access column by label
print("\n")

# Read JSON data for max points (simulating Unit 5 task)
json_data = '''
{
    "assignments": [
        {
            "name": "Discussions",
            "display_name": "Group Discussions",
            "num_tasks": 8,
            "max_points": 50
        },
        {
            "name": "Course Projects",
            "display_name": "Course Project",
            "num_tasks": 8,
            "max_points": 50
        },
        {
            "name": "Core Assessments",
            "display_name": "Final Assessments",
            "num_tasks": 4,
            "max_points": 50
        }
    ]
}
'''
assignment_rules = json.loads(json_data)  # Parse JSON string to dictionary

# Create a dictionary of max points for each assignment type
max_points_dict = {assignment['name']: assignment['max_points'] 
                  for assignment in assignment_rules['assignments']}

# Clean the data
cleaned_df = grades_df.copy()  # Create a copy to preserve original data

# Replace grades < 0 with 0 and grades > max_points with max_points
for assignment_type in cleaned_df.index:
    max_score = max_points_dict.get(assignment_type.replace('Discussion', 'Discussions'), 50)  # Get max points from JSON
    # Apply conditions: if less than 0, set to 0; if more than max, set to max
    cleaned_df.loc[assignment_type] = cleaned_df.loc[assignment_type].apply(
        lambda x: 0 if x < 0 else (max_score if x > max_score else x)
    )

# Display cleaned data
print("Cleaned data (grades < 0 set to 0, grades > max set to max):")
print(cleaned_df)

