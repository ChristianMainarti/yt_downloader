<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Downloader</title>
</head>
<body>
    <h1>YouTube Video Downloader</h1>
    <p>This is a Python script that downloads YouTube videos in the best available quality using <code>yt-dlp</code>. It reads a list of video URLs from a text file (<code>links.txt</code>) and downloads the videos in MP4 format, merging the best available video and audio.</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.7 or higher</li>
        <li><code>yt-dlp</code> (an improved version of <code>youtube-dl</code>)</li>
    </ul>

    <h2>Setup</h2>
    <h3>1. Clone the repository or download the files</h3>
    <p>If you already have the script, skip to the next step. Otherwise, download the files or clone this repository using:</p>
    <pre><code>git clone https://github.com/your_username/your_repository.git
cd your_repository
    </code></pre>

    <h3>2. Create a virtual environment</h3>
    <p>It is recommended to create a virtual environment to manage the project's dependencies in isolation.</p>
    <pre><code># Create a virtual environment called 'env'
python3 -m venv env

# Activate the virtual environment
# On Linux/Mac:
source env/bin/activate

# On Windows:
env\Scripts\activate
    </code></pre>

    <h3>3. Install the dependencies</h3>
    <p>With the virtual environment activated, install the necessary dependencies:</p>
    <pre><code># Update pip and install yt-dlp
pip install --upgrade pip
pip install yt-dlp
    </code></pre>
    <p>Now you're ready to use the script.</p>

    <h2>How to Use</h2>

    <h3>1. Create the <code>links.txt</code> file</h3>
    <p>Create a text file named <code>links.txt</code> in the same directory as the script. Add one YouTube URL per line, like the example below:</p>
    <pre><code>https://www.youtube.com/watch?v=EXAMPLE1
https://www.youtube.com/watch?v=EXAMPLE2
https://www.youtube.com/watch?v=EXAMPLE3
    </code></pre>

    <h3>2. Run the script</h3>
    <p>After adding the links to the <code>links.txt</code> file, you can run the script to download the videos. Make sure your virtual environment is activated.</p>
    <pre><code>python download_videos.py
    </code></pre>
    <p>The videos will be downloaded to the same directory where the script is run, in the best possible quality, in MP4 format.</p>

    <h2>Important Notice</h2>
    <p><strong>Please ensure that you only download videos that are not protected by copyright, or that you have explicit permission to download. This script is intended for downloading content that is in the public domain, licensed under Creative Commons, or for personal use in compliance with YouTube's terms of service. Downloading copyrighted content without permission is illegal and against YouTube's policies.</strong></p>

    <h2>Project Structure</h2>
    <pre><code>├── download_videos.py  # Main script to download videos
├── links.txt           # File containing the video URLs
├── README.md           # This file
└── env/                # Virtual environment (after creation)
    </code></pre>

    <h2>Script Functions</h2>
    <ul>
        <li><strong><code>download_video(yt_url)</code></strong>: Downloads a specific YouTube video, using the best available video and audio quality and merging them into an MP4 file.</li>
        <li><strong><code>main()</code></strong>: Reads all the URLs from the <code>links.txt</code> file and downloads each one.</li>
    </ul>

    <h2>Deactivating the virtual environment</h2>
    <p>After using the script, you can deactivate the virtual environment with:</p>
    <pre><code>deactivate
    </code></pre>

    <h2>Contribution</h2>
    <p>If you wish to contribute to the project, feel free to open an issue or submit a pull request.</p>

</body>
</html>
