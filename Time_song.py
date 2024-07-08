import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Aku berbeda darimu", 0.1, False),
        ("Berhenti !", 0.1, False),
        ("Aku benci kebohongan itu", 0.1, False),
        ("Kau tak harus jadi sosok yang ideal", 0.08, False),
        ("Aku hanya ingin kau mengerti ", 0.11, False),
        ("Aku bahkan tak memiliki harapan apapun", 0.08, False),
        ("Aku tak ingin membohongi diriku sendiri", 0.08, False),
        ("Maaf!", 0.08, True),
    ]

    delays = [0.8, 0.5, 0.5, 0.5, 0.7, 0.5, 0.5, 2.7]

    for i, (line, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[91m", end='')  

        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        if is_colored:
            print("\033[0m", end='')  

        time.sleep(delays[i])
        print('')

print_lyrics()
