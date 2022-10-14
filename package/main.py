import sys
##sys.path.append(r'C:\Users\balli\.ebcli-virtual-env\Lib\site-packages')
sys.path.append(r'\requests')

import requests;


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
