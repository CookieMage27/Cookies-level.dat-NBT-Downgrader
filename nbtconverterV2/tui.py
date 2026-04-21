import sys
import argparse

parser = argparse.ArgumentParser(description="Takes a level.dat input file and asks details on what to do with it, then passes the information on to main.py."
	)

def processArgs():
	parser.add_argument("level.dat", type = str, help = "A Minecraft level.dat file (1.21.11 or older), to be downgraded")
	
