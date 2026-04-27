# phishing detector
import pandas as pd

df = pd.read_csv("phishing_site_urls.csv")  

print("Hello! This is a basic phishing detector\n")


print(df.columns) 

phishing_links = set(df['URL'].str.lower())

link = input("Please input the link you want to check:\n").lower()


def check_url(url):
    score = 0

    if "@" in url:
        score += 1
    if url.count('.') > 3:
        score += 1
    if "-" in url:
        score += 1
    if not url.startswith("https"):
        score += 1
    if len(url) > 75:
        score += 1

    if score >= 3:
        return "This link is likely PHISHING (malicious). Be careful!"
    else:
        return "This link seems safe, but always stay cautious."


# check dataset first
if link in phishing_links:
    print("This link was FOUND in the dataset → malicious!")
else:
    result = check_url(link)
    print(result)