from game_parameters import get_random_apple_data

class Apple:
    def __init__(self):
        """
        a constructor for the apple object
        """
        x, y, score = get_random_apple_data()
        self.location = (x, y)
        self.score = score

    def get_location(self):
        """
        this function returns the apples location
        :return: a tuple containing the coordinates of the apple
        """
        return self.location

    def get_score(self):
        """
        this function returns the score the apple adds to the game score if it is eaten
        :return: an int containing the score the is to be added to the game score if the apple is eaten
        """
        return self.score