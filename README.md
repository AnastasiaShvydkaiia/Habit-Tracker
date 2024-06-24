
# Habit Tracker
A habit tracker is an essential tool thet helps you achieving your personal goals. With a habit tracker, you can create habits, complete them and analyze them.
## About the project
This project aims to simplify the process of developing habits by offering a convenient tool for tracking habits and gaining insights into them.

This project is built using Python 3.11.9. and is based on the concept of functions and classes.
## Installation
Clone the Github repo and run the following command to initialize it
```
git init
```
Create a virtual environment and install requirements (packages) using the following command

```
pip install -r requirements.txt
```
Requirements (packages):
- Questionary is a Python library for effortlessly building pretty command line interfaces
## Usage
- To start, run the folowing command
```
python main.py
```
- Create a habit

    To create a habit, select option "Add Habit". Enter the name of the habit you want to create and select periodicity either weekly or daily. If successful, you will see the message "Habit created successfully!". If you have already created this habit, you will see the message "This habit already exists". 
- Delete a habit

    To delete a habit, select option "Delete Habit". Select the habit you want to delete and then confirm your choice. if successful, you will see the "Habit deleted successfuly!" message.
- Check-off habit

    To mark your habit as completed, select "Check Off Habit" option. Then select a habit to check-off. If successful, you will see the message "Your habit is checked off". If you try to check-off the already completed habit you will see the message "You have already completed this habit". 

    Note: If you do not check off the habit within the defined period, the streak will be reset to one.
- Show all habits

    To see your habits, select "Show My Habits" option. Then select which periodicity of habits you want to see: daily, weekly or all. The program will display a table with your habits for this periodicity. If you have no such habits, you will see "no habits found" message.

- Show longest streak

    To see the longest streak of your habit, select "Show My Longest Streak" option. Then select the habit or all. The program will display a table with your habit's longest streak.
- Show tracker

    To see the current streak of your habits, select "Show Tracker" option. The program will display a table with your habit current streaks.

- Exit

    To exit the app, select "Exit" option.
## Tests
To run the tests, run the following command
```
python -m pytest
```