# Reddit Story AI Content Farm

This project is designed to generate AI-created stories and convert them into YouTube Shorts, leveraging advanced natural language processing techniques and automation.

## Features

- **AI Story Generation**: Utilizes advanced language models to create engaging stories.
- **Video Creation**: Converts generated stories into YouTube Shorts.
- **Customization Options**: Allows configuration of story themes and video styles.
- **Logging and Monitoring**: Tracks content creation and performance metrics.

## Getting Started

### Prerequisites

To run this project, you will need:

- Python 3.8 or higher
- Reddit API Key (for scraping reddit posts)
- YouTube API credentials (for uploading videos)

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    **If you are running on OSX**:
     - if you are runnning on OSX and would like to allow for speedup of mp3, you will need to perform the following instructions to download ffprobe, which is a requirement for pydub, our python audio interpreter.
    1. Download both ffmpeg and ffprobe from https://ffbinaries.com/downloads
    2. Run the following in the command line:
        ```zsh
        sudo cp Downloads/ffmpeg /usr/local/bin/
        sudo chmod 755 /usr/local/bin/ffmpeg
        ffmpeg

        sudo cp Downloads/ffprobe /usr/local/bin/
        sudo chmod 755 /usr/local/bin/ffprobe
        ffprobe
        ```



### Configuration

1. **YouTube API Setup**:
    - Create a project in the [Google Developers Console](https://console.developers.google.com/).
    - Enable the YouTube Data API and obtain your API credentials.

2. **Environment Variables**:
    - Create a `.env` file in the project root with the following content:
      ```plaintext
        REDDIT_CLIENT_ID= "" //PUT_YOUR_REDDIT_ID_HERE
        REDDIT_CLIENT_SECRET="" //PUT_YOUR_REDDIT_SECRET_HERE
        REDDIT_USER_AGENT = "" //NAME_YOUR_REDDIT_USER_AGENT
      ```

### Usage

1. **Generate Stories**:
    - The story generation script uses an AI model to create engaging content based on specified themes.
    - Example command:
    ```bash
    # Command to generate stories
    ```

2. **Create YouTube Shorts**:
    - The video creation script converts generated stories into video format suitable for YouTube Shorts.
    - Example command:
    ```bash
    # Command to create videos
    ```

3. **Upload Videos to YouTube**:
    - The upload script automates the process of uploading videos to YouTube.
    - Example command:
    ```bash
    # Command to upload videos
    ```

### Logging and Monitoring

- The project includes logging features to keep track of content creation and video performance (e.g., views, likes, comments).
- Example logs:
    ```plaintext
    [INFO] Created video "Title" from story "Story Title" at 2024-06-29 12:00
    [INFO] Video received 100 views and 10 likes in the first hour
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact us at your-email@example.com.

---

This README provides a high-level overview of the Reddit Story AI Content Farm, detailing its features, setup, and usage. As the project evolves, more specific instructions and examples can be added.
