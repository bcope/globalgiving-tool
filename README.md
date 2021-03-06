# Global Giving Scraper and Crawler Tool



## Problem
Currently, GlobalGiving connects with organizations based in the US along with some nonprofits in other countries. However, the process of finding and applying to GlobalGiving remains significantly easier within the United States. In certain countries, factors including lack of internet connectivity and lack of access to documents required by GlobalGiving has led to slower onboarding and discovery of the organization. 

## Solution 

### Scraping directories of nonprofits

We identified 8 different directories of nonprofits, scraping each one and gathering as much information as possible from the website. We placed each scraper in its own microservice, creating a universal API to interact with all the nonprofits. 

Through the command line tool you can get a list of the registered scrapers, run the scrapers, and fetch the logs of the run.

### Crawling for potential sources 
 
We wanted to create a crawler in which you can search for potential directories of nonprofits so you know the one's to scrape. To rank the list of nonprofits, we are currently using heuristics such as the number of subpages, number of nonprofits that match ones we have already found, and finding repeated structures on the webpage. 

### Architecture

![GitHub Logo](/resources/architecture.png)


# Setup

## Installation

```
cd globalgiving 
pip3 install -r requirements.txt
cd ..
pip3 install --editable .
globalgiving -h
```

## Command Line Tool

* **globalgiving list** 
Lists all the scrapers availible


* **globalgiving routes <scrape_name>** 
Lists all the routes available for that scraper
    * Example: globalgiving routes vietnam

* **globalgiving register <scrape_name> <scrape_url>** 
Register that scraper url with a given name, or will update that scraper
    * Example: globalgiving register vietnam https://gg-scraper-viet.now.sh


* **globalgiving delete <scrape_name>** 
Removes that scraper from the list of scrapers in the database
    * Example: globalgiving delete vietnam 


* **globalgiving test <scrape_name>** 
Uses the test endpoint to give you an example of what the data looks like
    * Example: globalgiving delete vietnam 

* **globalgiving run <scrape_name>** 
Runs the scraper on the entire directory and adds all the nonprofits to the database
    * Example: globalgiving run australia

* **globalgiving log --scraper_name <scrape_name>** 
Gets a list of all uploaded logs from every run of the scraper
    * Example: globalgiving run australia

* **globalgiving log --scraper_name <scraper_name > --filename <file name> --output_filename <output file name>** 
Downloads the log file locally with the name specified as the output file. 
    * Example: globalgiving log --scraper_name australia --filename
008deece-bcf7-4bff-90eb-9566e401e84e.txt --output_filename out_log.txt    


## Adding a new microservice

* **globalgiving generate <scraper_name>** 
This will generate the scraper in the microservices folder with everything autogenerated. Then navigate to ```microservices/scraper-<scraper_name>/app/scraper.py``` and modify it to scrape the website you specified. 


## Contributing Guidelines

### Unit Testing
When new web scrapers or any new feature is added, unit testing must be done to ensure code functionality. All of the test files will be stored in the `tests` directory within your own microservice directory and will be run using the `pytest` python module. CircleCI will be running the test cases and they will be checked prior to merging.

In order for unittest to recognize and run tests, each method in the class should start with the pattern `test_`. The methods `setUp()` and `tearDown()` can also be used to set up the environment prior to testing. After all of the test cases have been written, they can all be run using `pytest`, which will find and run all tests that have the specified pattern in files in the current directory and any subdirectories.






