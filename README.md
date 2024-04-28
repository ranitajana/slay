<div style="background-color: #f1f1f1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">

# slay

This is the codebase for an AI assisted teaching assistant 'Slay'.

The code takes the YouTube URL of a video lecture and a lesson plan as an input and returns the lecture-notes in structured format based on the lesson plan. It also auto-generates a set of quiz. 

## Try it out here :

[Click here](https://slay.unsupervized.com/)


## If you want to use it from source:

### Requirements

- Python 3.10 or higher
- OpenAI API key
- Deepgram API key

### Installation

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
  - Visit [OpenAI](https://openai.com/) and sign up for an account.
  - Follow their instructions to generate an API key.
- Deepgram API key:
  - Visit [Deepgram](https://deepgram.com/) and sign up for an account.
  - Follow their instructions to generate an API key.

4. Add your API keys in `API.py` file:

- Open the file named `API.py` in the project root directory.
- Add the following content to `API.py`:
  ```python
  OpenAI_API_KEY = 'your-openai-api-key'
  Deepgram_API_KEY = 'your-deepgram-api-key'
  ```
- Replace `'your-openai-api-key'` and `'your-deepgram-api-key'` with your actual API keys obtained in step 3.

### Use Jupyter notebook to use the teaching assistant

Run ```jupyter lab``` in terminal from the project root directory and open `slay.ipynb`. Follow the instructions in the Jupyter notebook to generate notes and quiz from the Youtube URL of the video lecture.


![Image of slay.ipynb](https://photos.app.goo.gl/AyyCtDB7KeekJfft8)   




