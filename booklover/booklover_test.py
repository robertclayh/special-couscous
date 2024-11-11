import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # Add a book and test if it is in `book_list`.
        test_object = BookLover("Frodo Baggins", "frodo@shire.com", "fantasy")
        test_object.add_book("The Fellowship of the Ring", 5)
        self.assertIn("The Fellowship of the Ring", test_object.book_list['book_name'].values)
        
    def test_2_add_book(self):
        # Add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Samwise Gamgee", "samwise@shire.com", "adventure")
        test_object.add_book("The Two Towers", 4)
        test_object.add_book("The Two Towers", 4)
        self.assertEqual(len(test_object.book_list[test_object.book_list['book_name'] == "The Two Towers"]), 1)
                
    def test_3_has_read(self): 
        # Pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Gandalf the Grey", "gandalf@middleearth.com", "spell books")
        test_object.add_book("The Return of the King", 5)
        self.assertTrue(test_object.has_read("The Return of the King"))
        
    def test_4_has_read(self): 
        # Pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Aragorn", "aragorn@dunedain.com", "history")
        test_object.add_book("The Silmarillion", 4)
        self.assertFalse(test_object.has_read("The Hobbit"))
        
    def test_5_num_books_read(self): 
        # Add some books to the list, and test num_books matches expected.
        test_object = BookLover("Legolas", "legolas@woodlandrealm.com", "fantasy")
        test_object.add_book("The Children of Hurin", 4)
        test_object.add_book("Unfinished Tales", 3)
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating > 3
        test_object = BookLover("Bilbo Baggins", "bilbo@hobbiton.com", "adventure")
        test_object.add_book("The Hobbit", 5)
        test_object.add_book("The Lord of the Rings", 4)
        test_object.add_book("The Adventures of Tom Bombadil", 2)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)