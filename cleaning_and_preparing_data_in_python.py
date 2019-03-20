# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Opening a file, convert to list, and separating out the header row

opened_file = open('artworks.csv')
from csv import reader
read_file = reader(opened_file)
moma = list(read_file)
moma_header = moma[0]
moma = moma[1:]

# Using str.replace() function in python

age1 = "I am thirty-one years old"
age2 = age1.replace("thirty-one", "thirty-two")

nationalities = ['(American)', '(Spanish)', '(French)']

for n in nationalities:
    clean_open = n.replace("(","")
    clean_both = clean_open.replace(")","")
    print(clean_open)

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    gender = row[5]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[2] = nationality
    row[5] = gender

# 5. String Capitalization

for row in moma:
    '''assigning the gender column to a variable'''
    gender = row[5]
    '''assigning the nationality column to a variable'''
    nationality = row[2]
    '''converting the gender to title case'''
    gender = gender.title()
    '''checking for empty string and updating with a string'''
    if gender == "":
        gender = "Gender Unknown/Other"
    row[5] = gender

    nationality = nationality.title()
    if nationality == "":
        nationality = "Nationality Unknown"
    row[2] = nationality


# 6. Errors During Data Cleaning

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    BeginDate = row[3]
    EndDate = row[4]

    BeginDate = clean_and_convert(BeginDate)
    EndDate = clean_and_convert(EndDate)

    row[3] = BeginDate
    row[4] = EndDate

# 7. Parsing Numbers from Complex Strings, Part One

bad_chars = ["(",")","c","C",".","s","'", " "]

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string

stripped_test_data = []

for string in test_data:
    string = strip_characters(string)
    stripped_test_data.append(string)
print(stripped_test_data)

# Output: ['1912', '1929', '1913-1923', '1951', '1994', '1934', '1915', '1995', '1912', '1988', '2002', '1957-1959', '1955', '1970', '1990-1999']

# 8. Parsing Numbers from Complex Strings, Part Two

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]       
        date = (int(date_one) + int(date_two)) / 2
        date = round(date)
    else:
        date = int(date)
    return date

processed_test_data = []

for d in stripped_test_data:
    date = process_date(d)
    processed_test_data.append(date)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date
