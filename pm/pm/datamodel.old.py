#!/usr/bin/env python

"""
Data model for the Program Manager tool. Contains two types:
    Task objects
    Person objects

"""

class TaskList(object):
    def __init__(self,*args):
        tasks=[]
        for arg in args:
            if isinstance(Task,arg):
                tasks.append(arg)



class Task(object):

    def __init__(self,name,owner,*args,**kwargs):
        import binascii, os, pytz, random 
        import datetime as dt

        assert str(name)

        rightNow  = dt.datetime.utcnow().replace(tzinfo=pytz.utc)
        self.creationDate = (rightNow)
        self.taskID       = (binascii.b2a_hex(os.urandom(25)))
        self.name         = name
        self.owner        = None
        self.startDate    = None
        self.endDate      = None
        self.parentTasks  = [] 
        self.subTasks     = [] 

    def set_start(self,date):
        self.startDate=date
    def set_end(self,date):
        self.endDate=date
    def set_owner(self,owner):
        try:
            assert isinstance(Person,owner)
            self.owner=owner
        except AttributeError as e:
            print(e)
    def add_parent(self,parent):
        if parent not in self.parentTasks:
            self.parentTasks.append(parent)
            try:
                assert isinstance(Task,parent)
                parent.add_subtask(self)
            except AttributeError as e:
                print(e)
        else:
            print('Already added.')
        
    def add_subtask(self,subtask):
        if subtask not in self.subTasks:
            self.subTasks.append(subtask)
            try:
                subtask.add_parent(self)
            except AttributeError as e:
                print(e)
        else:
            print('Already added.')

class Person(object):
    def __init__(self,name):
        import pytz, random, os, binascii
        import datetime as dt

        rightNow  = dt.datetime.utcnow().replace(tzinfo=pytz.utc)
        self.CreationDate = (rightNow)
        self.ID       = (binascii.b2a_hex(os.urandom(25)))
        self.name     = name
