class Utils:

    @staticmethod
    def wait_for_element(action, expected, time, retries):
        result = action
        while result != expected and retries > 0:
            action = action
            time.sleep(time)
            retries = retries - 1
        return result
