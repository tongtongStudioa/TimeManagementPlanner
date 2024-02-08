# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:04:25 2024

@author: La famille tong
"""
from TimeInterval import TimeInterval

class WorkDay:
    def __init__(self, day_code, busy_time_intervals):
        self.code = day_code
        self.busy_intervals = busy_time_intervals
        self.busy_intervals.sort(key=lambda interval: interval.start)
        
        
    def get_free_time_interval(self):
        free_intervals = []
    
        # Ajouter un point de départ pour le premier intervalle libre
        start_free_time = 7
        end_time = 22
        
        #Ajouter les suivants par successions
        for busy_interval in self.busy_intervals:
            free_interval = TimeInterval(start_free_time, busy_interval.start)
            if (free_interval.total_time() > 0):
                free_intervals.append(free_interval)
            start_free_time = busy_interval.end
        
        # Ajouter le dernier interval du jour
        free_intervals.append(TimeInterval(self.busy_intervals[-1].end, end_time))
            
        return free_intervals
    
    def show_free_time_intervals(self):
        free_intervals = self.get_free_time_interval()
        # Affiche les temps libres
        print("Intervalles de temps libre :")
        for interval in free_intervals:
            print(f"Entre : {interval.start}h et {interval.end}h")
    
    def get_free_time_during_day(self):
        free_intervals = self.get_free_time_interval()
        total_free_time = 0
        for interval in free_intervals:
            total_free_time += interval.total_time()
        return total_free_time
    
    def show_free_time_during_day(self):
        total_free_time = self.get_free_time_during_day()
        print(f"Temps total de libre pour ce jour : {total_free_time}h")
    
    def add_work_session(self):
        self.busy_intervals.append()