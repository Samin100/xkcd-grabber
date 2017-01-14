'''
xkcd-grabber downloads xkcd comics as a .jpg with their comic # and native name from http://xkcd.com.

By default the first comic will be '1' however you can specify which comic to start from
by changing 'currentComic'.

Some comics cannot be downloaded due to them being interactive, these comic numbers are stored
in the 'skipThese'. 404 is skipped due to http://xkcd.com/404 being an error page.

WARNING: Be sure this script is in a directory you want the files to be in before you run,
as it will populate the current directory with hundreds of xkcd comics.
'''


import bs4
import requests
import time


currentComic = 1
skipThese = [404, 1350, 1416, 1525, 1608, 1663]
skipThese = []

downloadCount = 0
failedDownloads = []


start = time.time()
print('Scraping has begun...')
while True:

    if currentComic in skipThese:
        currentComic += 1
        continue

    pageURL = 'http://xkcd.com/' + str(currentComic)
    page = requests.get(pageURL)

    try:
        page.raise_for_status()

    except requests.exceptions.HTTPError:  # no more comics
        break

    soup = bs4.BeautifulSoup(page.text, 'lxml')


    try:
        # parses to retrieve the comic image URL
        imageSoup = soup.select('#comic img')
        comicURL = imageSoup[0].get('src')
        comicURL = 'http://' + comicURL[2:]

        # parses to retrieve the comic title
        titleSoup = soup.select('div #ctitle')
        title = titleSoup[0].contents
    except IndexError:
        print('Could not process xkcd #' + str(currentComic))
        failedDownloads.append(currentComic)
        currentComic += 1
        continue

    if len(title) > 1:  # some comic titles contain special formatting, ex: #472
        newTitle = title[0].contents[0] + title[1]
        title = newTitle
    else:
        title = title[0]

    title = str(currentComic) + ' - ' + title
    title += '.jpg'

    title = title.replace('/', ':')  # replaces forward slashes with colons which appear as forward slashes in UNIX

    # writes the title and image to a file
    print('Processing ' + title)
    comicImage = requests.get(comicURL)
    comicFile = open(title, 'wb')
    comicFile.write(comicImage.content)
    currentComic += 1


end = time.time()
print('Scraping complete. Downloaded ' + str(downloadCount) + ' comics.')
print('Elapsed time: ' + str(end - start)[:6] + ' seconds')

if len(failedDownloads) > 0:
    for failure in failedDownloads:
        print('Comic #' + str(failure) + ' failed.')
