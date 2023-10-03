import argparse

import weasyprint


class Html2Pdf:
    """ """

    def __init__(self, url, output_filename):
        """ """
        self.url = url
        self.output_filename = output_filename

    def get_pdf(self):
        """get the file url and create output"""
        pdf = weasyprint.HTML(self.url).write_pdf()
        file_name = "output_files/" + self.output_filename
        with open(file_name, "wb") as file_:
            file_.write(pdf)


if __name__ == "__main__":
    # taking the inputs from cli
    parser = argparse.ArgumentParser()
    parser.add_argument("-inp", "--input", help="input file url")
    parser.add_argument("-out", "--output", help="output file name")
    args = parser.parse_args()
    obj = Html2Pdf(url=args.input, output_filename=args.output)
    obj.get_pdf()
