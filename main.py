import pings
import subprocess as sp
import re
import requests
from datetime import datetime, date
import time
import threading

"""
this class uses python threading technic, if you don't know threading in python properly. please refer to artcile below before you started using this.
    https://realpython.com/intro-to-python-threading/
TimeoutTips:
    https://qiita.com/toshitanian/items/133b42355b7867f5c458

"""

class Xxxx:
    def __init__(self):
        self.target_url = "https://www.google.com"

    def main(self):
        result = self.get_respons(self.target_url)
        print(result)
   
    def get_respons(self,target_url):
        start_time = time.time()
        print(str(start_time))

        try:
            result = requests.get(target_url)
        except:
            pass
        end_time = time.time()
        print(end_time-start_time)
        return result

    def write_to_csv():
        pass

if __name__ == "__main__":
  print("standalone/?")
  xxxa = Xxxx()
  xxxa.main()


