#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

def test_months_with_30():

# Write a test function for the months with 30 days
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30

def test_month_with_28_or_29():
# Write a test function for the months with 28 or 29 days
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) == "28 or 29"

# Write a test function for months that are not capitalized properly
def lower_case_months():
    for item in MONTHS_WITH_28_or_29():
        assert days_in_month.lower()

    for item in MONTHS_WITH_30:
        assert days_in_month.lower()

    for item in MONTHS_WITH_31:
        assert days_in_month.lower()

# Hint: use the lower() string method
# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
def month_errors_value():

   try:
       days_in_month("some string")
   except ValueError:
       assert True

def month_errors_attribute():
    try:
        days_in_month(74)
    except AttributeError:
        assert True




# Hint: use data types other than strings as input

# try:
#    some function call:
#except SomeError:
#   We get here cause of exception
#  assert True or False