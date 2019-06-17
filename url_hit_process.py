from UrlRequestData import *


def url_hit_process(url):  # Method executes hits to the stored URLS and stores time data values
    random_iterator = random.randint(1, 20)  # Creates random integer to decide how many times to hit URL
    min_val = 200
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
            min_val = time_new  # Replaces current min value with new time if new time is lesser
        if time_new > max_val:
            max_val = time_new  # Replaces current max value with new time if new time is greater
        avg_val = avg_val + (time_new - avg_val) / avg_count  # Calculates new average value without storing
        avg_count += 1
        while_loop_counter += 1
    url_dict = {'URL': url,  # Creates dict which saves the picked URL, times hit and time data vals
                'minimum value': min_val,
                'maximum value': max_val,
                'average value': avg_val,
                'times hit': random_iterator}
    return url_dict  # Returns dictionary to main function
