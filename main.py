import questionary 
from tabulate import tabulate 
from habit import Habit
import analytics

def cli():
    """CLI interface that allows users interact wuth the app"""
    
    print('\nSuccess is the sum of small efforts repeated day in and day out.') 
    print('                                                 -Robert Collier\n')

    stop=False
    while not stop:

        choice = questionary.select("MENU",
            choices=["Add Habit", "Delete Habit", "Show My Habits","Check Off Habit","Show My Longest Streak","Show Tracker","Exit"]).ask()
            
        # add habit
        if choice == "Add Habit":
            habit_name = questionary.text('Enter habit name to create: ').ask()
            second_choice = questionary.select("Choose periodicity",choices=["daily", "weekly"]).ask()
            if second_choice == "daily":
                habit_periodicity="daily"
            if second_choice == "weekly":
                habit_periodicity="weekly"
            habit = Habit(habit_name, habit_periodicity)
            habit.create_habit() 

        # delete habit
        elif choice == "Delete Habit":
            list_of_habits= [i[0] for i in analytics.show_all_habits()]
            if  len(list_of_habits)==0:
                print('\nNo habits found\n')
            else:
                habit_name= questionary.select("Select habit to delete",choices=(list_of_habits)).ask()
                habit = Habit(habit_name)
                confirmation= questionary.confirm("Are you sure you want to delete habit '{habit.name}?",).ask()
                if confirmation:
                    habit.remove_habit()
                    print('\nHabit deleted successfuly!\n')
                else:
                    print('\nHabit was not deleted\n')

        # show habits
        elif choice == "Show My Habits":
            second_choice = questionary.select("Choose periodicity",choices=["daily", "weekly","all"]).ask()
            if second_choice == "all":
                list_of_habits = analytics.show_all_habits()
                if len(list_of_habits)==0:
                    print('\nNo habits found\n')
                else:
                    print(tabulate(analytics.show_all_habits(), headers=['habit name','periodicity','start time'], tablefmt="pretty"))
            if second_choice == "daily":
                list_of_habits = analytics.show_all_habits('daily')
                if len(list_of_habits)==0:
                    print('\nNo daily habits found\n')
                else:
                    print(tabulate(analytics.show_all_habits('daily'), headers=['habit name','periodicity','start time'], tablefmt="pretty"))
            if second_choice == "weekly":
                list_of_habits = analytics.show_all_habits('weekly')
                if len(list_of_habits)==0:
                    print('\nNo weekly habits found\n')
                else:
                    print(tabulate(analytics.show_all_habits('weekly'), headers=['habit name','periodicity','start time'], tablefmt="pretty"))
        
        #check off
        elif choice == "Check Off Habit":
            list_of_habits= [i[0] for i in analytics.show_all_habits()]
            
            if  len(list_of_habits)==0:
                print('\nNo habits found\n')
            else:
                habit_name= questionary.select("Select habit",choices=(list_of_habits)).ask()
                periodicity=[i[1] for i in analytics.show_all_habits() if i[0]==habit_name]
                habit = Habit(habit_name,periodicity[0])
                habit.check_off()
                    
        # show longest streak        
        elif choice == "Show My Longest Streak":
            list_of_habits = [i[0] for i in analytics.current_streak()]
            if len(list_of_habits)==0:
                print('\nNo tracked habits found\n')
            else:
                list_of_habits.append("all")
                habit_name = questionary.select("Select habit", choices=(list_of_habits)).ask()
                if habit_name=="all":
                    print(tabulate(analytics.max_streak(), headers=['habit name','longest streak'], tablefmt="pretty"))
                else:
                    print(tabulate(analytics.max_streak(habit_name), headers=['habit name','longest streak'], tablefmt="pretty"))

        # show tracker
        if choice=="Show Tracker":
            list_of_habits = [i[0] for i in analytics.current_streak()]
            if len(list_of_habits)==0:
                print('\nNo tracked habits found\n')
            else:
                print(tabulate(analytics.current_streak(), headers=['habit name','last check-off','current_streak'], tablefmt="pretty"))
        
        # exit
        elif choice == "Exit":
            print('Bye!')
            stop=True

if __name__ == "__main__":
    cli()