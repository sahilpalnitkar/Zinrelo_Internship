from UrlRequestData import *
import json
import time
import threading

start_time = time.time()


def url_hit_process_for_conf(url, times_hit):  # Method executes hits to the stored URLS and stores time data values
    # times_hit = 100  # Creates random integer to decide how many times to hit URL
    min_val = 100
    max_val = 0
    avg_count = 1
    avg_val = 0
    while_loop_counter = 0
    print ("Hitting URL %d time(s)" % times_hit)
    while while_loop_counter < times_hit:
        print ("Hit %d" % (while_loop_counter + 1))
        response = requests.post(url)
        time_new = response.elapsed.total_seconds()
        if time_new < min_val:
            min_val = time_new  # Replaces current min value with new time if new time is lesser
        if time_new > max_val:
            max_val = time_new  # Replaces current max value with new time if new time is greater
        avg_val = avg_val + (time_new - avg_val) / avg_count  # Calculates new average value without storing
        avg_count += 1
        while_loop_counter += 1
    url_dict = {'URL': url,  # Creates dict which saves the picked URL, times hit and time data values
                'minimum value': min_val,
                'maximum value': max_val,
                'average value': avg_val,
                'times hit': times_hit}
    f = open("{}_benchmark.txt".format("s3_cloudfront"), "a")
    f.write(json.dumps(url_dict))
    f.write("\n")
    f.close()
    return url_dict  # Returns dictionary to main function


test_url = "http://d3sdpo4zrpd3b.cloudfront.net/b857a8dd91.js"
# test_url = "https://zrlconf1.s3.amazonaws.com/b857a8dd91.js"
# url_hit_process_for_conf(test_url)
print("--- Time taken to execute program was %s seconds ---" % (time.time() - start_time))

t1 = threading.Thread(target=url_hit_process_for_conf, args=[test_url, 100])
t2 = threading.Thread(target=url_hit_process_for_conf, args=[test_url, 150])
t3 = threading.Thread(target=url_hit_process_for_conf, args=[test_url, 200])
t4 = threading.Thread(target=url_hit_process_for_conf, args=[test_url, 250])
# t5 = threading.Thread(target=url_hit_process_for_conf, args=[test_url, 300])
t1.start()
t2.start()
t3.start()
t4.start()
# t5.start()
print("--- Time taken to execute program was %s seconds ---" % (time.time() - start_time))
