#writing a file
file =open('newFile.pdf', 'w')
file.write("My name is Rejoice. I am a girl.")

#reading a file
file=open('newFile.pdf', 'r')
content=file.read()
print(content)

#appending a file
file = open('newFile.pdf', 'a')
file.write("I am 20 years old.")

#input filename
user=input("filename:")

#reading user input file
# This code reads a file specified by the user and handles the case where the file does not
try:
    file=open(f"{user}", 'r')
    print(file.read()
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
finally:
    file.close()





















