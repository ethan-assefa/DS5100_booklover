# This file creates a class called BookLover
## Ethan Assefa

# Includes necessary packages
import pandas as pd

class BookLover():
    # Define the docstring for this class
    '''
    Purpose: A class called BookLover to keep track of books read and their ratings. Allows for new books to be added.
    
    INPUTS:
    name: A person's name (str)
    email: Their email address (str)
    fav_genre: The favorite book genre (str)
    book_list: A dataframe of books read and their ratings (default creates empty dataframe)
        book_name: The names of the books read (str)
        book_rating: A numeric scale rating the book, from 0 to 5 (int)
    '''

    # Sets up the initialization
    def __init__(self, name, email, fav_genre, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        # Sets input for name as string (mandatory)
        self.name = str(name)
        # Sets input for email as string (mandatory)
        self.email = str(email)
        # Sets input for favorite genre as string (mandatory)
        self.fav_genre = str(fav_genre)
        # Sets input for dataframe of books (optional, default is empty)
        self.book_list = book_list
        # Sets number of books read as int (default = 0)
        self.num_books = 0
        self.num_books = int(len(book_list.axes[0]))

    # Method 1: Creates method to add book to book_list
    def add_book(self, book_name, rating):
        # Checks if name is string
        if not isinstance(book_name, str):
            print("The book name you have entered is not a string")
            return None
        # Checks if rating is int between 0 and 5
        elif not (isinstance(rating, int) and (0 <= rating <= 5)):
            print("The rating is not an integer value between 0 and 5")
            return None
        # Checks if book is already in list
        elif book_name in self.book_list.book_name.values:
            print("A book with this title is already in the list")
            return None
        # Adds a book to the dataframe 
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            # Updates the num_books value for the new number of books
            self.num_books = int(len(self.book_list.axes[0]))
    
    # Method 2: Creates method to check if a book has been read
    def has_read(self, book_name):
        # Checks if name is string
        if not isinstance(book_name, str):
            print("The book name you have entered is not a string")
            return None
        # Returns true/false depending on if book is in list
        else:
            return book_name in self.book_list.book_name.values
    
    # Method 3: Creates method to return the total number of books read
    def num_books_read(self):
        # Checks if the num_books attribute is equal to the row length of book_list
        if self.num_books == len(self.book_list.axes[0]):
            return self.num_books
        # If the counts are not equal, then the length of book_list is more accurate count
        else:
            # Updates the num_books value for the new number of books
            self.num_books = int(len(self.book_list.axes[0]))
            return self.num_books
        
    # Method 4: Creates method to return filtered dataframe of the favorite books
    def fav_books(self):
        # Filters dataset for books with rating above 3
        fav_books = self.book_list.query("book_rating > 3")
        return fav_books