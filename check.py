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
        print("Run install command : -m pip install discord.py")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
        print("Discord.py install complete!")
    finally:
        import discord

        # check scipy
        print("Checking scipy...")
        try:
            import scipy
        except ImportError:
            print("Scipy not found.")
            print("Run install command : -m pip install Scipy")
            subprocess.check_call([sys.executable, "-m", "pip", "install", 'scipy'])
            print("Scipy install complete!")
        finally:
            import scipy

        # check scipy
        print("Checking numpy...")
        try:
            import scipy
        except ImportError:
            print("Scipy not found.")
            print("Run install command : -m pip install Scipy")
            subprocess.check_call([sys.executable, "-m", "pip", "install", 'scipy'])
            print("Scipy install complete!")



def check_internet(url='http://www.youtube.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False
