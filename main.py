import pings
import subprocess as sp
import re
import requests
from datetime import datetime, date
import time
import threading
import csv

"""
this class uses python threading technic, if you don't know threading in python properly. please refer to artcile below before you started using this.
    https://realpython.com/intro-to-python-threading/
TimeoutTips:
    https://qiita.com/toshitanian/items/133b42355b7867f5c458

"""

class wifictrl:
    def __init__(self):
        self.target_url = "https://www.google.co.jp"

    def main(self):
        result = self.get_response(self.target_url)
        print(result)
        self.write_to_csv(result)
   
    def get_response(self,target_url):
        response = []
        start_time = time.time()
        response.append(int(start_time))
        result = requests.get(target_url)
        response.append(result.status_code)
        end_time = time.time()
        response.append(end_time-start_time)
        return response
    
    def write_to_csv(self,result):
        with open("result.csv","a") as file:
            wrcsv = csv.writer(file,lineterminator='\n')
            wrcsv.writerow(result)

if __name__ == "__main__":
  print("boot with standalone mode")
  xxxa = wifictrl()
  xxxa.main()


