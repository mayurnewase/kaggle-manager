import argparse
import os
import time


class GetOutput():
	def __init__(self, user_name, kernel_name, dire):
		self.user_name = user_name
		self.kernel_name = kernel_name
		self.dir = dire

	def getOutput(self):
		os.popen('kaggle kernels output ' + self.user_name + "/" + self.kernel_name + " --path " + self.dir).read()



def main():
	parser = argparse.ArgumentParser(description = "default parser")
	parser.add_argument("--user_name")
	parser.add_argument("--kernel_name")
	parser.add_argument("--result_dir")
	args = parser.parse_args()

	cs = GetOutput(args.user_name, args.kernel_name, args.result_dir)
	cs.getOutput()

if __name__ == "__main__":
	main()









































