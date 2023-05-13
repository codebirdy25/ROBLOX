import requests
import os

def GetRobloxVersion(Version=""):
    Version = requests.get("http://setup.roblox.com/version.txt").content.decode("ascii")
    return Version
