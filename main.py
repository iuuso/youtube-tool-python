#!/usr/bin/python
import os
import urllib
import simplejson

#Variables
browser = "/usr/bin/firefox --new-window "
url = input("Please give me an URL: ")

def main(): # Main function where the magic happens
	print("I'm in the main!")
	urlParser()
	browserPrompt()
	print("Happy viewing!")
	tempFunction()


def urlParser(arg=url): # Function for parsing the given URL
	str(url)
	parted = url.partition("watch?v=")
	fullscreenVersion = "http://youtube.com/v/" + parted[2]
	return fullscreenVersion


def browserPrompt(): # Promp the user whether to open a browser instance
	choice = input("Do you want to open this url in new firefox\ninstance? (y/n)")
	if (choice=="y"):
		os.system(browser + urlParser())
		print("Opening browser...")
	if (choice=="n"):
		print("\n***********************")
		print("** URL: " + urlParser() + "**")
		print("\n***********************")

	else:
		print("Sorry, I don't understand what you're trying to say.")

def tempFunction():

	id = 'KQEOBZLx-Z8'
	url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id

	json = simplejson.load(urllib.urlopen(url))

	title = json['entry']['title']['$t']
	author = json['entry']['author'][0]['name']

	print("id:%s\nauthor:%s\ntitle:%s" % (id, author, title))

# End functions

if __name__ == '__main__':
    main()

#http://www.youtube.com/watch?v=ddsz9XBhrYA
