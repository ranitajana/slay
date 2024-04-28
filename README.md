# slay
This is the codebase for an AI assisted teaching assistant 'Slay'.

The code takes the YouTube URL of a video lecture and a lesson plan as an input and returns the lecture-notes in structured format based on the lesson plan. It also auto-generates a set of quiz. 

## Requirements

- Python 3.10 or higher
- OpenAI API key
- Deepgram API key

## Installation


If you want to use it from source:

1. Install the dependencies manually:

```
pip install -r requirements.txt
```
2. Clone the repository:

```
git clone https://github.com/ranitajana/slay.git
```

3. Obtain the necessary API keys:
- OpenAI API key:
  - Visit [https://openai.com/] and sign up for an account.
  - Follow their instructions to generate an API key.
- Deepgram API key:
  - Visit [API Provider 2](https://api-provider-2.com) and sign up for an account.
  - Follow their instructions to generate an API key.

4. Create a configuration file:

- Open the file named `API.py` in the project root directory.
- Add the following content to `API.py`:
  ```python
  OpenAI_API_KEY = 'your-openai-api-key'
  Deepgram_API_KEY = 'your-deepgram-api-key'
  ```
- Replace `'your-openai-api-key'` and `'your-deepgram-api-key'` with your actual API keys obtained in step 3.

## Usage

Instructions for using your project go here.

## Contributing

Guidelines for contributing to your project go here.

## License


