import requests
from PyPDF2 import PdfWriter

# 
web_link = 'https://api.stackexchange.com/2.3/questions?site=stackoverflow&pagesize=50&sort=votes'

# Send a GET request to the endpoint to fetch the questions
res = requests.get(web_link)

if res.status_code == 200:
    # Assuming the response is in JSON format
    data = res.json()

    if 'questions' in data:
        questions = data['questions'][:50]  # fetch the first 50 questions

        # Create the pdf writer object
        pdf_writer = PdfWriter()

        # generate the pdf with numbered questions
        for i, question in enumerate(questions, 1):
            pdf_writer.add_page()
            pdf_writer.drawString(10, 800, f'Question {i}: {question}')

        # Save the PDF to a file
        endpoint_file = 'questions.pdf'
        with open(endpoint_file, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f'Cohort 4 endpoint file successfully saved {len(questions)} questions in "{endpoint_file}".')
    else:
        print('The API response does not contain a "questions" key.')
else:
    print('Cohort 4 you failed to fetch questions. Please check your endpoint URL.')
