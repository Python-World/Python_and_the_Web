from sys import argv, platform
from bs4 import BeautifulSoup
from os import mkdir, getcwd, chdir, path
import requests, time


def get_folder_links(folder_url):
    get_folder_url_contents = requests.get(folder_url).content
    bs4 = BeautifulSoup(get_folder_url_contents, "html.parser")
    link_grep = bs4.find_all(
        "a", class_="js-navigation-open link-gray-dark"
    )  # Filters for folders and file links on github page
    _all_folder_links = [
        link.attrs["href"] for link in link_grep
    ]  # extracts href attribute from <a> tag
    _all_folder_links_href = [
        link for link in _all_folder_links if "blob" in link
    ]  # exracts all folder links
    _all_folder_folders_href = [
        link for link in _all_folder_links if "blob" not in link
    ]  # extracts all file links
    print("Files -- ", _all_folder_links_href, "\n")
    print("Folders -- ", _all_folder_folders_href, "\n")
    # exit()
    return (
        _all_folder_folders_href,
        _all_folder_links_href,
    )  # returns both Folders links and Files links as a list


def download_files(files_to_download):
    for file in files_to_download:
        print("\nfile - ", file)
        filename = file.split("/")[
            -1
        ]  # Uses the last name on the path as filename of file to be saved to disk
        url_build = "https://raw.githubusercontent.com" + file.replace(
            "/blob", ""
        )  # Builds the url used to retrieve the file
        req_timenow = time.time()
        open_file_url_res = requests.get(
            url_build
        )  # uses python's request librar to download the file from github
        print("get-request-time => ", time.time() - req_timenow)
        wr_timenow = time.time()
        with open(filename, "wb") as file_handle:
            file_handle.write(
                open_file_url_res.content
            )  # writes the just downloaded file to disk
        print("write time => ", time.time() - wr_timenow)

        print(f"Retrieved {filename}")  # \n


def recursive_folder_download(folder_links_received, file_hrefs_received):
    # This function does an "os.walk()" type of heavy lifting, as it recursively downloads folder contents and
    # creates a mirror to disk, thereby preserving the folders hierechical structure as it is on github
    if len(folder_links_received) > 0:
        download_files(
            file_hrefs_received
        )  # if files present in folder, download them first
        for folder in folder_links_received:
            print("folder - ", folder)
            folder_name = str(folder).split("/")[-1]
            mkdir(
                folder_name
            )  # creates a local copy|mirror of the currently walked|selected github folder. ... helps preserve folder structure
            chdir(
                folder_name
            )  # changes working directory to the just created folder
            print("current dir ==> ", getcwd())
            # exit()
            folder_list, file_list = get_folder_links(
                "https://github.com" + folder
            )
            recursive_folder_download(folder_list, file_list)
            chdir(
                ".."
            )  # changes working directory to the parent directory ... helps preserve folder structure
    else:
        download_files(file_hrefs_received)


if __name__ == "__main__":
    os_platform = str(platform).lower()
    if (
        "linux" in os_platform
        or "linux2" in os_platform
        or "darwin" in os_platform
        or "posix" in os_platform
    ):
        try:
            mkdir(
                path.join(
                    path.expanduser("~"), "Desktop", "Git-Folder_Download"
                )
            )
        except FileExistsError:
            chdir(
                path.join(
                    path.expanduser("~"), "Desktop", "Git-Folder_Download"
                )
            )

    elif (
        "win32" in os_platform
        or "windows" in os_platform
        or "nt" in os_platform
        or "win64" in os_platform
    ):
        try:
            mkdir(
                path.join(
                    path.expanduser("~"), "Desktop", "Git-Folder_Download"
                )
            )
        except FileExistsError:
            chdir(
                path.join(
                    path.expanduser("~"), "Desktop", "Git-Folder_Download"
                )
            )

    # This lines above are probably redundant ... and self explanatory ... i hope i dont have to explain what it does
    # could replace them with a single "chdir(path.join(os.path.expanduser('~'), 'Desktop','Git-Folder_Download'))""

    while True:
        try:
            url = str(
                argv[1]
            )  # retrieves argument from user and sets it as the URL
        except:
            print("[x] No link supplied! ... \n")
            url = str(input("[-] Paste Github link here \n [Ctr-v] "))
            # url = "https://github.com/TEMHITHORPHE/hacktoberfest-html" default link can be set here

        folder_links, file_hrefs = get_folder_links(url)
        mkdir("git_folder-" + url.split("/")[-1])
        chdir("git_folder-" + url.split("/")[-1])
        recursive_folder_download(folder_links, file_hrefs)
        print(f"\n\n[x] Download complete! \n[x] Folder saved to [{getcwd()}]")
        break
