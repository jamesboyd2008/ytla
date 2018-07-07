# This program runs another program every 60 seconds.

import btc_watcher
import time

def update():
    while True:
        btc_watcher.main()
        time.sleep(60)

update()
