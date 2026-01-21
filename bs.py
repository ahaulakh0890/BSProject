from bs4 import BeautifulSoup   
import requests 

website = "https://subslikescript.com/movie/Titanic-120338"

response = requests.get(website)

content = response.text 

soup = BeautifulSoup(content, 'html.parser')  

titles = soup.find_all('p', class_="cue-line") 
for title in titles:
    print(title.get_text()) 

print("The whole script is printed above")    
# i = 0  
# for title in titles:
#     print(title.get_text())
#     i += 1  

# print(f"{i} titles are printed above")
# print(soup.prettify())  