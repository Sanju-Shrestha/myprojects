Transfer Market Tracker

src/data_collection.py 

* ~~Tried using BeautifulSoup but unable to collect data as desired. Changed the approach by using Selenium since the website is dynamic. The second commit is for single league data extraction only.~~
* Using both Selenium and BeautifulSoup4 helped to optimized the collection process.

src/data_collection_final.py

* Identified an issue with the collected dataset. There is no suffiecient features of the postions like Goalkeeper, Defense and Midfield. But the code above is applicable to extract the respective data.

* Different csv files for different dataset will be collected (Example: data_raw_goalkeeper, data_raw_midfield).

