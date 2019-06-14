
from UrlRequestData import *
import time

def url_hit_process(url):	 #Method executes hits to the stored URLS and stores time data values
	random_iterator = random.randint(1, 20)		#Creates random integer to decide how many times to hit URL
	min_val = 100
	max_val = 0
	avg_count = 1
	avg_val = 0
	while_loop_counter = 0
	print ("Hitting URL %d time(s)" % random_iterator)
	while while_loop_counter < random_iterator:
		print ("Hit %d" % (while_loop_counter + 1))
		response = requests.post(url)
		time_new = response.elapsed.total_seconds()
		if time_new < min_val:
			min_val = time_new #Replaces current min value with new time if new time is lesser
		if time_new > max_val:
			max_val = time_new #Replaces current max value with new time if new time is greater
		avg_val=  avg_val + (time_new - avg_val)/avg_count #calculates new average vaue without storing
		avg_count += 1
		while_loop_counter +=1
	url_dict = {'URL' : url, #Creates dict which saves the picked URL, times hit and time data vals
				'minumum value' : min_val,
				'maximum value' : max_val,
				'average value' : avg_val,
				'times hit' : random_iterator}
	return url_dict #Returns dictionary to main function
	

#START OF MAIN
start_time = time.time()
url1 = 'https://akshaysandbox4.mybigcommerce.com/'
url2 = 'https://akshaysandbox4.mybigcommerce.com/bath/'
url3 = 'https://akshaysandbox4.mybigcommerce.com/garden/'
url4 = 'https://akshaysandbox4.mybigcommerce.com/kitchen/'
url5 = 'https://akshaysandbox4.mybigcommerce.com/publications/'

choice = input("Enter the page number for which you want the min, max and average response times - ")

if choice == 1:
	
	print(url_hit_process(url1)) #Prints dict returned by function
if choice == 2:
	print(url_hit_process(url2)) #Prints dict returned by function
if choice == 3:
	print(url_hit_process(url3)) #Prints dict returned by function
if choice == 4:
	print(url_hit_process(url4)) #Prints dict returned by function
if choice == 5:
	print(url_hit_process(url5)) #Prints dict returned by function


#ENDS MAIN AND PRINTS TIME TAKE TO EXECUTE ENTIRE PROGRAM
print("--- Time taken to execute program was %s seconds ---" % (time.time() - start_time))