# Importing pafy library
import pafy

# Taking url as input from the user
url = input("Enter URL: ")

# Creating a video instance
video = pafy.new(url)

# Using 'bestaudio()' to select the best audio file
bestaudio = video.getbestaudio()

# Using 'download()' to download the selected audio file
bestaudio.download()
