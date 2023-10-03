import io
import urllib.request as ulibr

from bs4 import BeautifulSoup

# wikipedia url
base_url = "https://en.wikipedia.org/wiki/"


# this function creates name suitable for searching
def create_name(first, last):
    if first is None and last is None:
        return "error"
    first = first[0].capitalize() + first[1:]
    last = last[0].capitalize() + last[1:]
    full_name = "{}_{}".format(first, last)
    return full_name


def get_table(soup):
    tables = soup.findChildren("table")
    content_table = []
    my_table = tables[0]
    # write_to_file(my_table)
    rows = my_table.findChildren(["th", "tr"])
    for row in rows:
        cells = row.findChildren("td")
        head = row.findChildren("th")
        row_list = []

        # specially for career stat
        if len(cells) == 0 and len(head) >= 4:
            head = [h.get_text() for h in head]
            content_table.append(head[1:])
            continue

        # getting headings
        if len(head) >= 1 and head[0] is not None and len(cells) >= 1:
            row_list.append(head[0].get_text())
            row_list.append(" : ")

        for cell in cells:
            row_list.append(cell.get_text())
        content_table.append(row_list)

    return content_table


# writes data to file
def write_to_file(content_table, name):
    with io.open(
        "./scraped_texts/{}.txt".format(name), "w", encoding="UTF-8"
    ) as dobj:
        for line in content_table:
            if len(line) >= 1 and line[0] is not None:
                for value in line:
                    if value is not None:
                        dobj.write(value + " ")
                dobj.write("\n")


# extracts contents from file and presents
def show_to_teeminal(name):
    not_needed = ["5 wickets in innings\n", "10 wickets in match\n"]
    final_list = []
    with io.open(
        "./scraped_texts/{}.txt".format(name), "r", encoding="UTF-8"
    ) as dobj:
        print("----------------------------{}-------------------".format(name))
        for line in dobj:
            if len(line.split()) > 2 and line not in not_needed:
                final_list.append(line)

    # check for that wierd string
    index = -1
    for i in range(len(final_list)):
        if final_list[i].startswith("Test ODI"):
            index = i
            break
    if index != -1:
        del final_list[index - 1]
    # printing nicely to console
    for line in final_list:
        print(line)


if __name__ == "__main__":
    first_name = input("Firstname : ")
    last_name = input("Lastname : ")
    # wiki needs name in certain format so adjust that
    full_name = create_name(first_name, last_name)

    # forming correct url with base url and name of the player
    url = base_url + full_name

    # getting a html data from wiki
    try:
        resp_obj = ulibr.urlopen(url=url)
        html = resp_obj.read().decode(encoding="UTF-8")
        soup = BeautifulSoup(html, "html.parser")

        content_table = get_table(soup)
        write_to_file(content_table, full_name)

        # to get the results to terminal
        show_to_teeminal(full_name)

    except Exception as err:
        print(err)
