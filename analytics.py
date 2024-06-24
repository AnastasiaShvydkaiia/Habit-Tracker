from db import get_db

def show_all_habits(periodicity=None,db_name='main.db'):
    """
    Gets the list of either all habits or the habits with a particular periodicity.

    Args:
        periodicity (str): periodicity of the habit, optional 
        db_name (str): name of the database, optional

    Returns:
        list: list of either all habits or the habits with particular periodicity
    """
    db=get_db(db_name)
    cur=db.cursor()
    if periodicity is not None:
        cur.execute("SELECT * FROM habits WHERE periodicity=?",(periodicity,))
    else:
        cur.execute("SELECT * FROM habits ")
    return cur.fetchall() 

def max_streak(habit_name=None,db_name='main.db'):
    """
    Gets the 'tracker' table entry with maxinum streak count for either a particular habit or for all habits.

    Args:
        habit_name (str): name of the habit, optional 
        db_name (str): name of the database, optional

    Returns:
        list: 'tracker' table entry with maxinum streak count for either a particular habit or for all habits.
    """
    db=get_db(db_name)
    cur=db.cursor()
    if habit_name is not None:
        cur.execute("SELECT habit_name, MAX(streak) FROM tracker WHERE habit_name=?",(habit_name,))
    else:
        cur.execute("SELECT habit_name, MAX(streak) FROM tracker GROUP BY habit_name")
    return cur.fetchall() 

def current_streak(habit_name=None,db_name='main.db'):
    """
    Gets the 'tracker' table entry with current streak count for all habits.

    Args:
        db_name (str): name of the database, optional

    Returns:
        list: 'tracker' table entry with current streak count for all habits.
    """
    db=get_db(db_name)
    cur=db.cursor()
    if habit_name is not None:
        cur.execute("SELECT habit_name, MAX(end_time),streak FROM tracker WHERE habit_name=?",(habit_name,))
    else:
        cur.execute("SELECT habit_name, MAX(end_time),streak FROM tracker GROUP BY habit_name")
    return cur.fetchall() 

