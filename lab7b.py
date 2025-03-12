#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    seconds = t1.second + t2.second
    minutes = t1.minute + t2.minute + seconds // 60
    hours = t1.hour + t2.hour + minutes // 60
    return Time(hours % 24, minutes % 60, seconds % 60)

def change_time(t, seconds):
    """Change the time object by adding a number of seconds."""
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second + seconds
    t.hour = (total_seconds // 3600) % 24
    t.minute = (total_seconds % 3600) // 60
    t.second = total_seconds % 60
    return None