import sys
import pytest


if __name__ == '__main__':
    # Exit with correct code
    sys.exit(pytest.main(["--pyargs", "pysnn.tests"] + sys.argv[1:]))
