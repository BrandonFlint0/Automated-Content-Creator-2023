import praw
from gtts import gTTS
import os
import re
import string
from slugify import slugify
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.fx.all import speedx
from moviepy.editor import *
import time
from PIL import Image, ImageDraw, ImageFont
import webbrowser
import shutil

# specify the directory path to delete
dir_path = "C:/Users/Brandon/Desktop/Videos"

# check if the directory exists
if os.path.exists(dir_path) and os.path.isdir(dir_path):
    # delete the directory and all its contents
    shutil.rmtree(dir_path)
    print("Directory deleted successfully")
else:
    print("Directory does not exist or is not a directory")

#%%

# Define the directory location
dir_location = "E:/Tiktok"

# Get a list of all the files in the directory
file_list = os.listdir(dir_location)

# Create a list of directory names
directory = [file.split('.')[0] for file in file_list]


# List of words you want to check for existence in directory
words_to_check = ['Scarystories', 'talesfromretail', 'relationships']

# Loop through each word and check if it exists in the directory
for word in words_to_check:
    if any(word in name for name in directory):
        # If the word is already in the directory, skip this iteration of the loop
        continue
    else:
        # If the word is not in the directory, set SubredditText to the word and break the loop
        SubredditText = word
        break

print("Making video based on subreddit " + SubredditText)  # Update SubredditText if the loop is not broken

############################################################### Reddit credential verification & Folder creation #########################################################

# Mac Address /Users/brandonsmac/Desktop
# Windows Address C:/Users/Brandon/Desktop

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # path to chrome.exe

#### Create used stories folder ####

UsedStories_file_path = "C:/Users/Brandon/Desktop/UsedStories.txt"

if not os.path.exists(UsedStories_file_path):
    with open(UsedStories_file_path, 'w') as f:
        f.write("")
    print("New file created.")
else:
    print("File already exists.")


# Initialize reddit instance and set client ID and secret
reddit = praw.Reddit(client_id='...', 
                     client_secret='...', 
                     user_agent='API/1')

print("API Connected")

# Get the current user's home directory
home = os.path.expanduser("~")

# Set the directory to the desktop
desktop = os.path.join(home, "Desktop")

# Create the Reddit Posts folder if it doesn't exist
if not os.path.exists(os.path.join(desktop, "Videos")):
    os.mkdir(os.path.join(desktop, "Videos"))


folder_location = "C:/Users/Brandon/Desktop/Videos"

############################################################### Pull reddit story #########################################################
# Set the subreddit to pull from
#subreddit = reddit.subreddit("Scarystories")

subreddit = reddit.subreddit(SubredditText)

# Set the subreddit folder location
folder_location = "C:/Users/Brandon/Desktop/Videos"

# Create subreddit folder inside "Videos" folder
subreddit_folder = os.path.join(folder_location, subreddit.display_name)
if not os.path.exists(subreddit_folder):
    os.makedirs(subreddit_folder)
    print("Successfully created the directory")
else:
    print("Directory already exists")

# Get the top 10 hot posts from the subreddit
top_posts = subreddit.hot(limit=100)

for i, post in enumerate(top_posts):
    # Get the post selftext
    text = post.selftext
    # Get the post URL
    url = post.url
    # Count the number of words in the post
    word_count = len(text.split())
    

    
    # Check if the post has more than 50 words
    if word_count > 50:
        print("Pass word requirement")
        filename = text
        if text.count('.') >= 2:
            print("Passed punctuation requirement")
            with open(UsedStories_file_path, 'r') as f:
                UsedStoriesText = f.read()
                if post.title not in UsedStoriesText:
                    
                    urlOpen = url

                    webbrowser.get(chrome_path).open(urlOpen)
                    
                    print("--------------------")
                    print(f"Title: {post.title}")
                    VideoTitle = post.title
                    print(f"Author: {post.author}")
                    print(f"{url}")
                    print("--------------------")
                    
                    response = input("Are you happy with this story? (yes/no): ")

                    if response == "yes":
                        # Create the file title using the word count
                        file_title = str(word_count) 
                        
                        # Create the filename using the subreddit variable and the post number
                        #filename = os.path.join(subreddit_folder, subreddit.display_name+" Post "+str(i+1) + ".txt")
                        filename = os.path.join(subreddit_folder, subreddit.display_name+" Post 1.txt")
                        UpdatedText = text.replace("’", "")
                    
                        with open(UsedStories_file_path, 'a') as f:
                            f.write(post.title + "\n")
        
                        with open(filename, "w") as file:
                            file.write(UpdatedText)
                        
                        print("Post loop ran once")
                        break
                    elif response == "no":
                        with open(UsedStories_file_path, 'a') as f:
                            f.write(post.title + "\n")
                        continue
                    else:
                        print("I didn't understand your response. Please answer with 'yes' or 'no'.")

                else:
                    print('Story has already been used')
                    continue
                
        else:
            print('File does not contain at least 2 full stops')
            continue
        
    else:
        print('File does not contain more than 50 words')
        continue
            


print("Txt Documents Created")


#%%


# Open the input file
with open('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'+ SubredditText +' Post 1.txt', 'r') as input_file:
    # Read the contents of the file and remove any newline characters
    contents = input_file.read().replace('\n', '')
    contents = contents.replace('“', '"')
    contents = contents.replace('”', '"')

# Open the output file and write the modified contents
with open('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'+ SubredditText +' Post 1.txt', 'w') as output_file:
    output_file.write(contents)



#%%

####################################################### Split text file into sentences ######################################################
folder_location = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +''
folder_name = "NewText"

if not os.path.exists(os.path.join(folder_location, folder_name)):
    os.mkdir(os.path.join(folder_location, folder_name))
    print("Successfully created the NewText folder")
else:
    print("Directory already exists")


# Define the base directory where the Videos folder is located
base_dir = os.path.join(os.path.expanduser('~'), "Desktop", "Videos")

# Get the list of files in the Scarystories folder
file_list = os.listdir(os.path.join(base_dir,SubredditText))


# Iterate through the files
for file in file_list:
    # Check if the file is a text file
    if file.endswith(".txt"):
        # Open the file and read its contents
        with open(os.path.join(base_dir, SubredditText,file), "r") as f:
            print("Text is defined")
            text = f.read()
        
    # Split the text into lines
    lines = text.split("\n")
    
    new_lines = []
    for line in lines:
        line_split = line.split(".")
        for i in range(len(line_split)):
            if i == len(line_split) - 1:
                new_lines.append(line_split[i].strip())
            else:
                new_lines.append(line_split[i].strip() + ".")

    # Create a new file
    #new_file = os.path.join(base_dir, "'+ SubredditText +'", "NewText", file.split(".")[0] + " Subtitles.txt")
    new_file = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText/NewText Subtitles Before.txt'

    #NewText Subtitles
    
    # Write the new lines to the new file
    with open(new_file, "w") as f:
        f.write("\n".join(new_lines))


# Remove lines that only contain '.'
with open('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText/NewText Subtitles Before.txt', 'r') as input_file, open('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText/NewText Subtitles.txt', 'w') as output_file:
    for line in input_file:
        if line.strip() != '.':
            output_file.write(line)




 #%%
######################### Txt To Speach Bit CHANGE VOICE AND OTHER PARAMETERS ##########################################
CountLines = 0

# Define the path of the subtitle folder
subtitle_folder_path = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText'
dir_path = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +''
# Define a list to store the created audio files
created_audio_files = []
mp3Counter = 1

# check if the folder exists
if os.path.exists(subtitle_folder_path) and os.path.isdir(subtitle_folder_path):
    print("Audio Files Being Created")

    # Define the path of the current text file
    file_path = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText/NewText Subtitles.txt'

    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):

        # open the text file and read the contents
        with open(file_path, "r") as text_file:
            text_lines = text_file.readlines()
        # Count the number of lines in the text
        line_count = len(text_lines)
        # Iterate through each line of the text
        for line_num in range(1, line_count + 1):
            # Get the current line of text
            text = text_lines[line_num-1]
            if not text.strip():
                continue
            # Skip the line if it contains only "."
            if text.strip() == ".":
                continue
            
            # Skip the line if it contains "...."
            if "...." in text:
                continue
            # Skip the line if it contains "...."
            if "..." in text:
                continue
            CountLines = CountLines + 1
            # Define the path of the current audio file ##### DO NOT CHANGE LINE BELOW ######
            audio_file_path = os.path.join(dir_path, file.split(".")[0] + " Audio " + str(CountLines) + ".mp3")
            
            # Check if the audio file already exists in the list
            if audio_file_path in created_audio_files:
                #print(f"Audio file for line {line_num} already exists, skipping.")
                continue
            
            # Check if the text is empty
            if not text.strip():
                print(f"Line {line_num} is empty, skipping.")
                continue
                
            # Create the gTTS object
            try:
                tts = gTTS(text, lang='en', tld='com.au', slow=False)
            except AssertionError as e:
                print(f"Line {line_num} has no text to send to TTS API, skipping.")
                continue

            #tts.save(audio_file_path)
            tts.save('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'+ SubredditText +' Post 1 Audio ' + str(CountLines) + '.mp3')
            #print(audio_file_path)
            #Scarystories Post 1 Audio 2
            print(f"Saved audio file {line_num}/{line_count}")
            # Add the audio file to the list of created files
            created_audio_files.append(audio_file_path)
            mp3Counter += 1

    else:
        print("bad")
else:
    print("The folder does not exist.")


Finalmp3Counter = mp3Counter -1

 #%%
 
 ############# Set video aspect ratio #############
 
 
folder_location = "C:/Users/Brandon/Desktop/Videos"
folder_name = "FinalVideo"

if not os.path.exists(os.path.join(folder_location, folder_name)):
    os.mkdir(os.path.join(folder_location, folder_name))
    print("Successfully created the directory")
else:
    print("Directory already exists")


video = VideoFileClip("C:/Users/Brandon/Desktop/Background Video/1.mp4")
audio_folder = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +''
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]

#video = video.volumex(0)

########## Set video length #############
mp3_dir = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'

# Get the total number of mp3 files in the directory
num_mp3_files = len([f for f in os.listdir(mp3_dir) if f.endswith('.mp3')])

totalLength = 0
# Loop through each mp3 file in the directory
for i in range(1, num_mp3_files + 1):
    
    mp3_file = mp3_dir + ''+ SubredditText +' Post 1 Audio ' + str(i) + '.mp3'
    if os.path.exists(mp3_file):
        # Get the duration of the mp3 file
        audio = AudioFileClip(mp3_file)
        duration = audio.duration
        audio.close()
        # Do something with the duration, such as print it
        totalLength = totalLength + duration
    else:
        continue


#Set length of vid
print(totalLength)
video = video.set_duration(totalLength)
##########################################

    
##Resize the video to match 9:16 aspect ratio
# Get the width and height of the video
width, height = video.size

# Define the size of the cropped video
new_width = 540
new_height = 960

# Calculate the x and y coordinates for the top-left corner of the cropped video
x1 = (width - new_width) / 2
y1 = (height - new_height) / 2
x2 = x1 + new_width
y2 = y1 + new_height
########################################################
# Crop the video
video = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
    
########################################################
# Apply speedx effect
speed_factor = 1 # Set speed factor as you want
video = speedx(video, factor=speed_factor)
video = video.set_fps(25)

video.write_videofile("C:/Users/Brandon/Desktop/Videos/FinalVideo/Final.mp4")

#%%
#################################### Add subtitles to vid ####################################

print("Processing please wait...")

import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def wrap_text(text, font, font_scale, max_width):
    words = text.split(" ")
    lines = []
    line = ""
    for word in words:
        text_size = cv2.getTextSize(line + word, font, font_scale, 1)[0]
        if text_size[0] > max_width:
            lines.append(line)
            line = ""
        line += word + " "
    lines.append(line)
    return list(reversed(lines))

cap = cv2.VideoCapture("C:/Users/Brandon/Desktop/Videos/FinalVideo/Final.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_rate = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter("C:/Users/Brandon/Desktop/Videos/FinalVideo/Finalwithsub.mp4", fourcc, frame_rate, (frame_width, frame_height))

font = cv2.FONT_HERSHEY_SIMPLEX
max_width = frame_width - 70

with open('C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/NewText/NewText Subtitles.txt') as f:
    lines = f.readlines()

line_index = 0
line = ""
line_display_start_time = 0

while True:
    ret, frame = cap.read()
    if ret == True:
        if line == "":
            line = lines[line_index].strip()

            # Get the duration of the audio file for the current line
            audio_file_path = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'+ SubredditText +' Post 1 Audio ' + str(line_index + 1) + '.mp3'
            if os.path.isfile(audio_file_path):
                audio = AudioFileClip(audio_file_path).duration
            else:
                audio = 0

            line_display_start_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

            # Move to the next line after the duration of the line has passed
            lines_to_display = wrap_text(line, font, 1, max_width)
            line_height = int(cv2.getTextSize(" ", font, 1, 1)[0][1] * 1.5)
            
            line_duration = 0
            for line_to_display in lines_to_display:
                line_width = cv2.getTextSize(line_to_display, font, 1, 2)[0][0]
                line_duration += (line_width / max_width) * audio

            line_index += 1
            if line_index >= len(lines):
                break
        
        lines_to_display = wrap_text(line, font, 1, max_width)
        line_height = int(cv2.getTextSize(" ", font, 1, 1)[0][1] * 1.5)
        
        y = int((frame_height + line_height * len(lines_to_display)) / 2)
        total_height = 0
        for line_to_display in lines_to_display:
            text_width, text_height = cv2.getTextSize(line_to_display, font, 1, 2)[0]
            x = int((frame_width - text_width) / 2) + 7
            y -= line_height
            # Draw black outline
            cv2.putText(frame, line_to_display, (x, y), font, 1, (0, 0, 0), 4, cv2.LINE_AA)
            # Draw white text in center
            cv2.putText(frame, line_to_display, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

            total_height += text_height
        bottom_y = y + total_height + line_height

        text_height = (line_height * len(lines_to_display))
        box_top_left = (10, y - 30 - int(text_height * 0.1))
        box_bottom_right = (frame_width - 10, bottom_y + 5)

        # Update the line if the line duration has passed
        if (cap.get(cv2.CAP_PROP_POS_MSEC) / 1000) - line_display_start_time >= audio:
            line = ""

        out.write(frame)
        cv2.imshow('video with subtitles', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

#%%
#################################### Add audio to vid ####################################

import praw
from gtts import gTTS
import os
import re
import string
from slugify import slugify
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.fx.all import speedx

from moviepy.editor import *
import time
from PIL import Image, ImageDraw, ImageFont


def count_mp3_files(folder_pathCount):
    count = 0
    for filename in os.listdir(folder_pathCount):
        if filename.endswith(".mp3"):
            count += 1
    return count

folder_pathCount = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'
mp3_file_count = count_mp3_files(folder_pathCount)
print("Number of Mp3 files:", mp3_file_count)


audio_tracks = []
# Loop through the range of audio files
for i in range(1, mp3_file_count + 1):
    audio_path = 'C:/Users/Brandon/Desktop/Videos/'+ SubredditText +'/'+ SubredditText +' Post 1 Audio ' + str(i) + '.mp3'

    # Check if the audio file exists
    if os.path.exists(audio_path):
        # Open the audio file
        audio = AudioFileClip(audio_path)

        audio_tracks.append(audio)
    else:
        # If the file does not exist, skip the iteration
        continue
        
# Combine the audio tracks into a single audio clip
combined_audio = concatenate_audioclips(audio_tracks)

# Open the video file
video = VideoFileClip("C:/Users/Brandon/Desktop/Videos/FinalVideo/Finalwithsub.mp4")

# Overlay the combined audio track onto the video
final_video = CompositeVideoClip([video])
final_video = final_video.set_audio(combined_audio)

# Write the final video to a single mp4 file
final_video.write_videofile("C:/Users/Brandon/Desktop/Videos/FinalVideo/Finalwithsub_combined.mp4")

############# Speed video up #############

video = VideoFileClip("C:/Users/Brandon/Desktop/Videos/FinalVideo/Finalwithsub_combined.mp4")

speed_factor = 1.08 # Set speed factor as you want
video = speedx(video, factor=speed_factor)

video.write_videofile("E:/Tiktok/" + SubredditText + ".mp4")

os.execl(sys.executable, sys.executable, *sys.argv)



