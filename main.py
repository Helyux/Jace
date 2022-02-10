__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "10.02.2022"
__email__ = "m@hler.eu"
__status__ = "Development"


try:
    # Defaults
    import os
    import sys

    # Self
    from src import util

except ImportError as e:
    print(f"ERROR: Missing Module [{e}]")
    sys.exit()


def main():

    # Load toml config
    global config
    config = util.getConf("settings.toml")


if __name__ == "__main__":
    main()
