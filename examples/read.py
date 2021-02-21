import argparse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from RSS.pullers import *

def main():
	print("What would you like to read?")

	for i in range(len(foos['Num'])):
  		print(f'{foos["Num"][i]}: {foos["Alias"][i]}')


	out = []
	x = input()
	for i in x:
	  out = out + foos['Funcs'][i-1]
	  
	out = sorted(out,  key=lambda x: datetime.strptime(x[0], '%A, %d %b %Y'),reverse=True)
	out = [i for i in out if i[0] == datetime.now().strftime('%A, %d %b %Y') or i[0] == (datetime.now()- timedelta(days=1)).strftime('%A, %d %b %Y')]

	for j in range(len(out)):
	  if out[j][3] == "N/A":
	    continue
	  print()
	  print(f"title: {out[j][1]}")
	  print(f"author: {out[j][2]}")
	  print(f"link: {out[j][3]}")
	  print('---')




if __name__ == "__main__":

    parser = argparser.ArgumentParser()
    args = parser.parse_args()

    main()
