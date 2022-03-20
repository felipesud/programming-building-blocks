# Checkpoint Week 11 Files
# From: https://byui-cse.github.io/cse110-course/lesson11/checkpoint.html
# By: Felipe dos Santos Belisário

# Overview: Practice Opening Files

with open("books.txt") as books:

   
    for line in books:
        book = line.strip()
        print(book)

        