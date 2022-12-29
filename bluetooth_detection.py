"""
https://qiita.com/kenichih/items/8baa27b3aecc94dd8193

https://atatat.hatenablog.com/entry/2020/07/09/003000

pip install bleak
"""

import asyncio
from bleak import discover

async def run():
    print("検出中")
    devices = await discover()
    for d in devices:
        if d.name != "Unknown" and d.rssi > -90:    #約1〜1.5mにあるとき
            print("強さ：", d.rssi, "     端末：",  d.name)

def main():
  tim = 1
  while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    print()
    print("{}秒後再開します。".format(tim))
    time.sleep(tim)

if __name__ == "__main__":
  main()
