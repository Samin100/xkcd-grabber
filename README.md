# Introduction
This is a Python based web scraper that downloads xkcd comics and stores it in the xkcd-grabber directory. The xkcd site offers a JSON interface so scraping the HTML web page for the image is not the most relaible and efficient method however this scraper was developed as a practice and reference for future web scraping programs.

# Getting Started
Simply run xkcd-grabber.py and it will begin downloading xkcd comics into the same directory. It stores a list of comics numbers that cannot be downloaded due to them being interactive comics or in the case of http://xkcd.com/404 a 404 error page. xkcd-grabber will begin to download starting at comic 1 until the most recent comic. To edit the starting comic, change ```currentComic = 1``` to whatever comic number you want. 

# Enjoy
