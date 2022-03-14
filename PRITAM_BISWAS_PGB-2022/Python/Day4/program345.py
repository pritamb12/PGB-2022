"""
3. Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space.
"""
def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("file.txt"))
"""
4. Write a Python program to remove newline characters from a file (multiple blank lines)
"""
with open("file.txt") as f:
    print ("".join(line for line in f if not line.isspace()))
"""
5. Write a Python program to copy the contents of a file to another file .( if file already exits then raise a exception and use input from user to create a new file with new name)
"""
# open both files
with open('file.txt', 'r') as firstfile, open('newfile.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)


import csv

file = open('Sample.csv')

type(file)

csvreader = csv.reader(file)