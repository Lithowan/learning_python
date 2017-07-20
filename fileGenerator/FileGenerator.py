import sys
import os

num_files = input("How many files would you like to create? " )

if not num_files.isdecimal():
    print("You broke it... already.")
    exit(1)
elif int(num_files) <= 0:
    print("You broke it... already.")
    exit(1)
else:
    num_files = int(num_files)

print("Generating", num_files, "files...")

for i in range(1,num_files+1):
    if not os.path.isfile('fileGenerator/file_'+str(i)+'.txt'):
        created_file = open('fileGenerator/file_'+str(i)+'.txt',"wb")