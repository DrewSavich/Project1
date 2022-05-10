import unittest
import random
from match_classes import Game


class Test_Game(unittest.TestCase):

    def setUp(self) -> None:
        """
        Creates an instance of the class
        Game and sets the random seed of
        1 for the computer preset random
        variables
        :return: None
        """
        self.game = Game()
        random.seed(1)  # Computer set: Rock, Scissor, Rock

    def tearDown(self) -> None:
        """
        Destroys the instance of the class
        Game and erases previous data to
        be reused for further tests
        :return: None
        """
        del self.game

    def test_choice_user(self) -> None:
        """
        Uses the choice_user() method to determine
        if the choice made from the gui are
        recognized and properly displayed.
        Sections of the return statement from
        the method are cut for ease of code reading.
        """
        self.assertEqual(str(self.game.choice_user(1))[-5:-1], 'rock', msg="Test 1.a")
        self.assertEqual(str(self.game.choice_user(2))[-6:-1], 'paper', msg="Test 1.b")
        self.assertEqual(str(self.game.choice_user(3))[-8:-1], 'scissor', msg="Test 1.c")

    def test_shoot(self) -> None:
        """
        Tests the method shoot() to determine
        if the function with the preset values
        are read and to determine if the method
        properly returns the expected string.
        """
        self.game.choice_user(2)
        self.assertEqual(self.game.shoot(), 'You win', msg="Test 2.a")

        self.game.choice_user(2)
        self.assertEqual(self.game.shoot(), 'You lose', msg="Test 2.b")

        self.game.choice_user(1)
        self.assertEqual(self.game.shoot(), "It's a tie", msg="Test 2.c")

    def test_two_result(self):
        """
        Tests the two_result() check section
        of the gui for scenarios with two wins
        in a row and properly returns the
        correct string.
        """
        self.game.choice_user(2)
        self.game.shoot()
        self.game.choice_user(1)
        self.game.shoot()
        self.assertEqual(self.game.two_result(), "GAME OVER - YOU WIN", msg="Test 3.a")
        self.tearDown()

        self.setUp()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(2)
        self.game.shoot()
        self.assertEqual(self.game.two_result(), "GAME OVER - COMPUTER WINS", msg="Test 3.b")

    def test_three_result(self) -> None:
        """
        Tests the core method three_results()
        to make sure all score scenarios, for
        the purpose of integers and not all
        combinations of the game, are properly
        read and properly responded with the
        correct string.
        """
        self.game.choice_user(2)
        self.game.shoot()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(2)
        self.game.shoot()
        self.assertEqual(self.game.three_result(), "GAME OVER - YOU WIN", msg="Test 4.a")
        self.tearDown()

        self.setUp()
        self.game.choice_user(2)
        self.game.shoot()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(1)
        self.game.shoot()
        self.assertEqual(self.game.three_result(), "GAME OVER - YOU WIN", msg="Test 4.b")
        self.tearDown()

        self.setUp()
        self.game.choice_user(1)
        self.game.shoot()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(1)
        self.game.shoot()
        self.assertEqual(self.game.three_result(), "GAME OVER - IT'S A TIE", msg="Test 4.c")
        self.tearDown()

        self.setUp()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(3)
        self.game.shoot()
        self.game.choice_user(1)
        self.game.shoot()
        self.assertEqual(self.game.three_result(), "GAME OVER - COMPUTER WINS", msg="Test 4.d")
        self.tearDown()

        self.setUp()
        self.game.choice_user(1)
        self.game.shoot()
        self.game.choice_user(2)
        self.game.shoot()
        self.game.choice_user(3)
        self.game.shoot()
        self.assertEqual(self.game.three_result(), "GAME OVER - COMPUTER WINS", msg="Test 4.e")


if __name__ == '__main__':
    unittest.main()
