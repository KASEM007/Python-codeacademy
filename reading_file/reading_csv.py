
*****

# Since our CSV’s first line identifies the third field in our CSV “ Email “, 

# we can use that as the key in each row of our DictReader.

# In the solution no key arguments are specified for DictReader:

# If you print out the original file:

with open('cool_csv.csv') as cool_csv_file:
  for line in cool_csv_file:
    print(line.strip())

# You will see:

Cool Name,Cool Birthday,Cool Fact  
Trevor Torres,03-09-08,Has never been out of the country.
Crystal Ellis,17-11-06,Published a small biography on a local legend.
... etc.
# That first line, Cool Name,Cool Birthday,Cool Fact , is the header line, 
# used by csv.DictReader to obtain the keys for its output dictionaries.

# So “Cool Fact” is actually the header or field name that we’re interested in, 
# and that is what is used in the solution:

  for row in cool_csv_dict:
    print(row['Cool Fact'])
Entirely optional below this line:

# You can further investigate what’s going on:

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  print(cool_csv_dict)

#Output:
# <csv.DictReader object at 0x7f941b527748>
# Hmm, not too useful. What’s inside that object?

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)  )
  for row in cool_csv_dict:
    print(row)

# Output:
OrderedDict([('Cool Name', 'Trevor Torres'), ('Cool Birthday', '03-09-08'), ('Cool Fact', 'Has never been out of the country.')])
OrderedDict([('Cool Name', 'Crystal Ellis'), ('Cool Birthday', '17-11-06'), ('Cool Fact', 'Published a small biography on a local legend.')])
... etc.
# Well! That’s a bit strange! We haven’t covered the OrderedDict type, 
# but if you look at it a bit, you will see that each entry is a list of tuples, 
# and that each tuple looks like a key:value pair from a conventional dictionary, 
# the final key being “Cool Fact” in each case.

# If OrderedDict is too much to deal with right now, you can cast it to a 
# conventional dict by changing that last line, print(row) to print(dict(row)), 
# and then the output looks like this:

{'Cool Name': 'Trevor Torres', 'Cool Birthday': '03-09-08', 'Cool Fact': 'Has never been out of the country.'}
{'Cool Name': 'Crystal Ellis', 'Cool Birthday': '17-11-06', 'Cool Fact': 'Published a small biography on a local legend.'}
# So, That is what csv.DictReader does: it takes this:

Cool Name,Cool Birthday,Cool Fact
Trevor Torres,03-09-08,Has never been out of the country.
Crystal Ellis,17-11-06,Published a small biography on a local legend.
... etc
# … and turns it into this:

{'Cool Name': 'Trevor Torres', 'Cool Birthday': '03-09-08', 'Cool Fact': 'Has never been out of the country.'}
{'Cool Name': 'Crystal Ellis', 'Cool Birthday': '17-11-06', 'Cool Fact': 'Published a small biography on a local legend.'}
... etc
… or, from the docs 2:
https://docs.python.org/3/library/csv.html#csv.DictReader

# Create an object that operates like a regular reader but maps the information in each row to an OrderedDict 3whose keys are given by the optional fieldnames parameter.

### (And that’s nothing compared to what Pandas can do!!)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Reading Different Types of CSV Files
# I need to level with you, I’ve been lying to you for the past two exercises. 
# Well, kind of. We’ve been acting like CSV files are Comma-Separated Values files. 
# It’s true that CSV stands for that, but it’s also true that other ways of separating 
# values are valid CSV files these days.

# People used to call Tab-Separated Values files TSV files, but as other separators 
# grew in popularity everyone realized that creating a new .[a-z]sv file format for 
# every value-separating character used is not sustainable.

# So we call all files with a list of different values a CSV file and then use 
# different delimiters (like a comma or tab) to indicate where the different values 
# start and stop.

# Let’s say we had an address book. Since addresses usually use commas in them, 
# we’ll need to use a different delimiter for our information. Since none of our 
# data has semicolons (;) in them, we can use those.
