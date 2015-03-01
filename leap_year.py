def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
# Test
print leap_year(2003)
print leap_year(2004) # <--- Leap Year
print leap_year(2005)

# Use this code to determine if a year is a leap year.
