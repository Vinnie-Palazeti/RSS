import argparse
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from RSS.pullers import *

def main():
	foos = {
	  'Funcs': [newyorker() + washpost_politics() + washpost_opinions() + washpost_sports()],
	  'Alias' : ["New Yorker", "Washington Post Politics", "Washington Post Opinions", "Washington Post Sports"]
	}

	out = foos['Funcs'][0]
	out = sorted(out,  key=lambda x: datetime.strptime(x[0], '%A, %d %b %Y'),reverse=False)
	out = [i for i in out if i[0] == datetime.now().strftime('%A, %d %b %Y') or i[0] == (datetime.now()- timedelta(days=1)).strftime('%A, %d %b %Y')]
	for j in range(len(out)):
	  if out[j][3] == "N/A":
	    continue
	  print()
	  print(f"title: {out[j][1]}")
	  print(f"author: {out[j][2]}")
	  print(f"{out[j][3]}")
	  print('---')



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main()
