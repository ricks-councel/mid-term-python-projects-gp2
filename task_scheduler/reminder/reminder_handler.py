import pandas as pd
import time
from datetime import datetime as dt
class RemindersHandler:
    def __init__(self, path):
        """[constractore]

        Args:
            path ([str]): [path to save reminders]
        """
        self.path = path
        self.next_reminder = {"time": None,"date":None, "message" : None}
        self.reminders = pd.read_csv(path)
        self.reminders['time'] = pd.to_datetime(self.reminders['time'], format="%Y-%m-%d %H:%M:%S")
        self.sort_reminders()
        self.update_next_reminder()
    def sort_reminders(self):
        """[sort reminder by time]
        """
        self.reminders.sort_values('time', inplace=True, ignore_index=True,  ascending=True)
    def add_reminder(self, time, message):
        """[add a new reminder with specific time]

        Args:
            time ([str]): [time of your reminder]
            message ([str]): [message of your reminder]
        """
        self.reminders = self.reminders.append({"time": dt.strptime(time, "%Y-%m-%d %H:%M:%S" ), "message": message}, ignore_index=True)
        self.sort_reminders()
        self.update_next_reminder()
    def update_next_reminder(self):
        """[update next reminder to display]
        """
        self.next_reminder['time'] = str(self.reminders.iloc[0]['time'].time())
        self.next_reminder['date'] = str(self.reminders.iloc[0]['time'].date())
        self.next_reminder['message'] = self.reminders.iloc[0]['message']
    def view_reminders(self):
        records = list(self.reminders.to_records(index = True))
        for index, time, message in records:
            t = pd.to_datetime(str(time))
            print(f"{index}. Time: {t.time()}\n   Date: {t.date()}\n   Message: {message}")
    
    def delete_reminder(self, index):
        self.reminders.drop(index, inplace=True)
        self.reminders.reset_index(drop=True, inplace=True)
        self.sort_reminders()
    def update_reminder(self, index, newtime, newmessage):
        """[update reminder time, date , and message]

        Args:
            index ([int]): [index of remider]
            newtime ([str]): [new time]
            newmessage ([str]): [new message]
        """
        self.reminders.iloc[index, self.reminders.columns.get_loc('time')] = dt.strptime(newtime, "%Y-%m-%d %H:%M:%S" )
        self.reminders.iloc[index, self.reminders.columns.get_loc('message')] = newmessage
        self.sort_reminders()
    def handle_delete(self):
        """[delete reminder]
        """
        print("Enter the index of the reminder you want to delete:")
        idx = input("➤➤➤   ")
        self.delete_reminder(int(idx))
        print("Reminder has been deleted successfully!") 
    def start(self):
        """[start with reminder]
        """
        time.sleep(0.5)
        print("Welcome to Reminders ⏰")
        while True:
            time.sleep(0.5)
            self.view_reminders()
            print("Options { u : update a reminder    d : delete a reminder    q : back to main   a : add new reminder }")
            pmt = input("➤➤➤   ")
            if pmt == 'q':
                return
            elif pmt == "d":
                self.handle_delete()
            else:
                print("Please enter a valid option.")