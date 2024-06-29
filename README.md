# Reddit Story AI Content Farm

This repository contains the code for generating and posting AI-generated stories to Reddit.

## Features

- AI Story Generation
- Automated Reddit Posting

## Getting Started

### Prerequisites

- Python 3.8+

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

1. **Reddit API Setup**:
    - Create a Reddit app and obtain client ID, client secret, and user agent.

2. **Environment Variables**:
    - Create a `.env` file with the following content:
      ```plaintext
      REDDIT_CLIENT_ID=your_client_id
      REDDIT_CLIENT_SECRET=your_client_secret
      REDDIT_USER_AGENT=your_user_agent
      OPENAI_API_KEY=your_openai_api_key
      ```

### Usage

1. **Generate Stories**:
    ```bash
    # Command to generate stories
    ```

2. **Post Stories to Reddit**:
    ```bash
    # Command to post stories
    ```

3. **Schedule Automated Posting**:
    - Use a task scheduler to run the posting script at desired intervals.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

---

Feel free to customize this skeleton to better fit your project's specifics and requirements.
