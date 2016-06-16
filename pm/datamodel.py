#!/usr/bin/env python

"""
Data model for the Program Manager tool. Contains two types:
    Task objects
    Person objects

"""

class Project(object):
    def __init__(self,name,deadline,**kwargs):
        self.name    = name
        self.mission = mission
        self.budget  = None
        self.deadline= 
        self.tasks   = []
    def add_task(self,name,owner):
        self.tasks.append(Task,name,owner)

class Task(object):

    def __init__(self,name,owner,*args,**kwargs):
        import binascii, os, pytz, random 
        import datetime as dt

        rightNow  = dt.datetime.utcnow().replace(tzinfo=pytz.utc)
        self.creationDate = (rightNow)
        self.taskID       = (binascii.b2a_hex(os.urandom(25)))
        self.name         = str(name)
        self.status       = 'open'
        self.owner        = None
        self.startDate    = None
        self.endDate      = None
        self.parentTasks  = [] 
        self.subTasks     = [] 

    def set_start(self,date):
        if not isinstance(date,datetime):
            raise typeError('A datetime object is expected.')
        self.startDate=date

    def set_end(self,date):
        if not isinstance(date,datetime):
            raise typeError('A datetime object is expected.')
        self.endDate=date

    def set_owner(self,owner):
        if not isinstance(owner,Person):
            raise typeError('A Person object is expected.')
        self.owner=owner

    def add_parent(self,parent):
        if not isinstance(parent,Task):
            raise typeError('Function expects a Task object')
        if parent not in self.parentTasks:
            self.parentTasks.append(parent)
            parent.add_subtask(self)
        
    def add_subtask(self,subtask):
        if not isinstance(subtask,Task):
            raise typeError('Function expects a Task object')
        if subtask not in self.subTasks:
            self.subTasks.append(subtask)
            subtask.add_parent(self)

    def percent_done(self):
        numberSubtasks = len(self.subTasks)
        subtaskPercent = []
        if numberSubtasks>0:
            for task in self.subTasks:
                print(task.name)
                print(task.status)
                print(task.percent_done())
                subtaskPercent.append(task.percent_done())
            percentDone = sum(subtaskPercent)/numberSubtasks
            if percentDone>=100:
                self.status = 'closed'
        else:
            if self.status == 'open':
                percentDone = 0.
            elif self.status == 'inprogress':
                percentDone = 50.
            elif self.status == 'closed':
                percentDone = 100.
            else:
                raise typeError('Unknown task status')
        return percentDone

class Person(object):
    def __init__(self,name):
        import pytz, random, os, binascii
        import datetime as dt

        rightNow  = dt.datetime.utcnow().replace(tzinfo=pytz.utc)
        self.CreationDate = (rightNow)
        self.ID       = (binascii.b2a_hex(os.urandom(25)))
        self.name     = name
