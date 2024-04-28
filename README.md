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


![Image of slay.ipynb](https://lh3.googleusercontent.com/pw/AP1GczOzxWP3cZzMJJAc8qXImQZ13dmmpbINANU7AHc2f-NhPjeMBEUD48X1YiyU_3XW3HN8i7wMoerXknbbeWdrkGVp7y5DTfnkKftNIdLpmM3jNDC8lC3u3xZlalyXDukTqoPwJ1YrGPsWgP6zi8eVjVuoR9CJPC5bauVHozMmhusJmmm6uZdEMmOmH5bXCR6Hhnk242NDoUCBql7bhjgZ1qr4TLju85h69LCrccUKx4Tv17kTNprwigtZj2_mRYouNmVAFMiWLf4N0scXKRIWyHR09tNx3Y8fsdHpns7UNLjBTEnE0d4VLY5aUmJMoO_VN02P0lcUA9JDALvkqvPDdRl59wGl6uckW3OHRQBy6m23Si0oXweHBrTZWHmGTU8-nammY8jixJ5yZ1st1zgUks5esdauk1neKfCCmIV1j40i_KuXMA5Lv_kXnfFYPhEveedwGxFGf17-HlEKZMhANIeUnj7_7zRiwrRMAM-N-WrACdl2XbVBW0FysKILwbZgLTO3vMffmhLD-BfrWnp_C8w8t3-LLo8wrOYwpfIWBX0cHpmkhrObtvKIE_jC5zihxex3AXx25VYycakwQBLBHCKETmK2gJ83fU98CXpixmFwknWknGsgAdSZeWGeEnyYOi688LTgYp66y3I-joaV6AgB8cqUKQM6YiReott4EdQdu3968oACtMcattu4FLew_TLXgdSg-ZPZLPb1hncK-J5-5oSV-sgP38tARXtMbaR2vPw0ABKKEe765klAdGR9rArgCkHSBqM1XCgMc6KdCuioipcq3NU6Rc2GURrdl3-eCL4xB1MfWcbInoMIfCVEs9K2V00pLgyHEi8ySetXZagaj-xpojvbPdQRz8WG223P3Ij-9gbmb8JZsyQkzcBJ6-OH6LeELWRSRHEGHXHRQduqAJVvQqScVL5e_FJahtThHILGEC3X4kMnYq_nSRkfWV7uPamiC3PWOhta_9ztZsdAxe44rCaVDO36HRv8R9g-Ypd4zA2jk7nZfQl7rllIVkZo0iWFxHxu4gtrzyKM6iFNzXzaEVQMmMmdOOoaZM2pYmo-vKChdlaaeYmSN6uv3ecKmDvTdQ=w2370-h1562-s-no-gm?authuser=1)   




