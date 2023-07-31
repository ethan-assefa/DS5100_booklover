# This file creates a class called BookLoverTestSuite
## Ethan Assefa

# Import necessary packages
import unittest
import pandas as pd
# Imports the BookLover class from the other python file
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds book
        test1.add_book(book_name="Book", rating=0)
        # The actual title in the book list
        actual = str(test1.book_list.values)
        # Gives the expected book title we should get
        expected = "Book"
        # Checks if the values are equal
        self.assertIn(expected, actual)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test2 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds book once
        test2.add_book(book_name="Book", rating=0)
        # Adds same book again
        test2.add_book(book_name="Book", rating=0)
        # Calculates the count of the actual book from our list
        booktitle = "Book"
        actual = int(test2.book_list["book_name"].value_counts()[booktitle])
        # Gives the expected count
        expected = 1
        # Checks if the values are equal
        self.assertEqual(actual, expected)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test3 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds book
        test3.add_book(book_name="Book", rating=0)
        # Saves the has_read check as a value
        check = test3.has_read("Book")
        # Creates a message for if the test value is not true
        message = "Test value is not True."
        # Checks to make sure this method returns a True statement
        self.assertTrue(check, message)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test4 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds book
        test4.add_book(book_name="Book", rating=0)
        # Saves the has_read check as a value
        check = test4.has_read("Not Book")
        # Creates a message for if the test value is not false
        message = "Test value is not False."
        # Checks to make sure this method returns a False statement
        self.assertFalse(check, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test5 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds four books total
        test5.add_book(book_name="Book", rating=0)
        test5.add_book(book_name="Book 2: The Book Strikes Back", rating=5)
        test5.add_book(book_name="Book 3: Return of the Book", rating=3)
        test5.add_book(book_name="Book 4: Endbook", rating=2)
        # Gives the actual count of books
        actual = test5.num_books
        # Gives expected count of books
        expected = 4
        # Checks whether count of books is equal to expected count
        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        test6 = BookLover(name="Test", email="Test@mail.com", fav_genre="Test")
        # Adds four books total
        test6.add_book(book_name="Book", rating=4)
        test6.add_book(book_name="Book 2: The Book Strikes Back", rating=5)
        test6.add_book(book_name="Book 3: Return of the Book", rating=3)
        test6.add_book(book_name="Book 4: Endbook", rating=2)
        # Creates a message for if the test value is not true
        message = "Test value is not True."
        # Your test should check that the returned books have rating  > 3
        self.assertTrue((test6.fav_books().book_rating.values > 3).all(), message)
                
if __name__ == '__main__':

    unittest.main(verbosity=3)