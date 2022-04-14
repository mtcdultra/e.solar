from cmath import cos, sin
from datetime import datetime
import math

def day_of_year():

    month = int(input("Type number of the month: "))
    day = int(input("Type number of the day: "))
    year = 2010

    date_choosed = datetime.strptime( str(year) + "-" + str(month) + "-" + str(day), '%Y-%m-%d' )
    date_first = datetime.strptime('2010-01-01','%Y-%m-%d')

    result = (date_choosed - date_first).days + 1
    
    return result

def diary_angle_b(days_of_year):
    result = ( days_of_year - 1 ) * ( 360 / 365 )

    return result

def spencer_equation(pi_180degrees, b_variable):
    
    result = round( ( 0.006918 - 0.399912 * math.cos( b_variable * pi_180degrees ) + 0.070257 * math.sin ( b_variable * pi_180degrees ) - 0.006758 * math.cos ( 2 * b_variable * pi_180degrees ) + 0.000907 * math.sin ( 2 * b_variable * pi_180degrees ) - 0.002697 * math.cos( 3 * b_variable * pi_180degrees )+0.00148 * math.sin( 3 * b_variable * pi_180degrees ) ) * (180 / math.pi ) , 2 )  

    return result

def cooper_equation(b_variable, days_of_year):

    result = round( 23.45 * math.sin( 360 * ( ( 284 + days_of_year ) / 365 ) ), 2 )

    return result

# Default equation is Spencer (more precise) and the other is Cooper equation
def solar_declination(days_of_year, equation):

    pi_180degrees = math.pi / 180
    b_variable = diary_angle_b(days_of_year)

    if equation == "spencer":
        result =  spencer_equation(pi_180degrees, b_variable)
    else:
        result = cooper_equation(b_variable, days_of_year)

    return (f"The solar declination are { str(result) } degrees")