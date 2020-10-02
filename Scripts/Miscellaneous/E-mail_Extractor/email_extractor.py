import re
import sys

import requests


def is_valid_url(url):
    """
    Function Vaildate the url
    """

    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)"
        r"+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None


class EmailExtracter:
    """
    Class EmailExtracter extracts
    email from the static webpages
    and text files
    """

    def __init__(self, source):
        if is_valid_url(source):
            self.source = requests.get(source).text
        else:
            file = open(source, "r")
            self.source = str(file.readlines())

    @property
    def extract_email(self) -> list:
        """
        Function that extract the email

        Regex Reference:
        https://emailregex.com/
        """

        regex = re.compile(
            r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+"
            r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+"
            r""")*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|"""
            r"""\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")"""
            r"@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])"
            r"?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|"
            r"\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
            r"{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]"
            r":(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|"
            r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        )

        result = re.findall(regex, self.source)
        return result


if __name__ == "__main__":
    source = sys.argv[1]
    emails = EmailExtracter(source)
    for email in emails.extract_email:
        print(email)
