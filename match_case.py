# match Case Statements


# start with def
def check_value(value):
    match value:
        case 1: return "One"
        case 2: return "Two"
        case _: return "Other"
    
print(check_value(1))
print(check_value(6))