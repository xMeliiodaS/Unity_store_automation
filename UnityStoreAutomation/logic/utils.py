import random
import string
import time


class Utils:
    """
    Utility class for common helper functions.
    """

    @staticmethod
    def generate_unique_comment(base_comment):
        """
        Generate a unique comment by appending a random alphanumeric string.

        :param base_comment: The base comment string.
        :return: The unique comment string.
        """
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"{base_comment} {unique_id}"

    @staticmethod
    def generate_random_number():
        """
        Generates a random number between 1 and 7 (inclusive).
        """
        return random.randint(1, 7)

    @staticmethod
    def wait_for_element(action, expected, time_to_sleep, retries):
        result = action
        while result != expected and retries > 0:
            time.sleep(time_to_sleep)
            retries = retries - 1
            result = action
        return result

