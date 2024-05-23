import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_vietnam_universities():

    url = "https://en.wikipedia.org/wiki/List_of_universities_in_Vietnam"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    extracted_html_tables = soup.find_all("table", {"class": "wikitable"})
    df = pd.DataFrame()
    for table_html in extracted_html_tables:
        sub_df = pd.read_html(str(table_html))[0]
        df = pd.concat([df, sub_df], ignore_index=True)

    # remove column "No."
    df = df.drop(columns=["No."])
    df.to_csv("data/vietnam_universities.csv", index=False)


if __name__ == "__main__":
    get_vietnam_universities()
