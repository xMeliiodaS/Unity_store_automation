import random
import string


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
