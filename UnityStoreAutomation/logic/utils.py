import random
import time


class Utils:
    """
    Utility class for common helper functions.
    """

    @staticmethod
    def generate_random_number():
        """
        Generates a random number between 1 and 7 (inclusive).

        This method uses the randint function from the random module to generate
        a random integer within the specified range.

        :return: A random integer between 1 and 7.
        """
        return random.randint(1, 7)

    @staticmethod
    def wait_for_element(action, expected, time_to_sleep, retries):
        """
        Waits for a specific condition to be met by repeatedly executing an action.

        This method repeatedly executes the provided action until the result matches
        the expected value or the number of retries is exhausted. It pauses for a specified
        amount of time between each retry.

        :param action: A callable action to be executed.
        :param expected: The expected result of the action.
        :param time_to_sleep: The amount of time to wait between retries (in seconds).
        :param retries: The maximum number of retries.
        :return: The result of the action after the last attempt.
        """
        result = action
        while result != expected and retries > 0:
            time.sleep(time_to_sleep)
            retries = retries - 1
            result = action
        return result
