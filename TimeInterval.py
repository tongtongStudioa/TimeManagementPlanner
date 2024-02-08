# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:07:40 2024

@author: La famille tong
"""
class TimeInterval:
    def __init__(self, start, end):
        self.start = start if start < end else end
        self.end = end if end > start else start
    
    def contains(self,hour):
        interval_range =list(range(self.start,self.end+1,1))
        return hour in interval_range
    
    def total_time(self):
        return abs(self.end - self.start)