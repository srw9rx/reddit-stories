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
- OpenAI API key (or similar service for text generation)
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

### Configuration

1. **YouTube API Setup**:
    - Create a project in the [Google Developers Console](https://console.developers.google.com/).
    - Enable the YouTube Data API and obtain your API credentials.

2. **Environment Variables**:
    - Create a `.env` file in the project root with the following content:
      ```plaintext
      OPENAI_API_KEY=your_openai_api_key
      YOUTUBE_API_KEY=your_youtube_api_key
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
