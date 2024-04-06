# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:26:36 2024

@author: La famille tong
"""

class Project:
    """\nUne classe qui définit un projet.\n
    name
        nom du projet
    impact
        importance du projet
    total_duration
        durée du projet en heures
    project_weeks
        étalement du projet voulue en semaine"""
    def __init__(self,name: str,impact: int,total_duration: float,project_weeks: int):
        self.name = name
        self.impact = impact
        self.total_duration = total_duration
        self.project_weeks = project_weeks
    
    def available_time(self,free_time: float, total_impact_projects: int):
        """\nRetourne le temps disponible en fonction de l'impact du projet par rapport au autres
        (arrondi au dixième dans la même unité que le temps disponible donnée)
        free_time
            interval de temps libre
        total_impact_projects
            importance total des projets (somme de toutes les importances)
        """
        if (total_impact_projects < 1):
            total_impact_projects = 1
        return round(float(self.impact * free_time / float(total_impact_projects)),1)
    
    def alocated_time(self, free_time: float, total_impact_projects: int):
        available_time = self.available_time(free_time, total_impact_projects)
        if (available_time >=  round(1.0/6,1) and available_time <= 3): # plus petit que 3h et plus grand que 10 minutes
            alocated_time = self.total_duration / (self.project_weeks * 5.) # calcul du temps à alloué par jour
            return round(alocated_time,1) 
        else: return 0