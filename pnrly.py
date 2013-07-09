import urllib
import urllib2
import os
import re
import time

print "+--------------------------------------+"
print "| Indian Railways' PNR Tracker [PNRly] |"
print "+--------------------------------------+"
pnr_number = raw_input("\nEnter PNR Number To Track:  ")

phone_number = raw_input("\nEnter your [FullOnSMS.com] Phone Number:  ")
password = raw_input("\nEnter your [FullOnSMS.com] Password:  ")

#send a test sms
print "\nInitializing & Verifying SMS functionality...\n"
#write sendsms.auth file
s = "[Login]\nusername = "+phone_number+"\npassword = "+password+"\n\n[Phonebook]\n\n[Auth]\nlogindone = http://fullonsms.com/landing_page.php\nloginpage = http://fullonsms.com/login.php\nsms_sent = http://fullonsms.com/MsgSent.php\nsendsms = http://fullonsms.com/home.php\nlogincheck = http://fullonsms.com/login.php\n"
f = open("sendsms.auth",'w')
f.write(s)
f.close()

while True:
	try:
		os.system('./sendsms.py '+phone_number+' "Tracking PNR #'+pnr_number+'" -t ./sendsms.auth')
	except:
		pass
	else:
		break

#continue
print "\nTracking..."

virgin = True #Flag that tells whether or not a status on the PNR number is already obtained. 
past_status = ""

while True:
	url = 'http://www.indianrail.gov.in/cgi_bin/inet_pnrstat_cgi.cgi'
	values = {'lccp_pnrno1' : pnr_number,
		     'submit' : 'Wait+For+PNR+Enquiry%21' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = ''
	while True:
		try:
			response = urllib2.urlopen(req)
		except:
			pass
		else:
			break
			
	the_page = response.read()

	list_entries = ''
	try:
		list_entries = re.findall(r'<TD class="table_border_both"><B>.*?</B></TD>',the_page)
	except:
		print "\nEither something is wrong with your PNR number or IRCTC Servers are busy'\n"
		break
	else:
		pass

	c = 1
	sms_output = ""
	current_status = ""

	#print list_entries
	for i in list_entries:
		i = re.sub(r'<TD class="table_border_both"><B>','',i)
		i = re.sub(r'</B></TD>','',i)
		print i
		if c==1:
			sms_output = sms_output+i
		
		if c==2:
			pass
		if c==3:
			sms_output = sms_output+": "+i+",   "
			current_status = current_status+i+"\n"
			c=0
		c=c+1
	
	if virgin:
		virgin = False
		past_status = current_status
		
	if past_status!=current_status:
		while True:
			try:
				os.system('./sendsms.py '+phone_number+' "PNR #'+pnr_number+' [Status Updated]      '+sms_output[:-4]+'" -t ./sendsms.auth')
			except:
				pass
			else:
				break
		past_status = current_status
		
	time.sleep(900) #check every 15 minutes
	
