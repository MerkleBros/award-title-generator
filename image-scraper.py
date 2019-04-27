import json, os
import wget
import configparser

Config = configparser.ConfigParser()
Config.read("./image-scraper.cfg")
client_id = Config.get("unsplash_api","CLIENT_ID")

### Unsplash has a limit of 30 counts for random photos. 
### We iterate this for 5 times to get enough photos scraped.
for i in range(5):
    output_directory = "./Images%i"%(i)
    os.mkdir(output_directory)
    jsonfilename = wget.download("https://api.unsplash.com/photos/random?count=30&client_id=%s"%client_id, out=output_directory)

    with open(jsonfilename) as json_file:
        data = json.load(json_file)
        for image in data:
            url = image["urls"]["raw"]
            wget.download(url, out=output_directory)