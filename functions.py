#!/usr/bin/python
from pytube import YouTube
import re
import API as api
import openai
import json
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import io

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"

def speech_to_text(url):
        # Create a YouTube object with the video URL
        yt = YouTube(url)
        # Get the audio stream with itag 139
        audio_stream = yt.streams.get_by_itag(139)
        # Get the buffer data from the stream
        buffer_data = io.BytesIO()
        audio_stream.stream_to_buffer(buffer_data)
        # Reset the buffer's position to the beginning
        buffer_data.seek(0)
        deepgram = DeepgramClient(api.DEEPGRAM_API_KEY)
        payload: FileSource = {
            "buffer": buffer_data,
        }
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            punctuate = True,
            utterances = True,
            diarize = True,
            numerals = True
        )

        #Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        # response = deepgram.transcription.sync_prerecorded(payload, options)
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

    return srt_subtitles

def lecture_notes(lesson_plan, transcript):
    openai.api_key = api.OpenAI_API_KEY
    # Prepare the prompt for GPT-3.5
    prompt = f"Given the following lesson plan:\n{lesson_plan}\n\nAnd the transcript:\n{transcript}\n\n Divide the whole transcript into paragraphs for each topic in the lesson plan and also add the timestamp for each topic. The heading of each topic should be exactly same as the corresponding point in the lesson plan. For each key topic write a paragraph, do not try to make itemized points. Do not add 'the speaker' while writing the paragraph."
    token_size = len(transcript.split())
    if (token_size < 3000):
        model_name = 'gpt-3.5-turbo'
        maximum = 2000
    else:
        model_name = 'gpt-4-turbo'
        maximum = 4096
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

def ask_ques(notes,  max_retries=5): #, lesson_plan):
    retry_count = 0
    while retry_count < max_retries:
        # Prepare the prompt for GPT-3.5
        prompt = f"Given the following notes:\n{notes} generate 5 set of multiple option type questions and answers with 4 options for each question. Give the output in json format with each question, its 4 options and the right answer as one json object."
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
            #max_tokens= maximum,
            # n=1,
            # stop=None,
            temperature=0.
        )

        # Extract the generated notes from the API response
        questions = response.choices[0].message.content
        try:
            json.loads(questions)
            return questions
        except ValueError as e:
            retry_count += 1
    
    # If the function reaches this point, it means it failed to generate a valid JSON object after max_retries attempts
    return False

    
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
        
def show_quiz(ques, ans):
    count = len(ans)
    for i in range(count):
        print('Question:', ques[i][0])
        for i, option in enumerate(ques[i][1], start=1):
            print(f"{i}. {option}")
        print('\n')
        print('Correct answer:', ans[i], '\n')

    







