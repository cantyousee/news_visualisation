import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


df = pd.read_csv('file_name',  delimiter = ',',   error_bad_lines=False, encoding="utf-8-sig")


cities = df['city'].tolist()
articles = df['source'].tolist()
articles_set = list(set(articles))
cities_set = list(set(cities))


c = Counter(articles)
most_articles_source = c.most_common(5)


source = []
for i in most_articles_source:
  print(i[0])
  #source.append(i[0])
  
  

check = 0
city_one = ""
article_limit = 0
while check != 1:
  city_one = input('Enter a city name: ')
  for z in cities_set:
    if city_one == z:
      check = 1


print(cities_set)
print(articles_set)

city_source_count = []
temp_string = ""
#source = []
city_count = []
cities_set = []
cities_set.append(city_one)
print(len(articles_set))
articles_count = 0



for i in range(len(most_articles_source)):
  print(articles_count)
  if articles_count == 5:
    break
  articles_count = articles_count + 1
  for j in range(len(cities_set)):
    count = 0
    for z in range(len(articles)):
      if most_articles_source[i][0] == articles[z] and cities_set[j] == cities[z]:
        count = count + 1
        #temp_string = str(articles_set[i]) + str(cities_set[j]) + str(count)
      
    #city_source_count.append(temp_string)
    source.append(most_articles_source[i][0])
    city_count.append(count)


for i in range(len(articles_set)):
  print(articles_count)
  if articles_count == 10:
    break
  articles_count = articles_count + 1
  for j in range(len(cities_set)):
    count = 0
    for z in range(len(articles)):
      if articles_set[i] == articles[z] and cities_set[j] == cities[z]:
        count = count + 1
        #temp_string = str(articles_set[i]) + str(cities_set[j]) + str(count)
      
    #city_source_count.append(temp_string)
    source.append(articles_set[i])
    city_count.append(count)
      
      
for z in range(len(source)):
  print(source[z], city_count[z])#source city city_count



s = [10*n for n in city_count]

plt.scatter(source, city_count, s = s, color = 'g', alpha = 0.75)
str1 = "Number of times a News org has reported on " + city_one
plt.title(str1)
plt.xlabel('Sources')
str1 = 'Reported count of '+ city_one
plt.ylabel(str1)
plt.show()
