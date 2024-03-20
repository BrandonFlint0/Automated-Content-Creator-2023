# Automated-Content-Creator-2023

Overview
RedditVideoCreator is a Python application designed to automate the creation of video content from Reddit posts. It fetches posts from specified subreddits, converts the text to speech, combines the audio with a background video, and adds subtitles for each post. The project aims to facilitate the production of engaging video content for platforms like YouTube or social media.

Features
- Fetches top posts from specified subreddits using the PRAW library.
- Converts post text to speech using gTTS (Google Text-to-Speech).
- Creates a video from a specified background clip and overlays the audio.
- Adds dynamically generated subtitles to the video.
- Supports customisation of subreddits and content filtering based on post length and keywords.

Required Libraries and Tools
To run this project, the following libraries and tools are required:
- PRAW: A Python wrapper for the Reddit API, used to fetch posts from Reddit.
- gTTS: A Python library and CLI tool to interface with Google's Text-to-Speech API.
- moviepy: A Python module for video editing, used to edit the background video, combine audio tracks, and add subtitles.
- cv2 (OpenCV for Python): Used for image and video processing, specifically here for subtitle placement.
- PIL (Python Imaging Library): Used for advanced image processing, including drawing text for subtitles.

Ensure all dependencies are installed using pip:
pip install praw gtts moviepy opencv-python pillow

Getting Started
1. Obtain Reddit API credentials by creating a Reddit developer account and registering a new application.
2. Update the placeholder values in the script with your Reddit API client_id, client_secret, and user_agent.
3. Specify the path to your background video and the output directory for the final videos.
4. Run the script to start creating videos from Reddit posts.

Project Structure
- The script initially cleans up any specified directory and sets up the necessary folders for storing intermediate and final video files.
- It checks for subreddit names in the given directory and selects one that hasn't been processed yet.
- For each selected subreddit, it fetches top posts, filters them based on length and content, and converts them to speech.
- The speech files are then combined with a background video, subtitles are added, and the final video is output to the specified directory.

Important Note
As this project involves fetching data from Reddit and using Google's Text-to-Speech API, please ensure you comply with their respective terms of service. Also, be mindful of the usage limits for the APIs to avoid service disruptions or bans. This project was discontinued in mid-2023 upon completion and has not been maintained since. Users should be aware that some aspects of the code may no longer function as intended due to changes in the APIs or dependencies.
