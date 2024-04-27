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
    prompt = f"Given the following lesson plan:\n{lesson_plan}\n\nAnd the transcript:\n{transcript}\n\n Divide the whole transcript into paragraphs for each topic in the lesson plan and also add the timestamp for each topic. The heading of each topic should be exactly same as the corresponding point in the lesson plan. For each key topic write a paragraph, do not try to make itemized points. Do not add 'the speaker' while summarising, just summarise the content."
    token_size = len(transcript.split())
    if (token_size < 3000):
        model_name = 'gpt-3.5-turbo'
        maximum = 1000
    else:
        model_name = 'gpt-4-turbo'
        maximum = 4000
    response = openai.ChatCompletion.create(
        model = model_name,
        messages=[
        {"role": "system", "content": "You are a helpful assistant. You answer what is asked without any introduction and followup narrative."},
        {"role": "user", "content": prompt}
        ],
        max_tokens=maximum,
        # n=1,
        # stop=None,
        temperature=0.
    )

    # Extract the generated notes from the API response
    structured_notes = response.choices[0].message.content
    return structured_notes

def ask_ques(notes): #, lesson_plan):
    # Prepare the prompt for GPT-3.5
    #prompt = f"Given the following lesson plan:\n{lesson_plan}\n\nAnd the transcript:\n{lesson_plan}\n\n "
    prompt = f"Given the following notes:\n{notes} generate 5 set of multiple option type questions and answers with 4 options for each question. Give the output in json format with each question, its 4 options and the right answer as one json object. "
    token_size = len(notes.split())
    if (token_size < 3000):
        model_name = 'gpt-3.5-turbo'
        maximum = 1000
    else:
        model_name = 'gpt-4-turbo'
        maximum = 1000
    response = openai.ChatCompletion.create(
        model = model_name,
        messages=[
        {"role": "system", "content": "You are a helpful assistant. You answer what is asked without any introduction and followup narrative."},
        {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        # n=1,
        # stop=None,
        temperature=0.
    )

    # Extract the generated notes from the API response
    questions = response.choices[0].message.content
    return questions


def save_ques(questions):
    parsed_data = json.loads(questions)
    # Initialize lists to store questions, options, and answers
    questions_options = []
    answers = []
    # Iterate over each question
    for question_data in parsed_data['questions']:
        question = question_data['question']
        options = question_data['options']
        answer = question_data['answer']
        # Append a tuple containing the question and options to the questions_options list
        questions_options.append((question, options))
        # Append the answer to the answers list
        answers.append(answer)
    return questions_options, answers
    
    
    
    
    
# def save_ques(questions):
#     data = json.loads(questions)

#     # Initialize arrays to store questions, options, and answers
#     questions_options = []
#     answers = []

#     # Iterate over each question in the JSON data
#     for question_data in data['questions']:
#         question = question_data['question']
#         options = question_data['options']
#         answer = question_data['answer']
#         # Append the question and options to the 2D array
#         questions_options.append([question] + options)
#         # Append the answer to the answers array
#         answers.append(answer)

#     return questions_options, answers 

    
# def save_ques(questions): 
#     # Load the JSON data from the string
#     data = json.loads(questions)

#     # Open the files for writing
#     with open('questions.jsonl', 'w') as questions_file, open('answers.jsonl', 'w') as answers_file:
#         # Iterate over each question in the JSON data
#         for question in data['questions']:
#             # Extract the question and options
#             question_text = question['question']
#             options = question['options']
        
#             # Create a dictionary for the question and options
#             question_data = {
#                 'question': question_text,
#                 'options': options
#             }
        
#             # Write the question and options to the questions.jsonl file
#             questions_file.write(json.dumps(question_data) + '\n')
        
#             # Extract the answer
#             answer = question['answer']
        
#             # Write the answer to the answers.jsonl file
#             answers_file.write(json.dumps(answer) + '\n')