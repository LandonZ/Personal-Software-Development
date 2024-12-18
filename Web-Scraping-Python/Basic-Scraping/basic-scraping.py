from bs4 import BeautifulSoup

#open html file and read the file mode
with open('home.html', 'r') as html_file:
    #returns content in 1 long string
    content = html_file.read()

    #create beautifulsoup object that can parse lxml.
    # LXML: can parse html faster and cleaner (and WORKS WITH BROKEN HTML)
    soup = BeautifulSoup(content, 'lxml')

    # -- FINDING --
    # find searches for FIRST ELEMENT then stops
    # find_all searches for ALL ELEMENTS. Returns a list

    #GETTING EACH COURSE CARD
    # -- OBJECTIVE -- GET EACH COURSE TITLE AND PRICE

    #each card div class is 'card'. Has underscore class_
    course_cards = soup.find_all('div', class_='card')
    # PARSING IS ALL ABOUT FINDING PATTERNS IN HTML CODE.
    for course in course_cards:
        #COURSE TITLE: inside the h5 tag
        #COURSE PRICE: inside the a tag

        #get h5 attribute from div, then the text only
        course_name = course.h5.text
        #get a attribute, and then the text.
        # each has 3 words: "Start for __". Want the LAST WORD,
        # so do split(), and access last element
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')