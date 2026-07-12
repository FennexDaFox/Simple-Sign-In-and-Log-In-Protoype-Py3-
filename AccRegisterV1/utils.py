import time
import os


def wait(dur: float):
    time.sleep(dur)


def cls():
    # easily spam clear the terminal XD
    os.system("cls" if os.name == "nt" else "clear")


def divider(amount) -> int:
    # make a devider using "=" and multiply it
    print("=" * amount)
