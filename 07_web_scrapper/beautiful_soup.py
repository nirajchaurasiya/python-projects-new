from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")

    # tags = soup.find("h5")

    # courses_html_tags = soup.find_all("h5")

    # for course in courses_html_tags:

    #     print(course.text)

    courses_cards = soup.find_all("div", class_="card")

    for course in courses_cards:

        # print(course.h5)

        # print(course.a)

        course_name = course.h5.text

        course_price = course.a.text.split(" ")[-1]

        print(f"{course_name} => {course_price}")
