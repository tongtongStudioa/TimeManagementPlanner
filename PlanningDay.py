# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:04:25 2024

@author: La famille tong
"""
from TimeInterval import TimeInterval
from Project_class import Project

class WorkDay:
    def __init__(self, day_code, busy_time_intervals):
        self.code = day_code
        self.busy_intervals = busy_time_intervals
        self.busy_intervals.sort(key=lambda interval: interval.start)
        
    def __str__(self):
        string = f"Planning de la journée {self.code}:\n"
        planning_intervals = self.busy_intervals + self.get_free_time_interval()
        planning_intervals.sort(key=lambda interval: interval.start)
        for interval in planning_intervals:
            string +=  str(interval) + "\n"
        return string
    
    def get_free_time_interval(self):
        """Retourne les intervalles libres pour le jour spécifié.
            @return listes d'intervalles (TimeInterval)"""
        free_intervals = []
    
        # Ajouter un point de départ pour le premier intervalle libre
        start_free_time = 7
        end_time = 22
        
        #Ajouter les suivants par successions
        for busy_interval in self.busy_intervals:
            free_interval = TimeInterval("Temps libre",start_free_time, busy_interval.start)
            if (free_interval.total_time() > 0):
                free_intervals.append(free_interval)
            start_free_time = busy_interval.end
        
        # Ajouter le dernier interval du jour
        free_intervals.append(TimeInterval("Temps libre",self.busy_intervals[-1].end, end_time))
            
        return free_intervals
    
    def show_only_free_time_intervals(self):
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
    
    def add_work_session(self, projects, total_importance, time_available):
        return "test"
        
    def plan_day(self,projects,total_importance):
        free_intervals = self.get_free_time_interval()
        for interval in free_intervals:
            for project in projects:
                project_time = project.impact*interval.total_time()/total_importance
                if project_time > 1/6:
                    self.add_work_session()
            
            
            
            
            
            
            
            
            
            
            