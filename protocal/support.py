import _thread
import threading
import random
import sys
from codecs import decode, encode
import string
import time
import datetime
import json

class packageUnit:
    info = None
    id = 0
    nextUnit = None

    def __init__(self, info):
        self.info = info


class packageMenu:
    def __init__(self):
        self.size = 0
        self.root = packageUnit(None)
        self.root = None
        return

    def __init__(self):
        self.root = None
        self.size = 0

    def __del__(self):
        if self.root is None:
            return
        self.root = None
        self.size = 0

#todo: the insert method