import sys
import my_pip


def test_ping():
    sys.argv = ['foo', '10']
    my_pip.ping()

