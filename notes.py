#!/usr/bin/env python3

from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

file_path = './transcript.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

transcript = file_content

entrepreneur = Agent(
	role = "Note taker",
	goal = "Take notes of the business opportunities discussed in the video transcript and list the top skills needed to execute it",
	backstory = "You are an experienced entrepreneur with 20 years of\
	experienced in entrepreneurship, you are a programer and excellent marketer,\
	you have a deep understanding of what it takes to build a business",
	verbose = True,
	allow_delegation = False,
	)


write_notes = Task(
	description = f"Write notes based on the video transcript: '{transcript}'.",
	agent = entrepreneur,
	expected_output = "detailed notes of all the business opportunities discussed in the transcript and the main skills involved to execute them"

	)

crew = Crew(
	agents = [entrepreneur],
	tasks = [write_notes],
	verbose = 2,
	process = Process.sequential

	)

output = crew.kickoff()

print(output)