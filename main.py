import os
import urllib
import urllib2
import string
import re

def getFile(url):
	content = urllib2.urlopen(url).read()
	reg = r'href="(http://.{0,300}?\.mp3)"'
	file_link = re.compile(reg)
	file_list = file_link.findall(content)

	if not os.path.exists('collection'):
		os.mkdir('collection')

	os.chdir(os.path.join(os.getcwd(), 'collection'))

	for file in file_list:
		# file in file_list now is url string: http://.../...mp3
		# obtain file name from this string
		file_name = str(file).split('/')[-1]
		# handle the file-like object
		u = urllib2.urlopen(file)
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		# print file name and its size
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		# define downloaded file size
		file_size_dl = 0
		# define block size reading in buffer
		block_sz = 1024*1024

		# open a file for writing only in binary format
		f = open(file_name, 'wb')

		# while true write buffer to file and show downloading status bar
		while True:
			# read file in buffer
			buffer = u.read(block_sz)
			# if buffer is NULL then break
			if not buffer:
				break
			# calculate downloading file size
			file_size_dl += len(buffer)
			# write buffer to file
			f.write(buffer)
			# this is downloading status bar
			status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl*100.0/file_size)
			# ASCII code "8" is Backspace
			status = status + chr(8)*(len(status)+1)
			# with "," Newline was replaced by Space
			print status,
		print chr(8)
		# don't forget to close file
		f.close()

if __name__ == '__main__':
	url = 'http://www.theskepticsguide.org/podcast/sgu'
	getFile(url)