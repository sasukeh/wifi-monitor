# coding=utf-8
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
        """
        @TODO:
        set multiple site to stabilize monitoring for production.
        """
        self.target_url1 = "https://www.google.co.jp"
        self.target_url2 = "https://www.yahoo.co.jp"
        self.target_url3 = "https://www.facebook.com"

    def main(self):
        result = self.get_response(self.target_url1)
        try:
            self.write_to_csv(result)
        except:
            print("failed to get response")
        try:
            self.power_management()
        except:
            pass
   
    def get_response(self,target_url):
        response = []
        start_time = time.time()
        response.append(int(start_time))
        try:
            result = requests.get(target_url,timeout=(0.3,0.5))
            response.append(result.status_code)
            end_time = time.time()
            response.append(result.elapsed.total_seconds())
            return response
        except:
            print("timeout detected")
            response.append("timeout")
            end_time = time.time()
            response.append(0.600000)
            return response
    
    def write_to_csv(self,result):
        with open("result.csv","a") as file:
            wrcsv = csv.writer(file,lineterminator='\n')
            wrcsv.writerow(result)

    def timeout_check(self):
        timeout_count = 0
	result_list=[]
        with open("result.csv","r") as file:
            result_csv = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            #result_csv_r = result_csv.reverse()
            for row in result_csv:
                result_list.append([row[0],row[1],row[2]])
                
            result_list_r = list(reversed(result_list))
            if len(result_list_r) < 60:
                print("waiting for enough logs")
            else:
                #This value should be 60 for prod..temporaly set 20 for test
                for i in range(20):
                    if result_list_r[i][1] == "timeout":
                        timeout_count = timeout_count + 1
                print("Timeout Count : " +str(timeout_count))
                if timeout_count > 5:
                    return False
                else:
                    return True


    def power_management(self):
        #timeout_countが過去５分間に30を超える、つまり5分間不安定or切断が続くのであれば、tp-linkに対して電源を落として、再投入するリクエストをする
        #一回目Falseを検知すると一旦電源を落として上げる
        # x分程度待ってFalseか判断し、Falseであればもう一度チャンレジする
        boot_flag = False
        start_process_time=0
        print("==================== Power Management ====================")
        if self.timeout_check() == True:
            print("Status is normal")
        elif self.timeout_check() == False and boot_flag == False :
            print("now checking for wifi device")
            boot_start_time = time.time()
            print("restart wifi device")
            boot_flag = True
            # Bootflagを保持するためにファイルに書き込む or daemon化が必要そうなので、Whileで書く、もしくは、forkかthreadを使う。
            #現状だと、ずっとTrueのまま
            #実行方法をシンプルにする/watchは使わない。
        elif boot_flag == True:
            current_time = time.time()
            print("now booting up wifi")



        return True



    def log_lotate(self):
        #5秒でログを取っているので一日で17280になる。
        #17280のログが取れたらrotateする
        pass


if __name__ == "__main__":
  xxxa = wifictrl()
  xxxa.main()


