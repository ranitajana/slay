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


![Image of slay.ipynb](https://lh3.googleusercontent.com/pw/AP1GczNhJrQRT8HaklrmszSl2qKgHgasBCxjymeRmwkDCd4N3lE7tybw0_X5uu5ilgRNyOGd_j4E0_FHQoM6hazA42ZSKJgNu0EE900glkPjvidiarHpfrPNQFCz0j3bwlrWHQmrE8E2mvEE1if-TkOHtrqWPzIVLYDCtL24NvEJqa8VlDZHxgsbXdug7XcO5CYqYzZ1_6M8onjQhDYDYjaZW4CWQJYCo-6YdE3cdGW-FHnoeUURFuHihrIXlNrFFtzNpzoXfwXYrvS2DjBC6i3zbTgO9l7xRju6Mz_ZaXJhfKetFbL4Qp-RF0RfIa2oYV66yNSVCbyzmGpgkSYpbCMJkyqNybUlFsBExVG7U5sGCMa8SyCHjlFdPiZltCZDDpaNoDt7OqVjqMzpaMvCNpJiQrYHzZutSUeOPXhog_eBjNnkFUwfN2TFPFNPDcMt_8Z2ffeC_uOibmd36hNv5I1URhEe_QZDjZCtRAVaItDnzLDtMaEVe3F3ptlNydJLoIwwhTPDhZSGKZA0av6_LhO9ZbJL0lKIytjtNpDN8TR_op8toIyKmzmPQE0MkLjhJ7kxOb4c97HusxMA3pCg5uhPfi5hFRXU3iDqo1MZ5HuC85Qh3YZbDWRbqJnWtOmQhsXfsdQtr3bJ9nzZ7y4USm1rTcaVHGsRe0Y3WRsznuhjMj0F8XujgsGxBNbZCclbPrh6RV1z2DYmRNjNP8j3YL_UhcZx_gPeiERaRL-cCCw3CO1pz75KdAjGLC0TJPFf_o7ZXiVJKJI6DBUOPb2LmqbkLHib-klRdSUycIc68dHQ1O_eHDLupw47rAwzfHhWDwb0PghMBnPighxIeqrZZ1Z2zCvJeIcjl2zYtw4U1CDji80HiMKOE4c_LcilsU-kVx4BK-CUF3AWZKBbJFWxybD3e5ASEed9vMNYPKjyRxT8ixAM4AMGr3Y19heEmYovZhkx_foytjtoYr38XTFFVQlSGVDnXU27ukhnzt-QZeCjngwg45Wi77QoQveZVu27bbKVASY-W9U1ZzqwG06l4T3-s0f1sbAkqYiirLW9u6SXqjXll35H4uZdxZUgLYNBL3Y-8VZSAgBO=w2372-h1528-s-no-gm?authuser=1)   




