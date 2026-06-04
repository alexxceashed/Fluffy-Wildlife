#Application Program Interface (API) - a set of rules and protocols for building and interacting with software applications.
#It defines how different software components should interact with each other, allowing them to communicate and exchange
#data. APIs can be used to access web services, databases, and other software components, enabling developers to create applications 
#that can leverage existing functionality and data.

import requests as rq
import json
import sys as s
if len (s.argv) != 2: # Checks if the number of command-line arguments is not equal to 2 (the script name and one additional argument). 
    #If this condition is true, it means that the user has not provided the correct number of arguments.
    s.exit()
response = rq.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={s.argv[1]}")  #Acts as a client, sending a request to the iTunes API to search for a song 
# based on the term provided as a command-line argument.
o = response.json()
for result in o["results"]:
    print(result["trackName"]) #The response from the iTunes API is expected to be in JSON format, which is a common data interchange format.


#The response from the iTunes API is expected to be in JSON format, which is a common data interchange format.
# The .json() method is used to parse the JSON response and convert it into a Python dictionary, which can then be printed or manipulated as needed.

#json.dumps() - converts a Python object into a JSON string. This is useful for printing or storing the data in a format that 
# can be easily shared or transmitted.