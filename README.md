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