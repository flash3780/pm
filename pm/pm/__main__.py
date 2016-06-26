#!/usr/bin/env python

"""
The Program Manager (PM) tool is a command line tool for managing tasks.

"""

from datamodel import Person
from datamodel import Task
from datamodel import TaskList

def main():
    people=[]
    people.append(Person('Chris Hubley'))
    taskNames=['My first task',
               'My second task',
               'My third task',
               'My fourth task']

    tasks=[]
    tl = TaskList()
    for name in taskNames:
        tl.add_task(Task(name,people[0]))

    tl.tasks[0].add_subtask(tl.tasks[1])
    tl.tasks[0].add_subtask(tl.tasks[2])
    tl.tasks[0].add_subtask(tl.tasks[3])
    tl.tasks[1].status='closed'
    tl.tasks[2].status='inprogress'
    percentDone = tl.tasks[0].percent_done()
    print(percentDone)

    return(tasks,people)

if __name__ == "__main__":
    tasks, people = main()
