# try
# >python test.py 
# if it doesn't work, add the following to the file ~/.bashrc
# export PATH="/usr/local/anaconda3/bin:$PATH"
# (do not include the # character, which is used to mark comments)
# then run
# >source ~/.bashrc

print("\nHello, World!\n")

import sys
print("You are using python version %s.%s.%s." % sys.version_info[:3])
if (sys.version_info.major == 3):
	print("Congratulations, you successfully ran a python3 code!")
else:
	print("Please update your ~/.bashrc to use python3!\n(See instructions in test.py file.)")

