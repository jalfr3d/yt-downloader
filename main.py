import yt_dlp
import os

# Replace this with the YouTube link you want
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

# Set your desired output folder
output_folder = "downloads"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Hook function to show progress
def progress_hook(d):
    if d['status'] == 'downloading':
        if not progress_hook.started:
            print(f"\n📥 Starting download: {d['filename']}")
            progress_hook.started = True
    elif d['status'] == 'finished':
        print(f"\n✅ Download finished: {d['filename']}")
progress_hook.started = False

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'merge_output_format': 'mp4',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'progress_hooks': [progress_hook],
    'noplaylist': True,
    'quiet': False,
}

# Download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
