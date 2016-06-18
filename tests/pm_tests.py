#!/usr/bin/env python

"""
The Program Manager (PM) tool test suite.

"""

from nose.tools import *
import pm
from datamodel import Person
from datamodel import Task
from datamodel import TaskList

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
