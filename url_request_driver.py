import time
from url_hit_process import *
	

# START OF MAIN
start_time = time.time()
url1 = 'https://akshaysandbox4.mybigcommerce.com/'
url2 = 'https://akshaysandbox4.mybigcommerce.com/bath/'
url3 = 'https://akshaysandbox4.mybigcommerce.com/garden/'
url4 = 'https://akshaysandbox4.mybigcommerce.com/kitchen/'
url5 = 'https://akshaysandbox4.mybigcommerce.com/publications/'

choice = input("Enter the page number 1-5 for which you want the min, max and average response times - ")

if choice == 1:
	print(url_hit_process(url1))  # Prints dict returned by function
elif choice == 2:
	print(url_hit_process(url2))  # Prints dict returned by function
elif choice == 3:
	print(url_hit_process(url3))  # Prints dict returned by function
elif choice == 4:
	print(url_hit_process(url4))  # Prints dict returned by function
elif choice == 5:
	print(url_hit_process(url5))  # Prints dict returned by function
else:
	print("Invalid URL choice")

# ENDS MAIN AND PRINTS TIME TAKE TO EXECUTE ENTIRE PROGRAM
print("--- Time taken to execute program was %s seconds ---" % (time.time() - start_time))
