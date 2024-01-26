# Website Uptime Monitor

## Description
This Python script monitors the uptime and response times of different URL formats (HTTP/HTTPS, with/without 'www') for a specific website. It logs the availability and performance data, aiding in diagnosing connectivity and performance issues.

## Features
- Monitors multiple URL formats
- Checks both HTTP and HTTPS protocols
- Logs response times and status codes
- Configurable for different websites and intervals

## Usage
1. Modify the `urls` list in the script to include the URLs you want to monitor.
2. Set the `timeout_seconds` as per your requirement.
3. Run the script locally, or deploy it on a server or cloud function.

## Requirements
- Python 3
- `requests` library

## Installation
1. Clone the repository.
2. Install dependencies: `pip install requests`
3. Run the script: `main.py`

## Contributing
Feel free to fork this repository and submit pull requests or suggest improvements via issues.
