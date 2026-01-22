from bs4 import BeautifulSoup   
import requests 

website = "https://subslikescript.com/movies"

response = requests.get(website)

content = response.text 

soup = BeautifulSoup(content, 'html.parser')  

box = soup.find('article', class_="main-article")   

link_section = box.find_all('a', href=True)

links = []

for link in link_section:
    links.append(link['href'])

print("The links are being printed below:")

for link in links:
    print("https://subslikescript.com" + link)


print("\n")
print("The links are printed successfully")

# titles = soup.find_all('p', class_="cue-line") 
# # for title in titles:
# #     print(title.get_text()) 

# print("The whole script is printed above")   

# with open("titanic_script.txt", "w", encoding='utf-8') as f:
#     for title in titles:
#         f.write(title.get_text() + "\n")


# i = 0  
# for title in titles:
#     print(title.get_text())
#     i += 1  

# print(f"{i} titles are printed above")
# print(soup.prettify())  