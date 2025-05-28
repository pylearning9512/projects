#made this as an exercise to test out a regex concept learned from "automate the boring stuff"

import re

#regex to define the phone  number strugcture
#"\d" is a digit, 
# "{3}" and "{4}" is the number of digits in a row
#""
phone_num_regex = r'\d{3}-\d{3}-\d{4}'
mo= re.compile(phone_num_regex)

#example strings to search through
strings= [
    "Please call our customer service at 555-123-4567 for assistance.",
    "John's mobile is 999-888-7777 and his office number is 555-999-0000.",
    "Contact Sarah at sarah@email.com or 333-444-5555 if you need help.",
    "The restaurant reservation line is 888-FOOD-NOW or 888-366-3669.",
    "Emergency contact: Mom 777-555-1234, Dad 777-555-5678",
    "This text has no phone numbers in it at all.",
    "For technical support, dial 1-800-555-TECH (1-800-555-8324) anytime.",
    "Dr. Smith's office: 555-DOC-HELP, alternative: 555-362-4357",
    "Meeting room booking: 666-777-8888 ext. 1234",
    "Jane called from 444-333-2222 yesterday about the project.",
    "The old number 123-456-7890 is no longer in service.",
    "Text message alerts sent to 555-TEXT-ME (555-839-8631)",
    "Call back number: 222-333-4444 - available 9am to 5pm",
    "Home: 777-888-9999, Work: 777-111-2222, Cell: 777-444-3333",
    "No contact info here, just some random text about weather.",
    "Pizza delivery: 555-HOT-PIZZA or you can try 555-468-7492",
    "Conference call dial-in: 888-123-4567, access code 98765#",
    "Lost and found department can be reached at 555-LOST-IT",
    "Schedule appointment: 999-CARE-NOW (999-227-3669) or online",
    "Just some text with numbers like 12345 but no phone format."]

#list to store the matches
all_matches= []


for string in strings:
   matches=mo.findall(string)
   all_matches.extend(matches)

for i in all_matches:
   print(f'phone number found: {i}')