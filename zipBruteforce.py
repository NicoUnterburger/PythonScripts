import zipfile
import itertools
import string
from threading import Thread

zipfile = "file/location"
myLetters = string.ascii_letters + string.digits
zipfile1 = zipfile.ZipFile(zipfile)

def crack(zip, pwd):
	try:
	  zip.extractall(pwd=str.encode(pwd))
	  print(pwd)
	except:
	  pass

for i in range(3, 10):
  for j in map(''.join, itertools.product('myLetters', repeat=i)):
    t = Thread(target=crack, args=(zipfile1, j))
    t.start()
