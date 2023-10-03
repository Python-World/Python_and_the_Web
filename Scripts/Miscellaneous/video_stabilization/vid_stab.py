import os
import subprocess
from tempfile import NamedTemporaryFile

infile = input("Input file: ")
outfile = input("Output file: ")
# How shaky the video is. Will be used by vidstabdetect.
shakiness = input("Shakiness (1-10): ")
# Set the accuracy of detection used by vidstabdetect
accuracy = input("Accuracy (1-15): ")
# The number of frames used for lowpass filtering the camera movements.
smoothing = input("Smoothing (1-): ")

# Vidstabdetect analyzes the video stabilization/deshaking
vidstb = (
    "vidstabdetect=stepsize=6:shakiness="
    + shakiness
    + ":accuracy="
    + accuracy
    + ":result=/dev/stdout"
)

# Execute the command to analyze the video and pipe the result
cmd1 = [
    "ffmpeg",
    "-loglevel",
    "panic",
    "-i",
    infile,
    "-vf",
    vidstb,
    "-f",
    "null",
    "pipe:1",
]
p = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
vectors, err = p.communicate()

vf = NamedTemporaryFile()
original_path = vf.name

x = bytearray(vectors)
# Store the values
with open(original_path, "wb") as f:
    f.write(x)
    f.close()

# Execute the command to stabilize the video using the generated vector values
os.system(
    "ffmpeg -loglevel panic -i "
    + infile
    + " -vf vidstabtransform=input="
    + original_path
    + ":smoothing="
    + smoothing
    + ":crop=keep,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy "
    + outfile
)

print("Done")
