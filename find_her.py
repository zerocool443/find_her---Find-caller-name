import requests
from bs4 import BeautifulSoup
import time
number_start = int(raw_input("Provide the starting range"))
number_end = int(raw_input("Provide the ending range"))

for i in range(number_start,number_end+1):
		time.sleep(1)
		r = requests.post("https://xtremetricks.net/truecaller/truecall.php", data={'number': i})
		soup=BeautifulSoup(r.text,"html.parser")
		divs=soup.findAll("div",{"class":"user-heading"})
		soup2=BeautifulSoup(str(divs),"html.parser")
		name=str(soup2.find('h2'))
		print(name[4:-5])
		print(':')
		print(i)
		print('---------------------------------- \n \n')



