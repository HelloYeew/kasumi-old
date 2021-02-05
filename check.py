import subprocess
import sys
import urllib.request

def check_library():
    print("Start checking important library to run a program...")

    # check discord.py
    print("Checking discord.py...")
    try:
        import discord
    except ImportError:
        print("Discord.py not found.")
        print("Run install command : -m pip3 install discord.py")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'discord.py'])
        print("Discord.py install complete!")

    # check scipy
    print("Checking scipy...")
    try:
        import scipy
    except ImportError:
        print("Scipy not found.")
        print("Run install command : -m pip3 install Scipy")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'scipy'])
        print("Scipy install complete!")

    # check numpy
    print("Checking numpy...")
    try:
        import numpy
    except ImportError:
        print("Scipy not found.")
        print("Run install command : -m pip3 install numpy")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'numpy'])
        print("Scipy install complete!")

    # check requests
    print("Checking requests...")
    try:
        import requests
    except ImportError:
        print("Requests not found.")
        print("Run install command : -m pip3 install requests")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'requests'])
        print("Requests install complete!")

    # check pandas
    print("Checking pandas...")
    try:
        import pandas
    except ImportError:
        print("Pandas not found.")
        print("Run install command : -m pip3 install pandas")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'pandas'])
        print("Pandas install complete!")

    # check logging
    print("Checking logging...")
    try:
        import logging
    except ImportError:
        print("Logging not found.")
        print("Run install command : -m pip3 install logging")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'logging'])
        print("Logging install complete!")

    # check pornhubapi
    print("Checking pornhubapi...")
    try:
        import pornhubapi
    except ImportError:
        print("Pornhubapi not found.")
        print("Run install command : -m pip3 install pornhubapi")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'pornhubapi'])
        print("Pornhubapi install complete!")

    # check NHentai-API
    print("Checking NHentai-API...")
    try:
        import NHentai
    except ImportError:
        print("NHentai-API not found.")
        print("Run install command : -m pip3 install NHentai-API")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", 'NHentai-API'])
        print("NHentai-API install complete!")



def check_internet(url='http://www.youtube.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False
