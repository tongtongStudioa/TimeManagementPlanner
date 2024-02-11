# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:26:36 2024

@author: La famille tong
"""

class Project:
    def __init__(self,name,impact,total_duration):
        self.name = name
        self.impact = impact
        self.total_duration = total_duration
    
    def alocated_time(self,free_time, total_impact_project):
        """Retourne le temps alloué en fonction du temps disponible et de l'impact du projet par rapport au autres
        (arrondi au dixième dans la même unité que le temps disponible donnée)
        """
        if (total_impact_project < 1):
            total_impact_project = 1
        return round(float(self.impact * free_time / total_impact_project),1)