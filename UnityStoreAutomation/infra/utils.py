import random
import string


class Utils:

    @staticmethod
    def generate_unique_comment(base_comment):
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"{base_comment} {unique_id}"

