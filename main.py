
from crawler import topicUrlCrawlerThread
from crawler import topicHtmlCrawlerThread
from crawler import topicHtmlToContentProcess
from crawler import serviceInit

from os import listdir

import argparse

def main(args):

	path_forum   = "database/{}/forum.csv".format(args.dataset)
	path_url     = "database/{}/url".format(args.dataset)
	path_html    = "database/{}/html".format(args.dataset)
	path_content = "database/{}/content".format(args.dataset)

	serviceInit("database/{}".format(args.dataset))

	if args.url:

		topicUrlCrawlerThread(path_forum, path_url)

	if args.html:

		topicHtmlCrawlerThread(path_url, path_html, path_content, num_workers = 8)

	if args.content:

		topicHtmlToContentProcess(path_html, path_content, num_workers = 4)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("dataset", type = str)

	parser.add_argument("--url", 
		default = False, action = "store_true")
	parser.add_argument("--html", 
		default = False, action = "store_true")
	parser.add_argument("--content", 
		default = False, action = "store_true")

	args = parser.parse_args()

	main(args)
