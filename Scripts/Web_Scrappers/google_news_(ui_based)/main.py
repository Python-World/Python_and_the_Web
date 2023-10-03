import re

import requests as rq
from bs4 import BeautifulSoup


def fetch_news(link, file_name="custom_news.txt"):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    r = rq.get(link, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    main_div = soup.find(
        "div", attrs={"class": re.compile("lBwEZb BL5WZb GndZbb")}
    )
    news_set = main_div.find_all(
        "div", attrs={"jscontroller": re.compile("d0DtYd")}
    )
    news_set2 = main_div.find_all("div", attrs={"class": re.compile("xrnccd")})
    sources = []
    links = []
    headings = []
    for s in news_set:
        source = s.find(
            "a", attrs={"class": re.compile("wEwyrc AVN2gc uQIVzc Sksgp")}
        )
        time = s.find(
            "time", attrs={"class": re.compile("WW6dff uQIVzc Sksgp")}
        )
        try:
            stri = source.text + ", Uploaded - " + time.text
        except AttributeError:
            stri = source.text
        sources.append(stri)
        link = s.find("a")
        links.append("https://news.google.com" + link["href"][1:])
        head = s.find("h3")
        headings.append(head.text)
    for s in news_set2:
        headings.append(s.h3.text)
        links.append("https://news.google.com" + s.a["href"][1:])
        time = s.find(
            "time", attrs={"class": re.compile("WW6dff uQIVzc Sksgp")}
        )
        source = s.find(
            "a", attrs={"class": re.compile("wEwyrc AVN2gc uQIVzc Sksgp")}
        )
        try:
            stri = source.text + ", Uploaded - " + time.text
        except AttributeError:
            stri = source.text
        sources.append(stri)
    l = len(headings)
    with open(file_name, "w") as file:
        for i in range(l):
            file.write(sources[i] + "\n")
            file.write(headings[i] + "\n")
            file.write("Ref: " + links[i] + "\n\n")
    file.close()
    if file_name == "custom_news.txt":
        print('Your news in ready in "custom_news.txt" file.')


ans = input("Do you want to fetch latest World News (y/n) ? ")
if ans == "y":
    print("Fetching World News...    This might take a while")
    fetch_news(
        "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
        "world_news.txt",
    )
    print("Done!!")
    print('World latest news can be found in "world_news.txt" file.')

print("You can also grab custom news of your taste :-)")
print("\t 1. Business")
print("\t 2. Technology")
print("\t 3. Entertainment")
print("\t 4. Sports")
print("\t 5. Science")
print("\t 6. Health")
c1 = True
c2 = True
ch = int(input("Enter your choice (Eg : 1 for Business): "))
print("")

fetch = ""
if ch == 1:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Economy")
    print("\t c. Markets")
    print("\t d. Jobs")
    print("\t e. Personal finance")
    print("\t f. Enterpreneurship")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1HZG1jSE16S2dzU0NTOXRMekJuWm5Cek15Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURsek1XWVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiYENCQVNRZ29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1EbDVOSEJ0S2hvS0dBb1VUVUZTUzBWVVUxOVRSVU5VU1U5T1gwNUJUVVVnQVNnQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiXENCQVNQd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERjBjWEpyS2hjS0ZRb1JTazlDVTE5VFJVTlVTVTlPWDA1QlRVVWdBU2dBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERjVObU54S2dzU0NTOXRMekF4ZVRaamNTZ0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURsek1XWVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESnVkM0VxQ2hJSUwyMHZNREp1ZDNFb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
elif ch == 2:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Mobile")
    print("\t c. Gadgets")
    print("\t d. Internet")
    print("\t e. Virtual reality")
    print("\t f. Artificial  intelligence")
    print("\t g. Computing")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiZkNCQVNSZ29JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EVXdhemdxSHdvZENobE5UMEpKVEVWZlVFaFBUa1ZmVTBWRFZFbFBUbDlPUVUxRklBRW9BQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiX0NCQVNRUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ESnRaakZ1S2hrS0Z3b1RSMEZFUjBWVVgxTkZRMVJKVDA1ZlRrRk5SU0FCS0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ETnliSFFxQ2hJSUwyMHZNRE55YkhRb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EZGZibmtxQ2hJSUwyMHZNRGRmYm5rb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiR0NCQVNMd29JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJTkNBUWFDUW9ITDIwdk1HMXJlaW9KRWdjdmJTOHdiV3Q2S0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "g":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ERnNjSE1xQ2hJSUwyMHZNREZzY0hNb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
elif ch == 3:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Movies")
    print("\t c. Music")
    print("\t d. TV")
    print("\t e. Books")
    print("\t f. Art")
    print("\t g. Celebrities")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiXkNCQVNRQW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESjJlRzRxR1FvWENoTk5UMVpKUlZOZlUwVkRWRWxQVGw5T1FVMUZJQUVvQUEqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURKcWFuUVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EUnliR1lxQ2hJSUwyMHZNRFJ5YkdZb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EZGpOVElxQ2hJSUwyMHZNRGRqTlRJb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiXkNCQVNRQW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1HSjBYMk16S2hnS0Znb1NRazlQUzFOZlUwVkRWRWxQVGw5T1FVMUZJQUVvQUEqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURKcWFuUVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiR0NCQVNMd29JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJTkNBUWFDUW9ITDIwdk1HcHFkeW9KRWdjdmJTOHdhbXAzS0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "g":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ERnlabm9xQ2hJSUwyMHZNREZ5Wm5vb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1ESnFhblFTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
elif ch == 4:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Cricket")
    print("\t c. Hockey")
    print("\t d. Tennis")
    print("\t e. Football")
    print("\t f. Badminton")
    print("\t g. Kabbadi")
    print("\t h. Women's Cricket")
    print("\t i. Basketball")
    print("\t j. F1 Racing")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ESTBibW94S2dzS0NSSUhRM0pwWTJ0bGRDZ0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadWRHb1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTkNCQVNOQW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJUkNBUWFEUW9MTDIwdk1ERXhZbUk0TWpNcUNnb0lFZ1pJYjJOclpYa29BQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EZGljekFxQ2dvSUVnWlVaVzV1YVhNb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESjJlRFFxREFvS0VnaEdiMjkwWW1Gc2JDZ0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadWRHb1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTkNCQVNOQW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ERTVOR1FxRFFvTEVnbENZV1J0YVc1MGIyNG9BQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "g":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiS0NCQVNNZ29JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EUmlNSE1xQ3dvSkVnZExZV0ppWVdScEtBQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "h":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiV0NCQVNPd29JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1EY3diV3M0S2hNS0VSSVBWMjl0Wlc0bmN5QkRjbWxqYTJWMEtBQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "i":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiT0NCQVNOUW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ERTRkemdxRGdvTUVncENZWE5yWlhSaVlXeHNLQUEqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadWRHb1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "j":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTkNCQVNOQW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESjRlaklxRFFvTEVnbEdNU0JTWVdOcGJtY29BQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
elif ch == 5:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Environment")
    print("\t c. Outer space")
    print("\t d. Physics")
    print("\t e. Genetics")
    print("\t f. Wildlife")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiT0NCQVNOUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJUUNBUWFEQW9LTDIwdk1EUTJOak15Y3lvTUVnb3ZiUzh3TkRZMk16SnpLQUEqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadGNUY1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERTRNek4zS2dzU0NTOXRMekF4T0RNemR5Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadGNUY1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EVnhhblFxQ2hJSUwyMHZNRFZ4YW5Rb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ETTJYeklxQ2hJSUwyMHZNRE0yWHpJb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERXlPREJuS2dzU0NTOXRMekF4TWpnd1p5Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadGNUY1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
elif ch == 6:
    print(
        "Enter the sub-topic of the category you selected. You can choose from :"
    )
    print("\t a. Latest")
    print("\t b. Medicine")
    print("\t c. Healthcare")
    print("\t d. Mental health")
    print("\t e. Nutrition")
    print("\t f. Fitness")
    ch2 = input("Enter your choice (Eg : a for Latest): ")
    if ch2 == "a":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "b":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiRENCQVNMUW9JTDIwdk1HdDBOVEVTQldWdUxVZENJZzRJQkJvS0NnZ3ZiUzh3TkhOb015b0tFZ2d2YlM4d05ITm9NeWdBKikIAColCAoiH0NCQVNFUW9JTDIwdk1HdDBOVEVTQldWdUxVZENLQUFQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "c":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiR0NCQVNMd29JTDIwdk1HdDBOVEVTQldWdUxVZENJZzhJQkJvTENna3ZiUzh3TVcxM01uZ3FDeElKTDIwdk1ERnRkeko0S0FBKikIAColCAoiH0NCQVNFUW9JTDIwdk1HdDBOVEVTQldWdUxVZENLQUFQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "d":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiR0NCQVNMd29JTDIwdk1HdDBOVEVTQldWdUxVZENJZzhJQkJvTENna3ZiUzh3TTNnMk9XY3FDeElKTDIwdk1ETjROamxuS0FBKikIAColCAoiH0NCQVNFUW9JTDIwdk1HdDBOVEVTQldWdUxVZENLQUFQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "e":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiRENCQVNMUW9JTDIwdk1HdDBOVEVTQldWdUxVZENJZzRJQkJvS0NnZ3ZiUzh3TldScVl5b0tFZ2d2YlM4d05XUnFZeWdBKikIAColCAoiH0NCQVNFUW9JTDIwdk1HdDBOVEVTQldWdUxVZENLQUFQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    elif ch2 == "f":
        fetch = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiW0NCQVNQZ29JTDIwdk1HdDBOVEVTQldWdUxVZENJZzhJQkJvTENna3ZiUzh3TWpkNE4yNHFHZ29ZQ2hSR1NWUk9SVk5UWDFORlExUkpUMDVmVGtGTlJTQUJLQUEqKQgAKiUICiIfQ0JBU0VRb0lMMjB2TUd0ME5URVNCV1Z1TFVkQ0tBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    else:
        print("Invalid Choice!")
        c2 = False
else:
    c1 = False
print("")
cond = c1 & c2
if cond is True:
    print("Fetching your custom News...")
    fetch_news(link=fetch)
    print("Thank You")
else:
    print("The program will now exit!")
