import wikipedia as wiki
"""
author: Monil [https://www.github.com/MNISAR]

"""


def parse(content, esc):
    """
    type(content) = str
    """
    assert type(content) == str

    # if content=='':
    #   return None
    # finding max numbers of nested sections
    d = {}
    for i, c in enumerate(content.split(esc)):
        c = c.split(esc[::-1])
        if len(c) == 1:
            section = c[0]
            content = ''
        elif len(c) == 2:
            section = c[0]
            content = c[1]
        else:
            section = c[0]
            content = esc[::-1].join(c[1:])
        d[section.strip()] = content
    return d


def traversal(content, esc):
    if content != '':
        d = parse(content, esc)
        for k in d.keys():
            d[k] = traversal(d[k], esc=esc.strip(" ")+"= ")
        if '' in d:
            del d['']
        return d
    return None


def get_all_wiki(name):
    search_result = wiki.search(name)
    if len(search_result) == 0:
        raise ValueError("no result found for this name.")
    else:
        page = wiki.page(search_result[0], auto_suggest=True)

        d = {
            'content': traversal(page.content, esc='\n== '),
            'url': page.links,
            'summary': page.summary
        }
        return d


def main():
    name = input("Enter term to search('' to quit): ")
    while name != '':
        # get name of item to search
        page = get_all_wiki(name)
        parsed = page['content']

        while type(parsed) == dict:
            keys = list(parsed.keys())
            for ind, topic in enumerate(keys):
                if parsed[topic] is None:
                    print("\n\n", topic, "\n")
                else:
                    print(ind+1, ":", topic)
            if len(parsed) == 1:
                parsed = list(parsed.values())[0]
            else:
                tpc_idx = int(input("Enter topic index(-1 to break): "))
                if tpc_idx == -1:
                    break
                parsed = parsed[keys[tpc_idx-1]]

        print("="*20)
        name = input("Enter term to search('' to quit): ")


if __name__ == '__main__':
    main()
