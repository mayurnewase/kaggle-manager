import argparse
import kaggle
import time
import os

from utils import *
from notify import *

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--local_or_remote", type = str, default = "local")
	
	parser.add_argument("--user_name", type = str)
	parser.add_argument("--kernel_name", type = str, default = None)
	

	parser.add_argument("--competition_or_upload", type = str, default = "upload")
	parser.add_argument("--competition_name", type = str, default = None)

	parser.add_argument("--frequency", type = int, default = None)

	parser.add_argument("--notify", type = str, default = None)
	parser.add_argument("--notify_message", type = str, default = "kernel run finished for ")
	parser.add_argument("--tone_path", type = str, default = None)

	parser.add_argument("--message", type = str, default = "empty message")
	parser.add_argument("--result_dir", type = str, default = None)

	args = parser.parse_args()

	if(args.local_or_remote == "local"):
		s = Submit(args.kernel_name, args.message, args.competition_name)

		if(args.competition_upload == "competition"):
			s.submit_to_competition()
		else:
			s.upload()

	gs = CheckStatus(args.user_name, args.kernel_name, args.frequency)
	res = gs.getStatus()

	if(args.notify == "msg"):
		notify = Notify(args.kernel_name, args.notify_message)
		notify.notifyMessage()

	elif(args.notify == "linux"):
		notify = Notify(args.kernel_name, args.notify_message)
		notify.notifyLinux()
	
	elif(args.notify == "tone"):
		notify = Notify(args.kernel_name, args.notify_message, args.tone_path)
		notify.notifyTone()

	if(args.result_dir is not None):
		go = GetOutput(args.user_name, args.kernel_name, args.result_dir)
		go.getOutput()


if __name__ == "__main__":
	main()
