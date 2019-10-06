import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class GenEds:
    def __init__(self):
        foundations = {
            "CR": False,
            "FL": False, 
            "QR": False, 
            "LF": False,
        }
        approaches = {
            "PL_PX": False,
            "SS/HS_1": False,
            "SS/HS_2": False,
            "SS/HS_3": False,
            "PH": False,
            "LA": False,
            "VP": False,
        }
        connections = {
            "CI": False,
            "QI": False,
            "EE": False,
            "US": False,
            "NA": False,
            "BN": False,
            "WB": False,
            "GL": False,
        }

