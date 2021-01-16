import discord
from discord.ext import commands
import random
import numpy


def root(num_list):
    poly = numpy.poly1d(num_list)
    answer = poly.roots
    return answer