# -*- coding: utf-8 -*-
"""
SMFSWlogic.py
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


def swap_uint16(val):
    """ Byte swap val (unsigned int16)
    :param val: value u16
    :return: swapped u16 """
    tmp = (val << 8) | (val >> 8)
    return tmp & 0xFFFF


def swap_int16(val):
    """ Byte swap val (int16)
    :param val: value i16
    :return: swapped i16 """
    tmp = (val << 8) | ((val >> 8) & 0xFF)
    return tmp & 0xFFFF


def swap_uint32(val):
    """ Byte swap val (unsigned int32)
    :param val: value u32
    :return: swapped u32 """
    tmp = ((val << 8) & 0xFF00FF00) | ((val >> 8) & 0xFF00FF)
    tmp = (tmp << 16) | (tmp >> 16)
    return tmp & 0xFFFFFFFF


def swap_int32(val):
    """ Byte swap val (int32)
    :param val: value i32
    :return: swapped i32 """
    tmp = ((val << 8) & 0xFF00FF00) | ((val >> 8) & 0xFF00FF)
    tmp = (tmp << 16) | ((tmp >> 16) & 0xFFFF)
    return tmp & 0xFFFFFFFF


def swap_int64(val):
    """ Byte swap val (int64)
    :param val: value i64
    :return: swapped i64 """
    tmp = ((val << 8) & 0xFF00FF00FF00FF00) | ((val >> 8) & 0x00FF00FF00FF00FF)
    tmp = ((tmp << 16) & 0xFFFF0000FFFF0000) | ((tmp >> 16) & 0x0000FFFF0000FFFF)
    tmp = (tmp << 32) | ((tmp >> 32) & 0xFFFFFFFF)
    return tmp & 0xFFFFFFFFFFFFFFFF


def swap_uint64(val):
    """ Byte swap val (unsigned int64)
    :param val: value u64
    :return: swapped u64 """
    tmp = ((val << 8) & 0xFF00FF00FF00FF00) | ((val >> 8) & 0x00FF00FF00FF00FF)
    tmp = ((tmp << 16) & 0xFFFF0000FFFF0000) | ((tmp >> 16) & 0x0000FFFF0000FFFF)
    tmp = (tmp << 32) | (tmp >> 32)
    return tmp & 0xFFFFFFFFFFFFFFFF


def conv_16to8(v):
    """ Conversion d'une variable 16 bits en 8 bits
    :param v: var (16b)
    :return: 8bit conversion """
    return (v >> 8) & 0xFF


def conv_8to16(v):
    """ Conversion d'une variable 8 bits en 16 bits
    :param v: var (8b)
    :return: 16bit conversion """
    return ((v << 8) + v) & 0xFFFF


def conv_8upto16(val, nb):
    """ converts val (8bits) to 8+n bits (n must be comprised between 0 & 8 bits)
    :warning: conversion output shall not exceed 16bits (input shall strictly be unsigned 8bits)
    :warning: nb shall be in range 0-8 (note that using 0 doesn't change val)
    :param val: 8b var to convert
    :param nb: nb of bit pseudo shifts to add
    :return: 8+n bits conversion result """
    return ((val << nb) + (val & (0xFF >> (8 - nb)))) & 0xFFFF


def conv_16upto32(val, nb):
    """ converts val (16bits) to 16+n bits (n must be comprised between 0 & 16 bits)
    :warning: conversion output shall not exceed 32bits (input shall strictly be unsigned 16bits)
    :warning: nb shall be in range 0-16 (note that using 0 doesn't change val)
    :param val: 16bit var to convert
    :param nb: nb of bit pseudo shifts to add
    :return: 16+n bit conversion result """
    return ((val << nb) + (val & (0xFFFF >> (16 - nb)))) & 0xFFFFFFFF


def bin2gray(val):
    """ convert an unsigned binary number to reflected binary Gray code.
    :param val: value to convert (binary)
    :return: gray code """
    return (val >> 1) ^ val


def gray2bin(val):
    """  convert a binary Gray code number to reflected binary number.
    :param val: value to convert (gray code)
    :return: binary value """
    bits = 64
    tmp = val

    max_val = 0
    for i in range(bits):
        max_val |= 1 << i

    try:
        assert tmp <= max_val
    except AssertionError:
        print("nb should be {}bits max".format(bits))
        return

    # for up to 2^n bits, convert Gray to binary by performing (2^n)-1 bin2gray conversions
    # for i in range(bits-1):
    #     tmp = bin2gray(tmp)

    bits >>= 1                  # if not, perform first xor with 0
    while bits > 0:
        tmp ^= (tmp >> bits)    # xor current with current shifted decreasing pow 2 right
        bits >>= 1              # next decreasing pow 2 (Leave at the end)

    return tmp


if __name__ == "__main__":
    print("SWAP:")
    tst = 0x5AA5
    print("Input 16: {}".format(hex(tst)))
    tst = swap_uint16(tst)
    print("Swapped 16: {}".format(hex(tst)))
    print("")
    tst = 0x5AA55AA5
    print("Input 32: {}".format(hex(tst)))
    tst = swap_uint32(tst)
    print("Swapped 32: {}".format(hex(tst)))
    print("")
    tst = 0x5AA55AA55AA55AA5
    print("Input 64: {}".format(hex(tst)))
    tst = swap_uint64(tst)
    print("Swapped 64: {}".format(hex(tst)))

    print("")
    print("CONVERT:")
    tst8 = 0xFF
    tst16 = 0xFFFF
    print("Conv 8 to 16: {}".format(hex(conv_8to16(tst8))))
    print("Conv 16 to 8: {}".format(hex(conv_16to8(tst16))))
    print("Conv 16 to 32: {}".format(hex(conv_16upto32(tst16, 16))))

    print("")
    tst = 0x101526B1
    print("Input bin: {}".format(hex(tst)))
    tst = bin2gray(tst)
    print("Grayed bin: {}".format(hex(tst)))
    tst = gray2bin(tst)
    print("Back to bin: {}".format(hex(tst)))
