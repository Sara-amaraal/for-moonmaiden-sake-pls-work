import os

def run_tests():
    """
    Discover and execute test scripts located in specific directories.

    This function searches for test directories in the current working directory.
    If the current working directory ends with "quirked-up-software," it will look for a subdirectory named "DEV/testing"
    and change the working directory to it. If the current working directory ends with "DEV," it will look for a
    subdirectory named "testing" and change the working directory to it.

    It then identifies test scripts in the selected directory, executes them, and captures the results.

    Returns:
        None

    """
    PATH = os.getcwd()

    if PATH.endswith("quirked-up-software"):
        PATH = os.path.join(PATH, "DEV", "testing")
        os.chdir(PATH)

    elif PATH.endswith("DEV"):
        PATH = os.path.join(PATH, "testing")
        os.chdir(PATH)
        
    REQS = os.listdir()

    for REQ in REQS:
        SUBPATH = os.path.join(PATH, REQ)
        if os.path.isdir(SUBPATH):
            os.chdir(SUBPATH)
            FILES = os.listdir()
            for TEST in FILES:
                if TEST.startswith("Test"):
                    os.system('python ' + TEST)
    return

if __name__ == "__main__":
    run_tests()
