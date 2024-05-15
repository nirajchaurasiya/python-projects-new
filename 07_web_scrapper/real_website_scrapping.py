from bs4 import BeautifulSoup

import time

import requests

print("Put some skills that you are not familiar with.")

unfamiliar_skill = input(">")

print(f"Filtering out {unfamiliar_skill}")


def main():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation="
    ).text
    # data = html_text.json()
    # print(html_text)

    soup = BeautifulSoup(html_text, "lxml")

    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):

        published_date = job.find("span", class_="sim-posted").span.text

        if "few" in published_date:

            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")

            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write("-" * 70)

                print(f"File Saved: {index}.txt  ")


if __name__ == "__main__":
    while True:
        main()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
