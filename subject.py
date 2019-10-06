import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Course:
    def __init__(self, subject, number, credit, desc):
        self.subject = subject
        self.number = number
        self.credit = credit
        self.desc = desc

    def __str__(self):
        return "%s %s - %s credit(s) - %s" % (
            self.subject,
            self.number,
            self.credit,
            self.desc,
        )


def show_contents(container):
    x = 0
    for val in container:
        print(str(x) + " " + val.subject)
        x += 1


def process_link(url: str):
    # url = "https://catalog.unc.edu/courses/aero"
    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    courses_div = soup.find("div", {"id": "sc_sccoursedescs"})
    course_title = courses_div.findAll("p", "courseblocktitle")

    for x in course_title:
        course = x.string.split(". ")

    courses = []

    x = 0
    for val in course_title:
        course = val.string.split(". ")
        course[0] = course[0].split("\xa0")
        courses.append(
            Course(course[0][0], course[0][1], course[1].strip(), course[2].strip())
        )
        x += 1

    for i in courses:
        print(i)

