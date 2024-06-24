import sqlite3

def get_db(name='main.db'):
    """
    Establishes a database connection.

    Args:
        name (str): name of the database 

    Returns:
        db: database connection
    """
    db=sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    """Creates tables "habits" and "tracker" in the database"""
    cur=db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habits (
                habit_name TEXT PRIMARY KEY,
                periodicity TEXT,
                start_time TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker(
                habit_name TEXT,
                end_time TEXT,
                streak INT,
                FOREIGN KEY (habit_name) REFERENCES habits(habit_name))""")

    db.commit()

def add_habit(db, habit_name, periodicity, start_time):
    """
    Adds new entry in table 'habits' with the habits data.

    Args:
        db: database connection
        habit_name (str): name of the habit to add
        periodicity(str): periodicity of the habit
        start_time(str): time when the habit was created
    """
    cur=db.cursor()
    cur.execute("INSERT INTO habits VALUES (?,?,?)", (habit_name, periodicity, start_time)) 
    db.commit()

def add_event(db, habit_name, end_time):
    """
    Adds new entry in table 'tracker' with a time when the habit has been checked-off and increases habit's streak.

    Args:
        db: database connection
        habit_name (str): name of the habit to check-off
        end_time(str): time when the habit was checked-off
    """
    cur=db.cursor()
    cur.execute("SELECT streak FROM tracker WHERE habit_name= ? ORDER BY end_time DESC",(habit_name,))
    data=cur.fetchall()
    if data != []:
        streak=data[0][0]+1
        cur.execute("INSERT INTO tracker VALUES (?,?,?)",(habit_name,end_time,streak))
    else:
        streak=1
        cur.execute("INSERT INTO tracker VALUES (?,?,?)",(habit_name,end_time,streak))
    db.commit()

def delete_habit(db,habit_name):
    """
    Deletes the habit data from the database.

    Args:
        db: database connection
        habit_name (str): name of the habit to delete
    """
    cur=db.cursor()
    cur.execute("DELETE FROM habits WHERE habit_name=?",(habit_name,))
    cur.execute("DELETE FROM tracker WHERE habit_name=?",(habit_name,))
    db.commit()

def reset_streak(db, habit_name, end_time):
    """
    Adds new entry in table 'tracker' with a time when the habit has been checked-off and resets habit's streak to 1.

    Args:
        db: database connection
        habit_name (str): name of the habit to check-off
        end_time(str): time when the habit is checked-off
    """
    cur=db.cursor()
    cur.execute("INSERT INTO tracker VALUES (?,?,?)",(habit_name, end_time,1))
    db.commit()

def last_visit(db, habit_name):
    """
    Gets the last date and time when the habit was checked-off.

    Args:
        habit_name (str): name of the habit, optional 
        db_name (str): name of the database, optional

    Returns:
        string: the last date and time when the habit was hecked-off.
    """
    cur=db.cursor()
    try:
        cur.execute("SELECT MAX(end_time) FROM tracker WHERE habit_name=?",(habit_name,))
        return cur.fetchall()[0][0]
    except:
        return None