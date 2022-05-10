import random

class Game:

    def __init__(self) -> None:
        self.__user = ''  # The slot for user choice
        self.__comp = ''  # The slot for computer choice
        self.__score = 0  # The slot for score tallying

    def choice_user(self, p1) -> str:
        """
        Sets the choices from the user and generates the
        choice for the computer. Returns the choices made
        from both sides after verifying it is a choice
        :param p1: Text received from the entry box
        :return: A display telling what both side chose
        """
        options = ['rock', 'paper', 'scissor']
        self.__user = options[p1-1]
        self.__comp = options[random.randint(0, 2)]
        return f'Computer is {self.__comp}. You are {self.__user}.'

    def shoot(self) -> str:
        """
        Compares the options of user and computer, then
        displays the result of the match while returning
        a score into the object for final results
        :return: The results of the match
        """
        if self.__user == 'rock':
            if self.__comp == 'rock':
                return f"It's a tie"
            elif self.__comp == 'paper':
                self.__score -= 1
                return f"You lose"
            elif self.__comp == 'scissor':
                self.__score += 1
                return f"You win"

        elif self.__user == 'paper':
            if self.__comp == 'rock':
                self.__score += 1
                return f"You win"
            elif self.__comp == 'paper':
                return f"It's a tie"
            elif self.__comp == 'scissor':
                self.__score -= 1
                return f"You lose"

        if self.__user == 'scissor':
            if self.__comp == 'rock':
                self.__score -= 1
                return f"You lose"
            elif self.__comp == 'paper':
                self.__score += 1
                return f"You win"
            elif self.__comp == 'scissor':
                return f"It's a tie"

    def two_result(self) -> str:
        """
        Displays the end title and prints the results
        of the winner. Made to check if the score
        has reached -2 or 2.
        :return: The results according to the score
        """
        if self.__score == -2:
            return f"GAME OVER - COMPUTER WINS"
        elif self.__score == 2:
            return f"GAME OVER - YOU WIN"

    def three_result(self) -> str:
        """
        Displays the end title and prints the results
        of the winner. Checks the final score after
        the third match.
        :return: The results according to the score
        """
        if self.__score == 0:
            return f"GAME OVER - IT'S A TIE"
        elif self.__score >= 1:
            return f"GAME OVER - YOU WIN"
        elif self.__score <= -1:
            return f"GAME OVER - COMPUTER WINS"

