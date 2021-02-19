import sys

from discover import discover
from sat2rf1 import logger, utilities

def main():
    utilities.tests()
    logger.info("Done")
    sys.exit(0)
