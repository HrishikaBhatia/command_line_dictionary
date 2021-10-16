import json
import difflib
from difflib import get_close_matches
data = json.load(open("F:\khushi\python_course_udemy\data.json"))
def eng_dict(key):
    key = key.lower()
    if key in data.keys():
        return data[key]
    elif key.title() in data.keys():
        return data[key.title()]
    elif key.upper() in data.keys():
        return data[key.upper()]
    elif len(get_close_matches(key,data.keys(),cutoff = 0.8))!=0:
        actual_key = get_close_matches(key,data.keys(),cutoff = 0.8)[0]
        print(f"Did you mean '{actual_key}'?" \
               f"\nEnter 'Y' for yes" \
               f"\nEnter 'N' for no")
        choice = input("Y/N: ")
        if choice == "Y":
            return data[actual_key]
        elif choice == "N":
            return "Word not found"
        else:
            return "We didn't understand your query"
    else:
        return "Word not found"
enter_word = input("Enter the word: ")
output = eng_dict(enter_word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)