PNRly
=====

##What ?

`PNRly` is a script that enables a user to track their Indian Railways' PNR status and update them if their status changes (For example, when a passenger's reservation status changes from `W/L 10` to `W/L 9` or from `W/L 1` to `S4, 30`/`CNF` etc.)

##How ?
This script requires you to have an account on [FullOnSms.com](http://fullonsms.com).

##Working
To run the software,

* First `download` the tool from the repository (Git Clone/Download ZIP)
* `cd` to the extracted files directory
* `run` the following command in the terminal

>```
$ python ./pnrly.py
```
##Customization
The script checks the PNR status every 15 minutes (900 seconds). To change it, you can change the update frequency by editing the last line of `pnrly.py` script.
>```
  time.sleep(900) #check every 15 minutes
``` 

##Credits
This script uses Indian Railways PNR Enquiry Service  & `sendsms` script by [siddhant3s](https://github.com/siddhant3s/sendsms)

##DISCLAIMER
The author of this script is in no way associated with [Indian Railways](http://www.indianrail.gov.in/) or [FullOnSms](http://fullonsms.com). This script is for personal or educational use only. Any commercial use is forbidden without the conscent of `The Indian Railways` and `FullOnSms`. Author takes no responsibility whatsoever if this script is misused in any way or for any losses incurrred to any individual, company or property either directly or indirectly as a result of using this script. Also, there is no warranty of any kind with this script.
