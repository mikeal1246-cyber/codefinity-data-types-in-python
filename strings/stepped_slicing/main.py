filename = "Annual Budget Report 2024"

# 1. Split on spaces and take the last piece, which is the year
year = filename.split()[-1]       # "2024"

# 2. Take every second character (indexes 0 and 2)
year_code = year[::2]            # "22"

print("Variable sliced_string equals:", year_code)