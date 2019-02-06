import os
import time

res = os.popen('kaggle kernels status mayurnewase/more-features-of-future-sales').read()
print(res)
status = res.split(" ")[-1].strip("\n")
print(status)
while(True):
	if(status == "\"complete\""):
		#os.popen('notify-send -i face-wink "Hello! January" -u critical').read()
		os.system("ffplay /home/mayur/Downloads/deadpool_iphone.mp3 -nodisp")
		exit()
	time.sleep(20)
	res = os.popen('kaggle kernels status mayurnewase/more-features-of-future-sales').read()
	status = res.split(" ")[-1].strip("\n")
	print(status)
