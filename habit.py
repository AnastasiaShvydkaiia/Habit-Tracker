import db
from datetime import datetime

class Habit:
    """
    Represents a habit.

    Attributes:
        habit_name (str):  the name of the habit, optional
        periodicity (str): the periodicity of the habit, optional
        db_name (str): name of the database where the habit is stored, optional
    """
    def __init__(self, habit_name=None, periodicity=None,db_name='main.db'):
        """Initializes a new instance of the Habit class"""
        self.habit_name=habit_name
        self.periodicity= periodicity
        self.start_time=datetime.now().strftime("%m/%d/%Y %H:%M")
        self.db=db.get_db(db_name)
    
    def create_habit(self):
        """Saves the habit to the database if one doesn't exist"""
        try:
            db.add_habit(self.db, self.habit_name, self.periodicity, self.start_time)
            print ('\nHabit created successfully!\n')
        except:
            print ('\nThis habit already exists\n')
        
    def remove_habit(self):
        """Deletes the habit from the database"""
        db.delete_habit(self.db, self.habit_name)  

    def check_off(self):
        """Marks habit as completed or resets its streak"""
        last_visit=db.last_visit(self.db,self.habit_name)
        today=datetime.strptime(self.start_time, "%m/%d/%Y %H:%M").date()
        gap=0
        if self.periodicity=='daily' and last_visit is not None:
            someday=datetime.strptime(last_visit, "%m/%d/%Y %H:%M").date()
            gap = (today - someday).days 
        elif self.periodicity=='weekly' and last_visit is not None:
            someday=datetime.strptime(last_visit, "%m/%d/%Y %H:%M").date()
            gap= (today - someday).days//7
        if gap == 0 and last_visit is not None:
            print("\nYou have already completed this habit\n")
        elif gap == 1 or last_visit is None:
            db.add_event(self.db, self.habit_name, self.start_time) 
            print('\nYour habit is checked off\n')
        else:
            db.reset_streak(self.db,self.habit_name, self.start_time)
            print('\nStreak has been reset\n')
