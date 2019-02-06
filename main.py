import argparse
import kaggle
import time
import os

from get_status import *
from submit import *
from get_output import *
"""
input -> 
	take kernel name/path -> pre-exist on kaggle / submit from local directory
	submit it
	result dir
	actions on submitted kernel-> 
		add it in check pool
		add frequency
		notify
		store output

output ->
	status
	result
"""

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--local_or_remote", type = int)
	parser.add_argument("--user_name", type = str)
	parser.add_argument("--kernel_name", type = str)
	parser.add_argument("--competition_name", type = str)
	parser.add_argument("--frequency", type = int, default = 0)

	parser.add_argument("--message", type = str, default = "nope lmao")
	parser.add_argument("--result_dir", type = str, default = None)

	args = parser.parse_args()

	if(args.local_or_remote == 0):
		#submit first
		s = Submit(args.kernel_name, args.message, args.competition_name)
		s.upload()
	
	gs = CheckStatus(args.user_name, args.kernel_name, args.frequency)
	res = gs.getStatus()

	if(args.result_dir is not None):
		go = GetOutput(args.user_name, args.kernel_name, args.result_dir)
		go.getOutput()

	


if __name__ == "__main__":
	main()














































