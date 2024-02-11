# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:17:13 2024

@author: La famille tong
"""
from datetime import timedelta
from PlanningDay import WorkDay
from TimeInterval import TimeInterval
from TimeTable import WeekTimeTable
from Project_class import Project
    
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
    Project("Faire les courses", 3, 1), #timedelta(hours=2)
    Project("Développement app", 2, 25), #timedelta(hours=1)
    Project("Lecture", 1, 4) #timedelta(hours=3)
]

timetable = WeekTimeTable([day1, day2, day3, day4, day5])
print(timetable)
timetable.plan_work_sessions(projects, 6)
print(timetable)
#print(timedelta(hours=0.8))

