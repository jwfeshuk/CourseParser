import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import subject


def show_contents(container):
    x = 0
    for val in container:
        print(str(x) + " " + str(val.encode("utf-8")))
        x += 1


def main():
    url = "https://catalog.unc.edu/courses/"
    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    subjects_div = soup.find("div", {"id": "atozindex"})
    href_tag = subjects_div.findAll("a", href=re.compile("courses"))

    for i in range(0, len(href_tag)):
        one_href_tag = href_tag[i]
        link = one_href_tag["href"]
        # print(link)
        subject_link = "https://catalog.unc.edu" + link
        print(subject_link)
        subject.process_link(subject_link)
        time.sleep(1)

    print("done")


if __name__ == "__main__":
    main()
