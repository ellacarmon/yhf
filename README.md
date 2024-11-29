# YHF Wrapper

A Python wrapper for the Yahoo Finance API.

## Installation

To install the package, use pip:

```bash
pip install yhf-wrapper
```
Usage
Importing the Package
```
from yhf_wrapper import YHFClient
```

Creating a Client
```
client = YHFClient()
```
Fetching Stock Data
```
# Get stock price
price = client.get_stock_price('AAPL')
print(price)

# Get stock sentiment
sentiment = client.get_stock_sentiment('AAPL')
print(sentiment)
```
### Requirements
* Python 3.x
* requests
* numpy
### Installation
To install the required packages, run:
```bash
pip install -r requirements.txt
```
### Author
ellacarmon@gmail.com
### License
This project is licensed under the MIT License - see the LICENSE file for details.

Make sure to replace placeholders like `your_api_key` and `Your Name` with actual values.