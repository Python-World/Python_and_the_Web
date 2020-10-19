import os, subprocess
from tempfile import NamedTemporaryFile


infile = input('Input file: ')
outfile= input('Output file: ')
shakiness= input('Shakiness (1-10): ')
accuracy= input('Accuracy (1-15): ')
smoothing=input('Smoothing (1-): ')

vidstb= 'vidstabdetect=stepsize=6:shakiness='+shakiness+':accuracy='+accuracy+':result=/dev/stdout'

cmd1=['ffmpeg', '-loglevel', 'panic','-i',infile , '-vf',vidstb, '-f','null','pipe:1']
p = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
vectors, err = p.communicate()

vf = NamedTemporaryFile()
original_path = vf.name

x = bytearray(vectors)

f = open(original_path, 'wb')
f.write(x)
f.close()

os.system('ffmpeg -loglevel panic -i ' + infile + ' -vf vidstabtransform=input='+ original_path +':smoothing='+smoothing+':crop=keep,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy ' + outfile )


print('Done')
