# -*- coding: utf-8 -*-
"""
SMFSWdecor.py
Author: SMFSW
Copyright (c) 2016-2017 SMFSW

The MIT License (MIT)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


def is_match(_lambda, pattern):
    """ Check member value before launching function """
    from re import search
    from functools import wraps

    if isinstance(pattern, str):
        pattern = [pattern]     # make a list from the pattern
    elif not isinstance(pattern, list):
        return                  # return pattern is neither a string nor a list

    def wrapper(fct):
        """ wrapper
        :param fct: function to be wrapped
        :return: wrapper """
        @wraps(fct)
        def wrapped(self):
            """ wrapped function
            :param self: object instance
            :return: wrapped function """
            for i in pattern:
                if callable(_lambda) and search(i, (_lambda(self) or '')):
                    return fct(self)
        return wrapped
    return wrapper


if __name__ == "__main__":
    class Tst(object):
        def __init__(self, name):
            self.tst = name

        @is_match(lambda t: t.tst, 'tst1')
        def tst1(self):
            print("tst1 executed")

        @is_match(lambda t: t.tst, 'tst2')
        def tst2(self):
            print("tst2 executed")

        @is_match(lambda t: t.tst, ['tst1', 'tst2'])
        def tst3(self):
            print("tst3 executed")


    tst = Tst('tst1')
    tst.tst1()
    tst.tst2()
    tst.tst3()
