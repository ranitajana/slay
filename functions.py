#!/usr/bin/python
from pytube import YouTube
import re
import API as api
from deepgram import Deepgram
import openai
import json
import numpy as np

def download_audio(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Get the audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio
    print(f"Downloading audio: {yt.title}")
    audio_stream.download(filename="audio.mp3")
    print("Audio downloaded successfully!")

def save_transcript(transcript):
    with open('transcript.txt', 'w') as file:
        file.write(transcript)

def save_segments(segments, json_list):
    with open(segments, 'w') as jsonl_file:
        for json_obj in json_list:
            jsonl_file.write(json.dumps(json_obj) + '\n')

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"

def speech_to_text(input_audio_path):
    deepgram = Deepgram(api.DEEPGRAM_API_KEY)
    with open(input_audio_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        options = {'punctuate': True,
                'utterances': True,
                'diarize': True,
                'numerals': True}
        response = deepgram.transcription.sync_prerecorded(source, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']    
        words = response['results']['channels'][0]['alternatives'][0]['words']
        return transcript, words

def subtitle(transcript,words):
    # Split the transcript into sentences
    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    # Create subtitles in SRT format
    srt_subtitles = ''
    subtitle_count = 1
    word_index = 0

    for sentence in sentences:
        sentence_words = sentence.split()
        start_time = words[word_index]['start']
        end_time = words[word_index + len(sentence_words) - 1]['end']
    
        srt_subtitles += f"{subtitle_count}\n"
        srt_subtitles += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_subtitles += f"{sentence}\n\n"
    
        subtitle_count += 1
        word_index += len(sentence_words)

    # Save the subtitles to an SRT file
    #with open('subtitles.srt', 'w') as f:
        #f.write(srt_subtitles)
    return srt_subtitles

def lecture_notes(lesson_plan, transcript):
    openai.api_key = api.OpenAI_API_KEY
    # Prepare the prompt for GPT-3.5
    prompt = f"Given the following lesson plan:\n{lesson_plan}\n\nAnd the transcript:\n{transcript}\n\n Divide the whole transcript into paragraphs for each topic in the lesson plan and also add the timestamp for each topic. The heading of each topic should be exactly same as the corresponding point in the lesson plan. For each key topic write a paragraph, do not try to make itemized points."
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant. You answer what is asked without any introduction and followup narrative."},
        {"role": "user", "content": prompt}
        ],
        # max_tokens=1000,
        # n=1,
        # stop=None,
        temperature=0.
    )

    # Extract the generated notes from the API response
    structured_notes = response.choices[0].message.content
    return structured_notes

#