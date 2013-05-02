
def h24h12(h24):
    if h24 < 13 or h24 > 25:
        return 'ERROR: You did not put in a proper 24-hour PM time. Try again.'
    else:
        output = h24 - 12
    return output
    
def ib2kg(ib):
    #pounds to kilograms
    return ib * 0.453592
    
def kg2ib(kg):
    #kilograms to pounds
    return kg * 2.20462
    
def l2ml(l):
    #liters to mililiters
    return l * 0.001
    
def ml2l(ml):
    #militers to liters
    return ml * 1000
    
def h12h24(h12):
    if h12 < 1 or h12 > 12:
        return 'ERROR: You did not put in a proper 12-hour time. Try again.'
    else:
        output = h12 + 12
        return output
