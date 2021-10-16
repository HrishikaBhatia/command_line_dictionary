import mysql.connector
import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
query1 = cursor.execute("SELECT * FROM Dictionary")
results1 = cursor.fetchall()
lst_of_exp = []
for item1 in results1:
    lst_of_exp.append(item1[0])

def get_def(exp):
    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{exp}'")
    results = cursor.fetchall()
    if results:
        return results
    else:
        exp = exp.lower()
        if len(get_close_matches(exp,lst_of_exp,cutoff = 0.8))!=0:
            actual_exp = (get_close_matches(exp,lst_of_exp,cutoff = 0.8))[0]
            choice = input(f"Did you mean '{actual_exp}'?\n"
                           f"Enter 'Y' for yes\n"
                           f"Enter 'N' for no: ")
            if choice == "Y":
                query2 = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{actual_exp}'")
                results2 = cursor.fetchall()
                return results2
            elif choice == "N":
                return "Word not found"
            else:
                return "We didn't understand your choice"
        else:
            return "Word not found"

word = input("Enter the expression: ")
output = get_def(word)
if type(output) == list:
    for item in output:
        print(item[1])
else:
    print(output)
