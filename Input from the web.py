import urllib.request
file = urllib.request.urlopen('http://helloworldbook3.com/data/message.txt')
message = file.read().decode('utf-8')
print(message)
