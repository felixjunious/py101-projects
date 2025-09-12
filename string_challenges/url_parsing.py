url = input('Enter URL : ')

protocol = url[:url.index('://')]
domain = url[url.index('www.')+4:url.index('.com')]
page = url[url.index('.com')+4:]

print('Protocol ' + protocol)
print('Domain ' + domain)
print('Page ' + page)

# Test URL : https://www.kaggle.com/datasets
# Test URL : http://www.google.com/search