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
busy_intervals1 = [TimeInterval(7,17),
                  TimeInterval(19,20)]

busy_intervals2 = [TimeInterval(7,13),
                  TimeInterval(15,16.5),
                  TimeInterval(18.5,20)]

day1 = WorkDay(1, busy_intervals1)
day2 = WorkDay(2, busy_intervals2)
day3 = WorkDay(3, busy_intervals1)
day4 = WorkDay(4, busy_intervals1)
day5 = WorkDay(5, busy_intervals1)

projects = [
    Project("Projet A", 3, 10), #timedelta(hours=2)
    Project("Projet B", 2, 25), #timedelta(hours=1)
    Project("Projet C", 1, 4) #timedelta(hours=3)
]

timetable = WeekTimeTable([day1, day2, day3, day4, day5])
free_time = timetable.show_free_time_during_week()
timetable.plan_work_session(projects,6)
#print(timedelta(hours=0.8))

