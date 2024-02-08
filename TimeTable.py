# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:13:16 2024

@author: La famille tong
"""
from PlanningDay import WorkDay

class WeekTimeTable:
    def __init__(self, days):
        self.days = days
    
    def get_free_time_during_week(self):
        free_time = 0
        for day in self.days:
            free_time += day.get_free_time_during_day()
        return free_time
    
    def show_free_time_during_week(self):
        week_free_time = self.get_free_time_during_week()
        print(f"Temps total sur la semaine : {week_free_time}h")
        
    def plan_work_session(self,projects,impact_total):
        free_time_intervals = {}
        for day in self.days:
            free_time_intervals[day.code] = day.get_free_time_interval()
            