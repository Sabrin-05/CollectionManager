'''import unittest
from CollectionManager import Watch_list
from unittest import mock
from unittest import TestCase


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
    unittest.main()'''



import unittest
from unittest import mock
from CollectionManager import Watch_list

class WatchListTests(unittest.TestCase):
    @mock.patch('builtins.input', create=True)
    def test_add_movie(self, mocked_input):
        # Mock input to return specific values
        mocked_input.side_effect = ["Inception", "148", "Action", "Leonardo DiCaprio", "9.0", "Complete"]

        # Create a Watch_list instance
        watch_list = Watch_list()

        # Pretend add_movie is using input for values instead of direct method arguments
        watch_list.add_movie(
            mocked_input(),
            int(mocked_input()),      
            mocked_input(),
            [mocked_input()],         # Actors could be a parsed list
            float(mocked_input()),    
            mocked_input()
        )

        # Validate the movie added against expected details
        self.assertEqual(len(watch_list.movies_list), 1)
        movie = watch_list.movies_list[0]
        self.assertEqual(movie.name, "Inception")
        self.assertEqual(movie.length, 148)
        self.assertEqual(movie.genre, "Action")
        self.assertEqual(movie.actors, ["Leonardo DiCaprio"])
        self.assertEqual(movie.ratings, 9.0)
        self.assertEqual(movie.watch_status, "Complete")


if __name__ == '__main__':
    unittest.main()