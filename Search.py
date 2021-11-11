import webbrowser
print('--Search--')
url = input()
url2 = 'https://www.google.com/search?q='
webbrowser.open("".join([url2, url]))
