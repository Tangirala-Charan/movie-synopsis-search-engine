import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
serv_obj = Service('D:\driveers\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.imdb.com/list/ls048276758/?st_dt=&mode=detail&page=1&sort=list_order,asc")
time.sleep(2)
file=open('D:\\datasetir\\synopsis.text','x')

li = []
movie_list=set()
synopsis=[]
d_movies=[]
actor_names=[]
actor_links=[]
d_movie_link=[]
actor_movie_links=[]
actor_movies=[]

for i in range(2,6):

    s = (driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div[4]/div[3]/div[{i}]/div[2]/h3/a'))
    for j in s:
        # movie.append(j.text)
        li.append(j.get_attribute('href'))

print(li)
#
i = 0

director = []
actl=[]
dcl=[]
mvl=[]
director_movie_links=[]
actor_movie_links=[]
df=0

while (i!= 1000):
    time.sleep(2)

    driver.get(li[i])

    s=(driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]'))


    for ii in s:
        synopsis.append(ii.text)
        file.write(str(i) + '\n' +ii.text + '\n')

    # --------------extract directors name----------------------

    driver.get(li[i])
    time.sleep(2)
    zy= driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]')

    for j in zy:


        director.append(j.text)
        file.write( j.text + '\n')
        time.sleep(2)


    #----for directors link------



    ii=driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a')
    for kl in ii:
        dcl.append(kl.get_attribute('href'))
    print('dcl',dcl)

    driver.get(dcl[i])
    for ii in range(1,5):
        p=driver.find_elements(By.XPATH, f'/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/div[3]/section[2]/div[5]/div/div/div[4]/div/ul/li[{ii}]/div[2]/div[1]/a')
        for kk in p:
            d_movies.append(kk.text)
            d_movie_link.append(kk.get_attribute('href'))


    print(d_movie_link,'d_movie_link')
    print(d_movies,'d_movies')

    driver.get(li[i])

   #for the actor name,actor movies ,actor links

    for k in range(1, 3):

        p = driver.find_elements(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[{k}]/a')
        for j in p:
            actor_names.append(j.text)
            file.write(j.text + " ")
            actor_links.append(j.get_attribute("href"))
        file.write("\n")
    print(actor_names,'actor_names')
    print(actor_links,'actor_links')


    for ii in range(0,2):
        driver.get(actor_links[ii])
        for j in range(1,5):

            p=driver.find_elements(By.XPATH, f'/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/div[3]/section[2]/div[5]/div/div/div[4]/div/ul/li[{j}]/div[2]/div[1]/a')
            for kk in p:
                actor_movie_links.append(kk.get_attribute('href'))


            for kkk in p:
                actor_movies.append(kkk.text)

    print(actor_movie_links,'actor_movie_links')
    print(actor_movies,'actor_movies')







    print('li',li)
    for ii in range(0,len(d_movie_link)):
        li.append(d_movie_link[ii])
    for j in range(0,len(actor_movie_links)):
        li.append(actor_movie_links[j])



    print('li',li)
    i = i + 1


    print("director", director)

    print('synopsis',synopsis)



