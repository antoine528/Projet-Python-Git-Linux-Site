import dash
import dash_core_components as dcc
import dash_html_components as html
import random

app = dash.Dash(__name__)

questions = [
    {
        'question': 'Is Python a compiled language?',
        'answer': 'No'
    },
    {
        'question': 'Does Python support multiple inheritance?',
        'answer': 'Yes'
    },
    {
        'question': 'Does Git require an internet connection?',
        'answer': 'No'
    },
    {
        'question': 'Can you use Git without a remote repository',
        'answer': 'Yes'
    },
    {
        'question': 'Can you use the Linux command line to create a new file?',
        'answer': 'Yes'
    },
    {
        'question': 'Can you change the permissions of a file in Linux?',
        'answer': 'Yes'
    },
    {
        'question': 'Does Linux have a graphical user interface?',
        'answer': 'Yes'
    },
    {
        'question': 'Can you use Linux on a Mac computer?',
        'answer': 'Yes'
    },
    {
        'question': ' Does Linux support virtualization?',
        'answer': 'Yes'
    },
    {
        'question': 'Can you use Linux to run a web server?',
        'answer': 'Yes'
    },
    {
        'question': 'Is Linux more secure than other operating systems?',
        'answer': 'It is generally considered to be more secure'
    },
    {
        'question': 'Is Python case-sensitive? ',
        'answer': 'Yes'
    },
    {
        'question': 'Can you use Python to work with databases?',
        'answer': 'Yes'
    },
    {
        'question': 'Is Python suitable for scientific computing?',
        'answer': 'Yes'
    },
    {
        'question': 'Can you use Python for machine learning?',
        'answer': 'Yes'
    },
    {
        'question': 'What is the linux command to create a directory named test?',
        'answer': 'mkdir test'
    },
    {
        'question': ' What is the linux command to go into a directory named test?',
        'answer': 'cd test'
    },
    {
        'question': 'How to display your current location using Linux?',
        'answer': 'pwd'
    },
    {
        'question': 'Check the current git status?',
        'answer': 'Git status'
    },
    {
        'question': 'What is the commande to stage all the files at once?',
        'answer': 'Git add .'
    }
]

current_question = random.choice(questions)
app.layout = html.Div([
    html.H1('Quiz'),
    html.H2(id='question', children=current_question['question']),
    dcc.Input(id='answer', type='text', value=''),
    html.Button('Submit', id='submit'),
    html.Button('Random Question', id='random'),
    html.Div(id='answer-response')
])

@app.callback(
    dash.dependencies.Output('answer-response', 'children'),
    [dash.dependencies.Input('submit', 'n_clicks')],
    [dash.dependencies.State('answer', 'value')])
def check_answer(n_clicks, answer):
    if answer.lower() == current_question['answer'].lower():
        return html.Div('Correct!')
    else:
        return html.Div('Incorrect, try again.')

@app.callback(
    dash.dependencies.Output('question', 'children'),
    [dash.dependencies.Input('random', 'n_clicks')])
def random_question(n_clicks):
    global current_question
    current_question = random.choice(questions)
    return current_question['question']


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
