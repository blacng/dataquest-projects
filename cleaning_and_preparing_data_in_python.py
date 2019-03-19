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