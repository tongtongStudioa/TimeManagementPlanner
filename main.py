# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:17:13 2024

@author: axel
"""
from datetime import timedelta
from PlanningDay import WorkDay
from TimeInterval import TimeInterval
from TimeTable import WeekTimeTable
from Project_class import Project
from tkinter import *
from tkinter import ttk, messagebox

    
# Exemple d'utilisation
busy_intervals1 = [TimeInterval("Cours",7,17),
                  TimeInterval("Diner",19,20)]

busy_intervals2 = [TimeInterval("Cours",7,13),
                  TimeInterval("Cours",15,16.5),
                  TimeInterval("Sport",18.5,20)]

day1 = WorkDay(1, busy_intervals1)
day2 = WorkDay(2, busy_intervals2)
day3 = WorkDay(3, busy_intervals1)
day4 = WorkDay(4, busy_intervals1)
day5 = WorkDay(5, busy_intervals1)

projects = [
    Project("Faire les courses", 3, 1,1), #timedelta(hours=2)
    Project("Développement app", 2, 25,4), #timedelta(hours=1)
    Project("Lecture", 1, 4,4) #timedelta(hours=3)
]

timetable = WeekTimeTable([day1, day2, day3, day4, day5])
#print(timetable)
#timetable.plan_work_sessions(projects)
#print(timetable)
#print(timedelta(hours=0.8))


def on_item_click(event):
    item = treeview.selection()[0]
    values = treeview.item(item, "values")
    messagebox.showinfo("Event Information", f"Event: {values[0]}\nDate: {values[1]}\nTime: {values[2]}")

# Create the main application window
root = Tk()
root.title("Weekly Event Timetable")

# Adjust the size of the window
root.geometry("800x400")

frame = Frame(root, bg='lightblue')

# Create a Treeview widget
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_slots = ["08:00 AM", "08:30 AM", "09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
              "12:00 PM", "12:30 PM", "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM", "03:00 PM", "03:30 PM",
              "04:00 PM", "04:30 PM", "05:00 PM", "05:30 PM"]

columns = ["Time"] + days_of_week
treeview = ttk.Treeview(frame, columns=columns, show="headings", height=len(time_slots))

# Define column headings
treeview.heading("Time", text="Time")
for col in days_of_week:
    treeview.heading(col, text=col)

# Add time slots
for time_slot in time_slots:
    treeview.insert("", "end", values=[time_slot] + [""] * len(days_of_week))

# Add sample data (replace it with your own data)
data = [
    ("Event 1", "2024-03-15", "10:00 AM", "Monday"),
    ("Event 2", "2024-03-16", "02:30 PM", "Wednesday"),
    # Add more events as needed
]

# Bind a click event to display event information
treeview.bind("<ButtonRelease-1>", on_item_click)

# Pack the frame
frame.pack()

# Pack the Treeview widget
treeview.pack()

# Run the application
root.mainloop()