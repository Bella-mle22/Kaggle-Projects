#Instructions
#Instead of assigning the value at index 5 to the year property directly, use a try except block that:
#Tries to cast the value at index 5 to an integer.
#If an exception is thrown, assign the value 0 to the year property instead.
#Create a method called get_year that returns the year value for that Suspension instance.
#Create a Suspension instance using the 23rd row, and assign to missing_year.
#Use the .get_year() method to assign the year of the missing_year suspension instance to twenty_third_year.

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2] 
        try:
            self.year = int(row[5])
        except Exception:
             self.year = 0
    def get_year(self):
        return(self.year)
                
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
