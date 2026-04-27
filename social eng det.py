# phishing detector
import pandas as pd
from prettytable import PrettyTable

print("Hello! This is a beta social engineering message detector\n")

# Create table
table = PrettyTable(["Number", "Tactic", "Description"])

table.add_row(["1", "Urgency", "Creates pressure to act quickly (e.g., 'Act now!' or 'Your account will be locked')."])
table.add_row(["2", "Private Info Request", "Asks for sensitive data like passwords or credit card info."])
table.add_row(["3", "Phishing", "Mass emails pretending to be trusted brands."])
table.add_row(["4", "Pretexting", "Fake scenario (e.g., pretending to be IT support)."])
table.add_row(["5", "Baiting", "Offers something tempting (e.g., free download)."])
table.add_row(["6", "Scareware", "Fake warnings to scare users into action."])
table.add_row(["7", "Honey Trap", "Pretends to build a romantic/personal relationship."])
table.add_row(["8", "Quid Pro Quo", "Offers a service in exchange for credentials."])

print(table)

# User input
print("\nSelect the numbers that apply (comma separated). Example: 1,3,5")
choices = input("Your choices: ")

# Function to check message
def check_msg(choices):
    score = 0

    if "1" in choices:
        score += 1
    if "2" in choices:
        score += 1
    if "3" in choices:
        score += 1
    if "4" in choices:
        score += 1
    if "5" in choices:
        score += 1
    if "6" in choices:
        score += 1
    if "7" in choices:
        score += 1
    if "8" in choices:
        score += 1

    # Result logic
    if score >= 5:
        return "HIGH RISK: This is very likely a social engineering attack!"
    elif score >= 3:
        return "MEDIUM RISK: This might be a social engineering attempt. Be cautious."
    else:
        return "LOW RISK: This seems relatively safe, but stay alert."


result = check_msg(choices)
print("\nResult:", result)