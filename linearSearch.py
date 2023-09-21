def count_elements_linear(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
    return count

arr = 4,2,5,6,1,3,44,66,221,45,5,5,5
element = 5
print(count_elements_linear(arr, element) )

import psutil
import logging

# Configure the logging module
logging.basicConfig(
    filename='psutil_stats.log',  # Specify the log file name
    level=logging.INFO,          # Set the logging level to INFO
    format='%(asctime)s [%(levelname)s]: %(message)s',  # Define log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define date and time format
)

# Define a function to log CPU and memory usage
def log_cpu_memory_usage():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    logging.info(f'CPU Usage: {cpu_percent}% - Memory Usage: {memory_percent}%')

# Run the logging function periodically
while True:
    log_cpu_memory_usage()
