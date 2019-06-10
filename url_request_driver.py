
from UrlRequestData import *

# url1 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/')
# print("1 done\n")
# url2 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/bath/')
# print("2 done\n")
# url3 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/garden/')
# print("3 done\n")
# url4 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/kitchen/')
# print("4 done\n")
# url5 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/publications/')
# print("5 done\n")
response = requests.post('https://akshaysandbox4.mybigcommerce.com/')
print(response.elapsed.total_seconds())
url1 = UrlRequestData('https://akshaysandbox4.mybigcommerce.com/')

#UrlRequestDataList = [url1, url2, url3, url4, url5]

choice = input("Enter the page number for which you want the min, max and average response times - ")
#print(UrlRequestDataList[choice])
