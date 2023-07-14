import urllib.request
url = "https://rusbiathlon.ru/shop/id2752825/ty-molodyets-pozdravityelnaya-otkrytka_postcard_a6/"
img = urllib.request.urlopen(url).read()
out = open("img.jpg", "wb")
out.write(img)
out.close()