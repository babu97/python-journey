# import pprint
# from datetime import datetime

# def convert2ampm(time24:str) -> str:
#     return datetime.strptime(time24, '%H:%M'). strftime('%I,%M%P')
# flights = {}
# with open('buzzers.csv') as data:
#     ignore = data.readline() # ignore the first line
#     for line in data:
#         k, v = line.strip().split(',')
#         flights[k] = v



# fts = {convert2ampm(k): v.title() for k,v in flights.items() }

# westy =[k for k,v in fts.items() if v =='West End']

# when = {}
# for des in set(fts.values()):
#     when [des]  = [k for k,v  in fts.items() if  v == des] 

# when2 = {des: [k for k,v in fts.items()]  for des in set(fts.values())}

# # pprint.pprint(when)
# pprint.pprint(when2)




# vowels  = {'a','e', 'i', 'o', 'u'}
# message = "Don't forget to pack our towel"

# found  = set()

# for v in vowels:
#     if v in message:
#         found.add(v)
# print (found)

# found2  = {v for v in message if v in message}
# print(found)

import requests
urls = ('http://headfirstlabs.com', 'https://oreilly.com', 'https://twitter.com')

# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code,'->', resp.url )

for url in urls:
    if resp in requests.get(url):
            print(len(resp.content), '->', resp.status_code,'->', resp.url )
