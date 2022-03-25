# File: 12-Team_Activity.py
# Reference: https://byui-cse.github.io/cse110-course/lesson12/teach.html

largest = 0
largest_book = None

user_scripture = input("\nChoice one of the following scriptures: \n- Old Testament\n- New Testament\n- Book of Mormon\n- Doctrine and Covenants\n- Pearl of Great Price\nType here: ")

with open("resources/books_and_chapters.txt") as books_list:
    print()
    for line in books_list:
        line = line.strip()
        book, chapters, scripture = line.split(":")
        
        if scripture.lower() == user_scripture.lower():
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
            
            if largest < int(chapters):
                largest = int(chapters)
                largest_book = book

if largest_book:
    print(f"\nThe largest Book is {largest_book} with {largest} chapters.")