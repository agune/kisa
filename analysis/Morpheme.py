# -*- coding: utf-8 -*-

__author__ = 'agun'
from konlpy.tag import *
engines = [Kkma(), Hannanum(), Mecab]


class Morpheme(object):
    kkma = None

    def __init__(self):
        self.kkma = Kkma()

    def nouns(self, content):
        noun = self.kkma.nouns(content)
        return noun