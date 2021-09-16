import argparse
import urllib.request
import csv
import re

def downloadData(url):
    request = urllib.request.urlopen(url)
    data = request.read().decode('utf-8')
    return data

def processImages(data):
    lines = 0
    jpg = 0
    gif = 0
    png = 0

    for row in data:
        lines = lines + 1
        if re.search(r".jpg", row[0]):
            jpg += 1

        elif re.search(r".gif", row[0]):
            gif += 1

        elif re.search(r".png", row[0]):
            png += 1

            
    return jpg + gif + png
    print('Image requests account for {(jpg+gif+png/lines)*100} of all requests')
    

def processBrowsers(data):
    ff = 0
    chrome = 0
    ie = 0
    safari = 0
    for row in data:
        if re.search(r"Firefox", row[2], re.IGNORECASE):
            ff += 1
        if re.search(r"Chrome", row[2], re.IGNORECASE):
            chrome += 1
        if re.search(r"Trident", row[2], re.IGNORECASE):
            ie += 1
        if re.search(r"AppleWebkit", row[2], re.IGNORECASE):
            safari += 1

    return max(ff, chrome, ie, safari)

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
