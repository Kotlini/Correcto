from pandas._config import dates
from pynput import keyboard
from tkinter import Tk

import plotly.graph_objs as go
import pandas as pd

import api.OpenIA
import utils.Utils

def on_press(key):
    if key == keyboard.KeyCode.from_char('\r'):
        text = get_selected_text()
        utils.Utils.replace_text(api.OpenIA.correcto(text))


def get_selected_text():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.ctrl_l)
    controller.press('c')
    controller.release('c')
    controller.release(keyboard.Key.ctrl_l)
    root = Tk()
    selected_text = root.clipboard_get()
    root.destroy()
    return selected_text

documents = ['Doc 1', 'Doc 2', 'Doc 3', 'Doc 4', 'Doc 5', 'Doc 6', 'Doc 7', 'Doc 8', 'Doc 9', 'Doc 10']

lex_errors = [4, 5, 6, 4, 7, 8, 3, 5, 6, 2]
punct_errors = [2, 1, 3, 4, 2, 3, 2, 5, 1, 3]
grammar_errors = [1, 2, 0, 3, 4, 2, 5, 1, 2, 3]

fig = go.Figure()
fig.add_trace(go.Bar(x=documents, y=lex_errors, name='Lexical Errors'))
fig.add_trace(go.Bar(x=documents, y=punct_errors, name='Punctuation Errors'))
fig.add_trace(go.Bar(x=documents, y=grammar_errors, name='Grammar Errors'))

fig.update_layout(title='Error Rates by Document',
                  xaxis_title='Documents',
                  yaxis_title='Error Rates')

fig.show()

fig2 = go.Figure(data=[go.Histogram(x=lex_errors)])
fig2.update_layout(title='Lexical Error Distribution',
                   xaxis_title='Error Rate',
                   yaxis_title='Count')
fig2.show()

df = pd.DataFrame({'Document': documents, 'Lexical Errors': lex_errors, 'Punctuation Errors': punct_errors, 'Grammar Errors': grammar_errors, 'Date': dates})

fig3 = go.Figure()

for col in df.columns[1:4]:
    fig3.add_trace(go.Bar(x=df['Document'], y=df[col], name=col))

fig3.update_layout(title='Error Rates by Document',
                   xaxis_title='Documents',
                   yaxis_title='Error Rates')

fig3.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label='All Dates',
                     method='update',
                     args=[{'visible': [True, True, True]},
                           {'title': 'Error Rates by Document',
                            'xaxis': {'title': 'Documents'},
                            'yaxis': {'title': 'Error Rates'}}]),
                dict(label='2022-01-01 to 2022-01-05',
                     method='update',
                     args=[{'visible': [True, True, True, False, False, False, False, False, False, False]},
                           {'title': 'Error Rates by Document (Jan 1-5)',
                            'xaxis': {'title': 'Documents'},
                            'yaxis': {'title': 'Error Rates'}}]),
                dict(label='2022-01-06 to 2022-01-10',
                     method='update',
                     args=[{'visible': [False, False, False, True, True, True, True, True, True, True]},
                           {'title': 'Error Rates by Document (Jan 6-10)',
                            'xaxis': {'title': 'Documents'},
                            'yaxis': {'title': 'Error Rates'}}])
            ]),
            showactive=True
        )
    ])

fig3.show()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
