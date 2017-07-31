#todo: analyseid -> match (510)
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
    ext = None
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

    def insert(self, new_data, package_id, ext=None):
        new = packageUnit(new_data)
        new.id = package_id
        new.ext = ext

        if self.root is None:
            self.root = new
            self.size += 1
            return
        var = self.root
        while var.nextUnit is not None:
            var = var.nextUnit
        var.nextUnit = new
        self.size += 1

    def get(self, id, ext = None, alias=[]):
        if self.size == 0:
            return None
        else:
            var = self.root
            for i in range(0, self.size):
                if var.id == id:
                    if id == 0:
                        # remains


    def analyse_id




