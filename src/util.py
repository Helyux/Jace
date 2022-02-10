"""
TBD
"""

__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "10.02.2022"
__email__ = "m@hler.eu"
__status__ = "Development"


# Default
import shutil
import os.path


# Custom
import toml


def getConf(fname):
    """
    """
    if fname.endswith(".toml"):
        if os.path.isfile(fname):
            try:
                config = toml.load(fname)
                checkConf(config)
                return config
            except ValueError as e:
                print(f"The provided '.toml' is probably invalid, returned error:\n{e}")
                exit(1)
        else:
            print(f"Couldn't locate the '.toml' file [{fname}].")
            print("Creating a new '.toml' file from template, please edit and restart.")
            shutil.copy("src/template.toml", fname)
            exit(1)
    else:
        print(f"The provided config file [{fname}] is not a '.toml' file.")
        print("Creating a new '.toml' file from template, please edit and restart.")
        shutil.copy("src/template.toml", "prod.toml")
        exit(1)


def checkConf(config):
    """
    TODO check if keys exist
    """
    pass


if __name__ == "__main__":
    exit()
