

# pip install moviepy

import glob
#The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
from moviepy.editor import VideoFileClip
sum = []
for file in glob.iglob('E:\DelhiT\C++T\c++/*.mp4'):
    #for mp4 file
    #you can change extension	
    
    # print('E:/MOOC/ML/%s' % filename)
     clip = VideoFileClip(file)
    # print( clip.duration )
     sum.append(clip.duration)
length = 0     
for video_length in sum:
    length = length + video_length
    
# "%.2f" % 3.14159      
length = length/3600.0
print( "I have to Study for %.2f Hours" % length)  

   