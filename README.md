# asg_web_trawling

For Crawling:
Head to http://webby-crawler.herokuapp.com
Please use http instead of https, as I do not have an SSL cert

Expand Web Crawler expander bar
Select Forensic Science International
Disregard Operating System
Enter the username email for FSI
Enter password for FSI
Number of pages to crawl (e.g. 3)
Enter Number of volumes to crawl (e.g. 10)

Note>> Number of volumes will supersede number of pages. 
For example in 2 pages, there may be 40 volumes, but if volumes is specify at 10, the web crawling will end at 10 volumes. 

Once crawling has been completed, the web app will print a "Completed" line. 


Download crawl results: 
Open Generate Link expander
Click the link to download all the crawled resutls in CSV format.


Same as previous, please indicate an 'X' in the download column of the CSV to indicate which to download. 

Download "download_journal-v3-windows.py" to your local machine
Execute the file using command line >> python download_journal-v3-windows.py 
>>Please refer to guide provided previously on how to navigate and execute script
>>First prompt will ask you to select your chromedriver, the next window to select the csv file, typing y to login, key in username and password.
>>Please ensure that a folder named "asg_idl" is created on your desktop for it to work correctly. 
