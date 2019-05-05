# kaggle-manager
Personal manager for Kaggle competitions.

## Why
Recently kaggle is launching kernel only competitions which requires kernels to be run on kaggle platform with some restrictions,
which is good thing because it restricts competitors from computational brut-forcing and allows some creativity in solutions,but it comes with the cost.

Kaggle provides only 1 gpu per kernel so running heavy kernels takes some extra time.
So I created this framework to reduce my pain and automate some of my tasks on kaggle.

## Features
1.Uses kaggle official api.

2.Automatic kernel uploading or submitions to competitions.

3.Automatic status check of running kernel and notifications when finished.

4.Custom postprocessing of results.

5.Multiple notifications type supported.(currently support messaging, desktop notification, tone)

## Usage
1.Clone repo
```
git clone https://github.com/mayurnewase/kaggle-manager.git
cd kaggle-manager
```
2.Install requirements
```
pip install -r requirements.txt
```
3.Set up kaggle api,if you haven't already.It's great way to do things quickly.
refer to [official docs](https://www.kaggle.com/docs/api) for this.

4.***[optional]*** If you want to use messaging notifications,you will need twillio account.
Don't worry it's free but you can send messages only on one registered personal number.

If you want to send message to whole team you may need premium account.(or other services which do it for free.In future this can be supported...)

Please go to [twillio](https://www.twillio.com) and create account,and save following ids.
```
account_sid
auth_token
twillio_number
personal_number_registered_on_twillio
```
Now open .env file and fill those entries.

5. Create your own post-processor for results,by default it appends selected file to master log.
```
It's a callback function which is called after kernel run is finished and results are downloaded successfully.
You can modify utils/postProcessor() function according to your need.
Make sure it take following arguments
  user_name
  kernel_name
  master_log
  result_path
  all_result_files
  result_file_to_append
```

6.Now you can run main file to upload local kernel and track its status or hook up existing kernel.

For example,to hook up currently running kernel,
```
python main.py --local_or_remote=remote --user_name=your_kaggle_name --kernel_name=simple-lstm
                --frequency=100 -- notify=msg --result_dir=../competition/result/
                --master_log=../competition/master_log --result_to_append=submission.csv
```
Arguments available are,
```
local_or_remote -> where is kernel that you want to track
competition_or_upload -> [optional] required only if kernel needs to upload.Is it competition submition or just upload with random dataset(need to setup metadata file)(This feature currently is in progress,please use kaggle api for now to upload kernels)
competition_name -> [optional] required only for competition submission.Competition name as it appears in url bar on competition home page
user_name -> kaggle user name
kernel_name -> kernel name to track
frequency -> Seconds in which to check for status of kernel.Triggers notification on status complete.
notify -> Way to notify.[msg/desktop/tone](desktop currenly support only linux and windows)
notify_message -> Message to notify.(Don't include space in message,windows may cause problem,use underscore instead.)
tone_path -> [optional] If tone notifications selected,provide path to tone to play.
result_dir -> [optional] If you want to fetch kernel results,provide where to to store them.
result_to_append -> [optional] From results collected from kernel,if you want some of them to append to one master log file(to store all results across all kernels versions)provide which result file to append to master log.
master_log -> [optional] Single file to store all results across all kernels
```


***Please note that this code is not yet tested,and was created to solve my own problems***

***I am not able to spend time on this so I need a team to test functionalities and add more features.Please drop a mail for any support***

***feedbacks and suggestions always welcome,if facing an issue please raise it***

## To do

```
1.All exceptions handling
2.Generic callbacks support
```
