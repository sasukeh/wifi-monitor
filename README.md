module検討

pings:
root privilidge必要らしいので難しそう

Don't need to use row socket.
Just use os function

----------
## monitoring方法
csv_exporter.pyでCSVにひたすら下記のフォーマットで書き出す

monitor.pyでそのCSVを監視

両方のインスタンスについては、main.pyから操作する


## file output
os.

## daemonize
daemon.

https://qiita.com/croquisdukke/items/9c5d8933496ba6729c78

- case1
- case2
when it is failing, write filedtime and message of fail to csv file.

## issue
requests timeout is something wrong
if set timeout=(0.1,0.1) but that is not works well... the time is totally defferent from what i expected.

