from db import get_db
from habit import Habit
import analytics
import pytest

@pytest.fixture
def db():
    """
    This fixture will connect to the test.db at the beginning and close the connection at the end of all tests.
    """
    db = get_db("test.db")
    cur = db.cursor()
    test_data = [("walk the dog", "05/01/2024 09:00", 1),
                ("walk the dog", "05/02/2024 09:00", 2),
                ("walk the dog", "05/03/2024 09:00", 3),
                ("walk the dog", "05/04/2024 09:00", 4),
                ("walk the dog", "05/05/2024 09:00", 5),
                ("walk the dog", "05/07/2024 09:00", 1),
                ("walk the dog", "05/08/2024 09:00", 2),
                ("walk the dog", "05/09/2024 09:00", 3),
                ("walk the dog", "05/10/2024 09:00", 4),
                ("walk the dog", "05/11/2024 09:00", 5),
                ("walk the dog", "05/12/2024 09:00", 6),
                ("walk the dog", "05/13/2024 09:00", 7),
                ("walk the dog", "05/14/2024 09:00", 8),
                ("walk the dog", "05/15/2024 09:00", 9),
                ("walk the dog", "05/16/2024 09:00", 10),
                ("walk the dog", "05/17/2024 09:00", 11),
                ("walk the dog", "05/18/2024 09:00", 12),
                ("walk the dog", "05/19/2024 09:00", 13),
                ("walk the dog", "05/20/2024 09:00", 14),
                ("walk the dog", "05/21/2024 09:00", 15),
                ("walk the dog", "05/24/2024 09:00", 1),
                ("walk the dog", "05/25/2024 09:00", 2),
                ("walk the dog", "05/26/2024 09:00", 3),
                ("walk the dog", "05/27/2024 09:00", 4),
                ("walk the dog", "05/28/2024 09:00", 5),
                ("walk the dog", "05/29/2024 09:00", 6),
                ("walk the dog", "05/30/2024 09:00", 7),
                ("walk the dog", "05/31/2024 09:00", 8),

                ("medicines", "05/02/2024 08:00", 1),
                ("medicines", "05/03/2024 08:00", 2),
                ("medicines", "05/07/2024 08:00", 1),
                ("medicines", "05/11/2024 08:00", 1),
                ("medicines", "05/12/2024 08:00", 2),
                ("medicines", "05/13/2024 08:00", 3),
                ("medicines", "05/25/2024 08:00", 1),
                ("medicines", "05/26/2024 08:00", 2),
                ("medicines", "05/27/2024 08:00", 3),
                ("medicines", "05/28/2024 08:00", 4),
                ("medicines", "05/30/2024 08:00", 1),
                ("medicines", "05/31/2024 08:00", 2),

                ("reading", "05/01/2024 08:00", 1),
                ("reading", "05/02/2024 08:00", 2),
                ("reading", "05/03/2024 08:00", 3),
                ("reading", "05/15/2024 08:00", 1),
                ("reading", "05/24/2024 08:00", 1),
                ("reading", "05/25/2024 08:00", 2),
                ("reading", "05/28/2024 08:00", 1),
                ("reading", "05/29/2024 08:00", 2),
                ("reading", "05/30/2024 08:00", 3),

                ("cleaning", "05/03/2024 10:00", 1),
                ("cleaning", "05/10/2024 10:00", 2),
                ("cleaning", "05/17/2024 10:00", 3),
                ("cleaning", "05/24/2024 10:00", 4),
                        
                ("gym", "05/05/2024 10:00", 1),
                ("gym", "05/12/2024 10:00", 2),
                ("gym", "05/26/2024 10:00", 1),
                ]
    cur.executemany("INSERT INTO tracker VALUES(?,?,?)", test_data)
    db.commit()
    yield db
    db.close()

def test_creation(db):
    """
    GIVEN a habit instance and a test database
    WHEN a new habit is created
    THEN check the habit successfully added to the database 
    """
    habit=Habit('skin care','daily','test.db')
    habit.create_habit()
    list_of_habits= [i[0] for i in analytics.show_all_habits('daily',"test.db")]
    assert 'skin care'  in list_of_habits

def test_check_off(db):
    """
    GIVEN a habit instance and a test database for testing
    WHEN a habit is checked-off 
    THEN check the habit is in database and the current streak is calculated correctly
    """
    habit=Habit('skin care',"daily",'test.db')
    habit.check_off()
    tracker= [i[0] for i in analytics.current_streak(db_name="test.db")]
    assert "skin care" in tracker
    current_streak=[i[2] for i in analytics.current_streak('skin care',"test.db")]
    assert current_streak[0]==1

def test_deletion(db):
    """
    GIVEN a habit instance and a test database for testing
    WHEN habit deletion requested
    THEN check the habit is not in the database
    """
    habit=Habit('skin care', 'daily','test.db')
    habit.remove_habit()
    list_of_habits= [i[0] for i in analytics.show_all_habits(db_name="test.db")]
    assert 'skin care' not in list_of_habits
    tracker= [i[0] for i in analytics.current_streak(db_name="test.db")]
    assert 'skin care' not in tracker

def test_reset_streak_daily(db):
    """
    GIVEN a daily habit instance and a test database for testing
    WHEN daily habit is cheked-off 
    THEN check the streak is reset
    """
    habit=Habit("medicines","daily",'test.db')
    habit.check_off()
    current_streak=[i[2] for i in analytics.current_streak("medicines","test.db")]
    assert current_streak[0]==1

def test_reset_streak_weekly(db):
    """
    GIVEN a weekly habit instance and a test database for testing
    WHEN weekly habit is checked-off
    THEN check the streak is reset
    """
    habit=Habit('cleaning',"weekly",'test.db')
    habit.check_off()
    current_streak=[i[2] for i in analytics.current_streak('cleaning',"test.db")]
    assert current_streak[0]==1

def test_longest_streak(db):
    """
    GIVEN a habit instance and a test database for testing
    WHEN the longest streak calculation requested
    THEN check the longest streak is calculated correctly
    """
    max_streak=analytics.max_streak("walk the dog", "test.db")
    assert max_streak[0][1]==15

def test_current_streak(db):
    """
    GIVEN a habit instance and a test database for testing
    WHEN the current streak calculation requested
    THEN check the current streak is calculated correctly
    """
    cur_streak=analytics.current_streak("reading", "test.db")
    assert cur_streak[0][2]==3

def test_longest_streak_per_periodicity(db):
    """
    GIVEN a habit instances and a test database for testing
    WHEN the longest streak calculation requested
    THEN check the longest streak is calculated correctly
    """
    daily_habits=['reading','walk the dog','medicines']
    max_streak=max([i[1] for i in analytics.max_streak(db_name= "test.db") if i[0] in daily_habits])
    assert max_streak==15
