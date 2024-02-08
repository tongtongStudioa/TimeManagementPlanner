# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:26:36 2024

@author: La famille tong
"""

class Project:
    def __init__(self,name,impact,total_duration):
        self.name = name
        self.imppact = impact
        self.total_duration = total_duration
    
    def alocated_week_time(self,total_week_free_time, total_impact_project):
        return float(self.total_duration * total_week_free_time / total_impact_project)