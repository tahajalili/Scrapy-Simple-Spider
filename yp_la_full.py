import requests
from bs4 import BeautifulSoup as bs

page = 1

while True:
	if page == 1:
		url = 'https://www.yellowpages.com/search?search_terms=coffee%20&geo_location_terms=Los%20Angeles%2C%20CA&page=1'
	else:
		url =  'https://www.yellowpages.com/search?search_terms=coffee%20&geo_location_terms=Los%20Angeles%2C%20CA&page={}'.format(page)
	
	r = requests.get(url)
	soup = bs(r.content,'html.parser')
	cafe_info = soup.find_all('div',attrs={"class":"info"})


	with open("name_la_full.txt",'a') as f:
		for i in cafe_info:
			# if name.text !='Home' and name.text !='Los Angeles, CA':
			try:
				f.write(i.find('span',attrs={"itemprop":"name"}).text.ljust(30,'-')+i.find('span',attrs={"class":"street-address"}).text.ljust(30,'-')+'  Phone: '+i.find('div',attrs={"class":"phones phone primary"}).text+'\n')
			except AttributeError:
				pass 
	if soup.find('a',attrs={"class":"next ajax-page"}) is None:
		break
	page += 1
print('done')

	

