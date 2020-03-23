from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://www.gssoc.tech/projects.html')
element = driver.find_elements_by_css_selector('.gs-project-name a')
links = [str(elem.get_attribute('href')) for elem in element]
p = open('gssoc20_projects', 'w')
for link in links:
    p.write(link)
    p.write('\n')
p.close()
driver.close()