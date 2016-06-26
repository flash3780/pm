#!/usr/bin/env python

"""
The Program Manager (PM) tool is a command line tool for managing tasks.

"""

from datamodel import Person
from datamodel import Task

def main():
    people=[]
    taskNames=['My first task',
               'My second task',
               'My third task',
               'My fourth task']

    tasks=[]
    for name in taskNames:
        tasks.append(Task(name))
    tasks[0].add_subtask(tasks[1])
    tasks[0].add_subtask(tasks[2])
    tasks[0].add_subtask(tasks[3])



    return(tasks,people)

if __name__ == "__main__":
    tasks, people = main()
