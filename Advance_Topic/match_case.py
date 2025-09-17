'''
    Match_Case
'''
def match_exp(choice):
    match choice:
        
        case 1:
            return "Sunday"
        
        case 2:
            return "Monday"
        
        case 3:
            return "Tuesday"
        
        case 4:
            return "Wednesday"
        case 4:
            return "Wednesday"  # Will not throw error for two same case
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        
        case _:
            return "Invalid Choice"

print(match_exp(choice:=int(input("Enter the valid choice: "))))