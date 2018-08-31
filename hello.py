#! /usr/bin/python3


import pyperclip,sys

password={'account1':'"password1',
           'account2':'password2',
	   'account3':'password3',
	   'account4':'password4',
	   'account5':'password5',
	   'account6':'password6',
	   'account7':'password7',
	   'account8':'password8'
          }

if sys.argv[1] and sys.argv[1] in password.keys() :
	pwd=password[sys.argv[1]]
	pyperclip.copy(pwd)
	print('password copied suucesfully')
else:
	print('please provide valid accoutn')
	print('Do you need to add the new account')
	res=input()
	if(res):
		newacc=input('Enter the new account')
		newpwd=input('Enter new password')
		password[newacc]=newpwd
		print('New account added')

