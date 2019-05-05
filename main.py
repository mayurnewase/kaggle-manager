import argparse
import kaggle
import time
import os

from utils import *
from notify import *

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--local_or_remote", type = str, default = "local")
	parser.add_argument("--competition_or_upload", type = str, default = "upload") #optional -> only if submit/upload

	parser.add_argument("--user_name", type = str)
	parser.add_argument("--kernel_name", type = str, default = None)
	
	parser.add_argument("--competition_name", type = str, default = None)  #optional ->only if to submit

	parser.add_argument("--frequency", type = int, default = None)

	parser.add_argument("--notify", type = str, default = None) #msg/desktop/tone
	parser.add_argument("--notify_message", type = str, default = "kernel_run_finished")
	parser.add_argument("--tone_path", type = str, default = None)

	parser.add_argument("--result_dir", type = str, default = None) #optional -> to save resukt
	parser.add_argument("--master_path", type = str, default = None) #optional
	parser.add_argument("--result_to_append", type = str, default = None)#optional -> to append in master callback

	args = parser.parse_args()

	preProcessor()

	if(args.local_or_remote == "local"):
		s = Submit(args.kernel_name, args.competition_name)

		if(args.competition_or_upload == "competition"):
			s.submit_to_competition()
		else:
			s.upload()

	gs = CheckStatus(args.user_name, args.kernel_name, args.frequency)
	res = gs.getStatus()

	if res == 1:
		print("Kernel run failed")
		
		if(args.notify == "msg"):
			notify = Notify(args.kernel_name, "Failed_with_error")
			notify.notifyMessage()

		elif(args.notify == "desktop"):
			notify = Notify(args.kernel_name, "Failed_with_error")
			notify.notifyDesktop()
		
		elif(args.notify == "tone"):
			notify = Notify(kernel_name = args.kernel_name, tone_path = args.tone_path)
			notify.notifyTone()		

		return 1

	all_result_files = None
	if(args.result_dir is not None):
		go = GetOutput(args.user_name, args.kernel_name, args.result_dir)
		all_result_files = go.getOutput()

	postProcessor(args.user_name, args.kernel_name, args.master_path, args.result_dir, all_result_files, args.result_to_append)

	if(args.notify == "msg"):
		notify = Notify(args.kernel_name, args.notify_message)
		notify.notifyMessage()

	elif(args.notify == "desktop"):
		notify = Notify(args.kernel_name, args.notify_message)
		notify.notifyDesktop()
	
	elif(args.notify == "tone"):
		notify = Notify(kernel_name = args.kernel_name, tone_path = args.tone_path)
		notify.notifyTone()





if __name__ == "__main__":
	main()