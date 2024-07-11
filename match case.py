#Match Case

def match_case(case):
    match case:
        case 100:
            return "OK"
        case 200:
            return "NICE"
        case 300:
            return "MID"
        case 400:
            return "POOR"
        case _:
            return "UNKNOWN"
        
x = int(input("Enter a case from 100-400: "))
print(match_case(x))