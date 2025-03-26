from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import pathlib
import json

load_dotenv()

Gemini_API_Key = os.getenv("API_KEY")

client = genai.Client(api_key=Gemini_API_Key)

def get_grades(file_path):
    filepath = pathlib.Path(file_path)

    prompt = """The First page of the document attached is the question paper, and all the pages that follows ahead is the answer-sheet given to you by a student, you are an assistant teacher and you have to analyze the the pdf according to these rules:
    
    1. If a question is not attempted, marks obtained for that question will be 0
    2. Ignore the order of the question, but make sure to read the answer number currosponding to the question
    3. The answer numbers tells you what question is being answered in that answer.

    return a single line in format [example]: { totalQuestions: 4, totalMarks: 20, obtainedMarks: 20, marksPerQuestion : { q1: 5, q2: 5, q3: 5, q4: 5 } } return it as a single line string.
    """

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
        ),
    prompt])

    l = len(response.text)
    data = response.text[7: l-4]

    jsonData = json.loads(data)

    return jsonData


