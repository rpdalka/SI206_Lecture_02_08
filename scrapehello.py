#scrapehello.py

from bs4 import BeautifulSoup

printHTML = False # Set True if want to print entire html document
printLectureEx = False # Set True if want to print examples from lecture
printExcercise = True # Set True if want to print lecture excercies

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

if printHTML:
    print(soup.prettify())


# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')

if printLectureEx:
	print('list items:', all_list_items)
	print('------')
	print('divs:', all_divs)
	print('------')
	print('goodbye elements:', all_goodbye_elements)
	print('------')
	print('french stuff:', all_french_list_items)
	print('------')
	print('hello id elements:', all_hello_elements)
	print('------')

	print(type(all_list_items[0]))
	print('------')

	print('All list items:')
	for li in all_list_items:
  		print(li.string)
	print('------')

	print('Children of hello-list:')
	for child in all_hello_elements[0].children:
  		print(child.string)
	print('------')

	print('List items within the hello tag')
	hello_list_items = all_hello_elements[0].find_all('li')
	print (hello_list_items)
	print('------')

	print('The hello-list element')
	the_hello_element = soup.find(id='hello-list')
	print(the_hello_element)
	print('------')

	img_tag = soup.find('img')
	print('The img source:')
	print(img_tag['src'])
	print('------')

if printExcercise:
	########## New Requirement ############3
	hello_list_items = all_hello_elements[0].find_all('li')
	print('Words in Hello List:')
	for wordh in hello_list_items:
		print(wordh.string)
	for i in range(2):
		print('------')
	print('Below this was not required, went ahead in lecture')
	for i in range(2):
		print('------')
	################# Below this was not required, went ahead in lecture
	goodbye_list_items = all_goodbye_elements[0].find_all('li')
	print('Words in Goodbye List:')
	for word in goodbye_list_items:
		print(word.string)
	print('------')

	print('Width of Image:')
	pic = soup.find('img')
	print(pic.get('width', 'n/a'))
	print('------')

	url = soup.find('a')
	print('URL:')
	print(url.get('href'))
	print('------')
