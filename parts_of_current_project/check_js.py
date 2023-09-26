# The code in this file is used to check if a string contains a variation of "/JavaScript" or "/JS".
# Which is part of the "final.py".

# import re

# # Define regular expression patterns for both variations
# js_pattern = re.compile(r'/[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*', re.IGNORECASE)
# javascript_pattern = re.compile(r'/(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t', re.IGNORECASE)

# # Get user input
# user_input = input("Enter your text: ")

# # Function to decode hex-encoded characters
# def decode_hex(match):
#     return chr(int(match.group(0)[1:], 16))

# # Decode the input before searching
# decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, user_input)

# # Search for both patterns in the decoded input
# js_match = js_pattern.search(decoded_input)
# javascript_match = javascript_pattern.search(decoded_input)

# # Check if the patterns were found
# if js_match:
#     print("The input contains a variation of '/JS'.")
# elif javascript_match:
#     print("The input contains a variation of '/JavaScript'.")
# else:
#     print("The input does not contain a variation of '/JS' or '/JavaScript'.")














# # # # # # ---------- Ten letter variations complete ---------- # # # # #
# import re

# # Define a regular expression pattern to match variations of "/JavaScript"
# pattern = re.compile(r'/(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t', re.IGNORECASE)

# # Get user input
# user_input = input("Enter your text: ")

# # Function to decode hex-encoded characters
# def decode_hex(match):
#     return chr(int(match.group(0)[1:], 16))

# # Decode the input before searching
# decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, user_input)

# # Search for the pattern in the decoded input
# match = pattern.search(decoded_input)

# # Check if the pattern was found
# if match:
#     print("The input contains a variation of '/JavaScript'.")
# else:
#     print("The input does not contain a variation of '/JavaScript'.")






# # # # # # ---------- Two letter variations complete ---------- # # # # #
# import re

# # Define a regular expression pattern to match variations of "/JS"
# pattern = re.compile(r'/[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*', re.IGNORECASE)

# # Get user input
# user_input = input("Enter your text: ")

# # Function to decode hex-encoded characters
# def decode_hex(match):
#     return chr(int(match.group(0)[1:], 16))

# # Decode the input before searching
# decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, user_input)

# # Search for the pattern in the decoded input
# match = pattern.search(decoded_input)

# # Check if the pattern was found
# if match:
#     print("The input contains a variation of '/JS'.")
# else:
#     print("The input does not contain a variation of '/JS'.")
