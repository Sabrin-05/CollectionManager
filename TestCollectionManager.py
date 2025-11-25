import unittest
from CollectionManager import Watch_list

class TestWatchList(unittest.TestCase):

    def test_add_movie(self):
        # Create a Watch_list instance
        watch_list = Watch_list()

        # Add a movie
        watch_list.add_movie("Inception", 148, "Action", ["Leonardo DiCaprio"], 9.0, "Complete")

        # Check that the movie was added
        self.assertEqual(len(watch_list.movies_list), 1)
        self.assertEqual(watch_list.movies_list[0].name, "Inception")
        self.assertEqual(watch_list.movies_list[0].length, 148)
        self.assertEqual(watch_list.movies_list[0].genre, "Action")
        self.assertEqual(watch_list.movies_list[0].actors, ["Leonardo DiCaprio"])
        self.assertEqual(watch_list.movies_list[0].ratings, 9.0)
        self.assertEqual(watch_list.movies_list[0].watch_status, "Complete")

if __name__ == '__main__':
    unittest.main()