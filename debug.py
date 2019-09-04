import logging
import os

debugPath = "debug"
try:
        os.mkdir(debugPath)
except Exception:
        pass
logging.basicConfig(filename=(debugPath + "log.txt"), level=logging.DEBUG, format= '%(message)s')