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


![Image of slay.ipynb](https://lh3.googleusercontent.com/pw/AP1GczM8QylyHh7pdW8UjZDypftYmtYvU-eBsx2SBuO2Kc7XR373Pv98uy30oLVfYjbdIrFi_nFga7hMC7kaQONg5z8WE8n9bkfBWSs28qjNDhQvOnuZ35hv80tSlZ87yKZxBkfZMzguhy8rEHHMmQXnN9tQKyS-8KU1wMNElaQHlh_UCP_soAYLonRdf0LnyV_yndIRtlKSfYhebg-AO46JLWg2t1uTQSs6kRvOeyCkpyWH4NHSNBMOchSxvQDVrFeKsdLBcvnWSbrLyvwfYIWhNKYX5dulFZvCVkJk01VePmnKAiDfjz55ZM_CegGs5a6gU3W6XZGkd3BzocZ7__GR2KeWy1ZdVDo7AQiKydOAEe_aL5EuKoKlyF9F3F93tYA3OlWS8S-Bbzv2NvUShnyVaWulodAr2I3TwP3mKWtuqjugOO1WMJyuE60uLvB7h2YNLS8ShRQ2hcZwWLbyiJZ0AsN-SOqvVE1_8DhB_Oagjm0eJN2pH22F_PdvNmlOw0quNK-O3IytHDlnQsk2X9AyWlU0Gq7tppiKAmHuHf-GNZm8THqb_Tjy2gBLa5oQRjlx3dgwLizES1YjvTix-T4ZugzWwLnSMeAd6Vwe9MOLLajRGdyDPA-KZtJN0e60G1XNZrfxZKyeJ4PBToItSAqXNqIAcgRNxM2RXVpZ8tu3zJS50ZSGv2MMOpMMtCl_t2XjzFRhnXshCX5o2VGVFxjMmbq0_AO9toqEur0-DKuKtO1r-q37WrP4_Lcur-SvBXtCM-GdWb2dZwMWPGITAstKuhi6UFZWRrUJQSAgWSHNFUqPZMTyVnv88D97KShz3YUboxOsFjqtvTSh--Lo3oU17bl-FhCyHmtOtdise0qp_PHComtFEdejcBHAN9ejcKH1-7Mdx6bvkO6wtquUXAz0LODPZ8fiMsjZ0permpZXXLbBc25h5JgUq3dn6tSNLYa3JZ7jHpJedNRS71FU6lxoFeyIixGpySUzmbtqFB9vXgs0PFgcTBQTWY_iqdJm3ajW58UWXdsCzyfHtOn_HsLJv4oKYr87dBWpIT0JpnhyWv8RkWCqhOEuWVuBByOY23Nu5iNWbkmWmA=w2370-h1562-s-no-gm?authuser=1)   




