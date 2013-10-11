import os.path
FIXTURES_DIR = "fixtures"

def get_fixture(name):
    """
    Quickly get a fixture for use in a test
    """
    return file(
        reduce(os.path.join, [
            os.path.dirname(__file__),
            FIXTURES_DIR,
            name
            ])
        ).read()


