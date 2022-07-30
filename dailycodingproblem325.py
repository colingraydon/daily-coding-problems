#The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

#Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.

#So the problem only prompted for distance units, so I created a simple program to deal with only distance. If we were dealign with all data types, I would make an abstract class for these methods (calculating conversion and adding a new unit)
#then create subclasses for other units, such as mass, time, mole, current, temp, lum, and mass. 

d = {"Inches": 1, "Feet" : 12, "Yards" : 36, "Chains": 792}

def calculate_conversion(unit_name, n):
    
    conversion_ratio = d[unit_name]
    print(n, " ", unit_name, "is equivalent to the following units.")
    for k in d:
        print((n * conversion_ratio) / d[k], " " , k)

#this line takes a new unit type, with its ratio to any other unit, and adds it into the dict
def add_unit(new_unit_name, ratio_to_other_unit, other_unit):

    d[new_unit_name] = ratio_to_other_unit * d[other_unit]



add_unit("Miles", 5280, "Feet")

for k in d:
    print(k, d[k])

calculate_conversion("Feet", 5280)