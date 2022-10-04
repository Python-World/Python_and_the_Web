import os
import shutil
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))


def organizeThis(dir_path):
    try:
        print("Organising your files...")
        for filename in os.listdir(dir_path):
            # Check if files are images
            if filename.lower().endswith(
                (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")
            ):
                # If images folder doesnt exist then create
                if not os.path.exists(dir_path + "/images"):
                    os.makedirs(dir_path + "/images")
                shutil.copy2(dir_path + "/" + filename, dir_path + "/images")
                os.remove(dir_path + "/" + filename)

            # Check if files are music
            if filename.lower().endswith(
                (
                    ".wav",
                    ".mp3",
                    ".flac",
                    ".3gp",
                    ".aa",
                    ".aax",
                    ".aiff",
                    ".raw",
                )
            ):
                # If music folder doesnt exist then create
                if not os.path.exists(dir_path + "music"):
                    os.makedirs(dir_path + "/music")
                shutil.copy2(dir_path + "/" + filename, dir_path + "/music")
                os.remove(dir_path + "/" + filename)

                # Check if files are videos
            if filename.lower().endswith((".mp4", ".mov", ".webm")):
                # If videos folder doesnt exist then create
                if not os.path.exists(dir_path + "/videos"):
                    os.makedirs(dir_path + "/videos")
                shutil.copy2(dir_path + "/" + filename, dir_path + "/videos")
                os.remove(dir_path + "/" + filename)

            # Check if files are executables
            if filename.lower().endswith((".exe", ".tar", ".deb")):
                # If executables folder doesnt exist then create
                if not os.path.exists(dir_path + "/executables"):
                    os.makedirs(dir_path + "/executables")
                shutil.copy2(
                    dir_path + "/" + filename, dir_path + "/executables"
                )
                os.remove(dir_path + "/" + filename)

            # Check if files are documents
            if filename.lower().endswith(
                (".txt", ".pdf", ".docx", ".csv", ".xlsx", ".pptx")
            ):
                # If documents folder doesnt exist then create
                if not os.path.exists(dir_path + "/documents"):
                    os.makedirs(dir_path + "/documents")
                shutil.copy2(
                    dir_path + "/" + filename, dir_path + "/documents"
                )
                os.remove(dir_path + "/" + filename)

    except OSError:
        print("Error")
    finally:
        # When script is finished clear screen and display message
        print("Your files are organized now!")


if __name__ == "__main__":
    try:
        dir_path = sys.argv[1]
    except Exception:
        print("Please enter directory path - python3 orgnize.py <path>")
        sys.exit()
    organizeThis(dir_path)
