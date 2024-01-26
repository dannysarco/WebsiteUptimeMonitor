import requests
import time

urls = [
    "http://savethehumans.ai",
    "https://savethehumans.ai",
    "http://www.savethehumans.ai",
    "https://www.savethehumans.ai",
]

timeout_seconds = 10  
log_file = "website_monitoring_log.txt"  

while True:
    with open(log_file, "a") as file:
        for url in urls:
            try:
                response = requests.get(url, timeout=timeout_seconds)
                log_message = f"Time: {time.ctime()}, URL: {url}, Status Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()} seconds\n"
                print(log_message, end='')
                file.write(log_message)
            except requests.exceptions.RequestException as e:
                log_message = f"Time: {time.ctime()}, URL: {url}, Website is down or unreachable. Error: {e}\n"
                print(log_message, end='')
                file.write(log_message)

    time.sleep(300)  
