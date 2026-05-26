import ollama


def generate_questions(role):

    try:

        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': f'Generate 5 interview questions for {role}'
                }
            ]
        )

        return response['message']['content']

    except Exception as e:

        return str(e)


def analyze_resume(text):

    try:

        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': f'Analyze this resume:\n{text}'
                }
            ]
        )

        return response['message']['content']

    except Exception as e:

        return str(e)


def evaluate_answer(answer):

    try:

        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': f'Evaluate this answer:\n{answer}'
                }
            ]
        )

        return response['message']['content']

    except Exception as e:

        return str(e)