
from UrlRequestData import *

def url_hit_process(url):
	random_iterator = random.randint(1, 20)
	min_val = 1000
	max_val = 0
	avg_count = 1
	avg_val = 0
	while_loop_counter = 0
	while while_loop_counter < random_iterator +1:
		response = requests.post(url)
		time_new = response.elapsed.total_seconds()
		if time_new < min_val:
			min_val = time_new 
		if time_new > max_val:
			max_val = time_new
		avg_val=  avg_val + (time_new - avg_val)/avg_count
		avg_count += 1
		while_loop_counter +=1
	url_dict = {'URL' : url,
				'minumum value' : min_val,
				'maximum value' : max_val,
				'average value' : avg_val,
				'times hit' : random_iterator}
	print(url_dict)

url1 = 'https://akshaysandbox4.mybigcommerce.com/'
# print("1 done\n")
url2 = 'https://akshaysandbox4.mybigcommerce.com/bath/'
# print("2 done\n")
url3 = 'https://akshaysandbox4.mybigcommerce.com/garden/'
# print("3 done\n")
url4 = 'https://akshaysandbox4.mybigcommerce.com/kitchen/'
# print("4 done\n")
url5 = 'https://akshaysandbox4.mybigcommerce.com/publications/'
# print("5 done\n")
#response = requests.post('https://akshaysandbox4.mybigcommerce.com/')
#print(response.elapsed.total_seconds())
#url1 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/')

#UrlRequestDataList = [url1, url2, url3, url4, url5]

choice = input("Enter the page number for which you want the min, max and average response times - ")
#print(UrlRequestDataList[choice])

if choice == 1:
	url_hit_process(url1)
if choice == 2:
	url_hit_process(url2)
if choice == 3:
	url_hit_process(url3)
if choice == 4:
	url_hit_process(url4)
if choice == 5:
	url_hit_process(url5)