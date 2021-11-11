import webbrowser

url1 = 'https://www.google.com/search?q='
url2 = 'https://www.youtube.com/results?search_query='
url3 = 'https://duckduckgo.com/?q='
S = '0'
#variables that we need

print('Where do you want to search')
print('Type 0 to check out my Github')
print('(1 = Google, 2 = Youtube, 3 = DuckDuckGo)')
S = input()

if S == '0':
    webbrowser.open('https://github.com/QuickPlayz')
    quit() #github

if S == '1' :
    print('What do you want to look up')
    S1 = input() 
    webbrowser.open("".join([url1, S1 ]))
    quit() #google

if S == '2' :
    print('What do you want to look up')
    S2 = input() 
    webbrowser.open("".join([url2, S2 ]))
    quit() #youtube

if S == '3' :
    print('What do you want to look up')
    S3 = input() 
    webbrowser.open("".join([url3, S3 ]))
    quit() #duckduckgo
