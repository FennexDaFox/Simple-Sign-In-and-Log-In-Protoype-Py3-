import time
import os


def wait(dur: float):
    time.sleep(dur)


def cls():
    # easily spam clear the terminal XD
    os.system("cls" if os.name == "nt" else "clear")


def divider():
    # make a devider using "=" and multiply it with 36
    print("=" * 36)
