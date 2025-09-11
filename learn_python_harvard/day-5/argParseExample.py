import argparse


parser = argparse.ArgumentParser(description="Print something")
parser.add_argument("-n", default=1, help="Number of times to print", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("Hello")

"""
This to handle the command line arguments.
Check below commands :
python argParseExample.py
python argParseExample.py -h
python argParseExample.py -n 3
"""