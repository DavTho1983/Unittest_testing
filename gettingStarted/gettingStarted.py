import unittest
import datetime

class DatePattern:

    def __init__(self, year, month, day, weekday=0):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    def matches(self, date):
        return (self.yearMatches(date) and self.month(date) and self.weekdayMatches(date))

class FooTests(unittest.TestCase):

    # def testFoo(self):
    #     self.assertTrue(False)

    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.assertTrue(p.matches(d))

    def testMatchesFalse(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 29)
        self.assertFalse(p.matches(d))

    def testMatchesYearAsWildCard(self):
        p = DatePattern(0, 4, 10)
        d = datetime.date(2005, 4, 10)
        self.assertTrue(p.matches(d))

    def testMatchesYearAndMonthAsWildCards(self):
        p = DatePattern(0, 0, 1)
        d = datetime.date(2004, 10, 1)
        self.assertTrue(p.matches(d))

    def testMatchesWeekday(self):
        p = DatePattern(0, 0, 0, 2) #2 is a Wednesday
        d = datetime.date(2004, 9, 29)
        self.assertTrue(p.matches(d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
