import csv
import errno
import os


# Write the reviews result to csv_file
def writecsv(filename, dict_data):
    csv_columns = ["Sno", "User", "Rating", "Review"]
    csv_file = filename + ".csv"

    file_exists = os.path.isfile(csv_file)

    try:
        with open(csv_file, "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not file_exists:
                writer.writeheader()
            writer.writerow(dict_data)
    except IOError as ioex:
        print("I/O error")
        print("Error occured while extracting Reviews")
        print("errno:", ioex.errno)
        print("err code:", errno.errorcode[ioex.errno])
