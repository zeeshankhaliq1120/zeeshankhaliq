#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:20:52 2021

@author: zeeshankhaliq
"""

import json
import requests
import time

#1 Grab a list of quotes to get form Yahoo



apikey='XwcUYqT8pN2tLSyt3lrw66bJU2T3TP6L2TFenIW2'


url = "https://yfapi.net/v6/finance/quote"
querystring = {"symbols":"FB"}
headers = {
  'x-api-key': apikey
   }

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)

response.raise_for_status()  # raises exception when not a 2xx response
#if response.status_code != 204:
stock_json = response.json()
timestamp = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
FB = stock_json['quoteResponse']['result'][0]["displayName"] + ", " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp)) + ", $" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])

import csv
with open('FBstockdata.csv', mode = 'a') as FBstockdata:
    FBstock_writer = csv.writer(FBstockdata, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    FBstock_writer.writerow(FB)