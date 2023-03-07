#Story telling project

#Start by writing a short story. 
# It could be any type of story, such as a fairy tale, a mystery, a romance, or a science fiction adventure. 
# The story should be broken down into several parts or chapters.

#Define a function to display each chapter of the story. 
# This function should take a chapter number as input and display the text of that chapter.

#Create a menu function to allow the user to navigate through the story. 
# This function should display a menu with the chapter numbers and allow the user to select a chapter to read.

#Define a function to save the user's progress. 
# This function should take the current chapter number as input and save it to a file.

#Define a function to load the user's progress. 
# This function should read the saved chapter number from the file and return it.

#sample coding:
import time

# Define the story chapters
story = [
    "Chapter 1: Once upon a time...",
    "Chapter 2: The hero sets out on a quest...",
    "Chapter 3: The hero encounters a challenge...",
    "Chapter 4: The hero overcomes the challenge...",
    "Chapter 5: The hero returns home...",
]

# Define a function to display a chapter
def display_chapter(chapter_num):
    print(story[chapter_num - 1])
    time.sleep(2)  # Wait for 2 seconds to give the user time to read the chapter

# Define a function to display the menu
def display_menu(current_chapter):
    print("Welcome to the story!")
    print("You are currently on chapter", current_chapter)
    print("Please select a chapter to read:")
    for i in range(1, len(story) + 1):
        print(f"{i}. Chapter {i}")
    print("0. Exit")

# Define a function to save progress
def save_progress(current_chapter):
    with open("progress.txt", "w") as f:
        f.write(str(current_chapter))

# Define a function to load progress
def load_progress():
    try:
        with open("progress.txt", "r") as f:
            current_chapter = int(f.read())
    except FileNotFoundError:
        current_chapter = 1
    return current_chapter

# Main program loop
def main():
    current_chapter = load_progress()
    while True:
        display_menu(current_chapter)
        choice = int(input())
        if choice == 0:
            break
        elif choice <= len(story):
            display_chapter(choice)
            current_chapter = choice
            save_progress(current_chapter)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

#This program reads the story chapters from a list and displays a menu for the user to navigate through them. 
# It saves the user's progress to a file so they can resume reading from where they left off. 
# We can modify this code to add our own story and customize the menu and display functions to suit our needs.
