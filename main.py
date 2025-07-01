from selenium import webdriver


drive = webdriver.Chrome()


drive.get('https://www.google.com/?hl=pt-BR')


print(drive.title)

print(drive.current_url)


print(drive.get_window_rect())


print(drive.name)


#print(drive.page_source)

#from Ipython.display import HTML


#HTML(drive.page_source)

prit (drive.get(''))


print(drive.back())


print (drive.forward())

drive.close() #aba


drive.quit() #ALL


