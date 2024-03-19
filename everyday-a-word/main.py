import os
import numpy as np

from blessed import Terminal
from datetime import datetime

from functions.datasets import read_verbs
from utils.terminal import print_pretty_window
from functions.database import return_the_word_day, set_the_word_day, return_all_words

current_date = datetime.now().strftime("%d/%m")

word = return_the_word_day(current_date)
verbs = read_verbs()

if word == "No word for today.":
    # Filtering the verbs
    non_zero_verbs = verbs[verbs['count'] > 0]
    non_zero_verbs = non_zero_verbs.sort_values(by='count', ascending=False)
    non_zero_verbs = non_zero_verbs.reset_index().drop("index", axis=1)

    # Getting the bottom 100 verbs
    bottom_100_verbs = non_zero_verbs.tail(100).reset_index().drop("index", axis=1)

    already_setted_words = return_all_words()
    bottom_100_verbs = bottom_100_verbs[~bottom_100_verbs['1p.prs'].isin(already_setted_words)].reset_index(drop=True)
    
    idx_selected = np.random.choice(range(100), 1)

    selected = bottom_100_verbs.loc[idx_selected, :].reset_index().drop("index", axis=1)

    set_the_word_day(current_date, selected.loc[0,'1p.prs'])

else:
    selected = verbs[verbs["1p.prs"] == word].reset_index().drop("index", axis=1)

if __name__ == "__main__":
    term = Terminal()
    os.system("cls")

    
    title = f"Everyday a word - {current_date}"

    subtitle = f"The word of the day is: {selected.loc[0,'1p.prs']}.\n"
    
    content = [
        f"third person present: {selected.loc[0,'1p.prs']}",
        f"the first person past: {selected.loc[0,'1p.pst']}",
        f"the third person past: {selected.loc[0,'3p.pst']}"  
    ]

    with term.fullscreen():
        with term.cbreak():
            print_pretty_window(term, title, subtitle, content)
            term.inkey()