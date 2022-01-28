import os
import sys
sys.path.append(os.path.realpath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src')))
sys.path.append(os.path.join('..', 'src'))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import Taqqiq


def main():
    """
    execution script for KeyRing
    """

    try:
        Taqqiq.entry()
    except KeyboardInterrupt:
        print("\nKeyRing has been forcefully stopped using CTRL+C")


if __name__ == '__main__':
    main()



