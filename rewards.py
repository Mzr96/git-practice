import webbrowser
import time
import os

string=input('give the string:')

bing='https://www.bing.com/search?q='

list_of_string=string.split()
print(list_of_string)


for word in list_of_string:
    if bing[-1]!='=':
        bing=bing+'+'+word
    else :
        bing=bing+word

counter=len(string.replace(' ',''))
print('counter is:',counter)

while counter>=0:
    
    webbrowser.open_new_tab(bing)
    bing=bing[:-1]
    counter-=1
    time.sleep(5.0)
    os.system('TASKKILL /F /IM chrome.exe')
    
'adding some comments for practicing git'
'good morning for git test'
'what happen to diff command'