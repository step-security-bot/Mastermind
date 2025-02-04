import unittest

from mastermind.utils.get_feedback import generate_feedback


class TestGenerateFeedback(unittest.TestCase):
    """Test suite for the generate_feedback function"""

    def test_generate_feedback_with_exact_matches(self):
        """Test that generate_feedback correctly counts exact matches"""
        guess = (1, 2, 3)
        secret = (1, 2, 3)
        number_of_colors = 3
        black_pegs, white_pegs = generate_feedback(guess, secret, number_of_colors)
        self.assertEqual(black_pegs, 3)
        self.assertEqual(white_pegs, 0)

    def test_generate_feedback_with_partial_matches(self):
        """Test that generate_feedback correctly counts partial matches"""
        guess = (1, 2, 3)
        secret = (1, 2, 4)
        number_of_colors = 4
        black_pegs, white_pegs = generate_feedback(guess, secret, number_of_colors)
        self.assertEqual(black_pegs, 2)
        self.assertEqual(white_pegs, 0)

    def test_generate_feedback_with_white_pegs(self):
        """Test that generate_feedback correctly counts colors in wrong positions"""
        guess = (1, 2, 3)
        secret = (3, 1, 2)
        number_of_colors = 4
        black_pegs, white_pegs = generate_feedback(guess, secret, number_of_colors)
        self.assertEqual(black_pegs, 0)
        self.assertEqual(white_pegs, 3)

    def test_generate_feedback_with_no_matches(self):
        """Test that generate_feedback correctly counts when there are no matches"""
        guess = (1, 2, 3)
        secret = (4, 5, 6)
        number_of_colors = 6
        black_pegs, white_pegs = generate_feedback(guess, secret, number_of_colors)
        self.assertEqual(black_pegs, 0)
        self.assertEqual(white_pegs, 0)

    def test_generate_feedback_with_duplicate_colors(self):
        """Test that generate_feedback correctly counts when the guess and secret have duplicate colors"""
        guess = (1, 1, 2)
        secret = (1, 2, 2)
        number_of_colors = 3
        black_pegs, white_pegs = generate_feedback(guess, secret, number_of_colors)
        self.assertEqual(black_pegs, 2)
        self.assertEqual(white_pegs, 0)

    def test_generate_feedback_with_complex_duplicates(self):
        """Test generate_feedback with complex duplicate color scenarios"""
        test_cases = [
            ((1, 1, 1), (1, 2, 2), 1, 0),
            ((1, 2, 1), (2, 1, 1), 1, 2),
            ((1, 1, 2), (2, 1, 1), 1, 2),
        ]
        for guess, secret, exp_black, exp_white in test_cases:
            black_pegs, white_pegs = generate_feedback(guess, secret, 3)
            self.assertEqual((black_pegs, white_pegs), (exp_black, exp_white))


if __name__ == "__main__":
    unittest.main()
