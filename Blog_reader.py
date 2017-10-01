from bs4 import BeautifulSoup
import requests
import shutil
page = requests.get("http://planet.dgplug.org/")
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all(class_="entrygroup")
columns = shutil.get_terminal_size().columns
size = len(data)-1
for i in range(0, size):
    piu = data[i]
    heading = piu.find("a").get_text()
    for n in range(84):
        print ("-", end=" ")
    print ('{}{}'.format(' ' * (int(columns / 2 - len(heading) / 2)), heading))
    for n in range(84):
        print ("-", end=" ")
    main_content = piu.find(class_="content").get_text()
    print (main_content)
