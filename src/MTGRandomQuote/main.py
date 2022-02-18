#!/usr/bin/env python3
from colorama import init, Style
import sqlite3
import sys
from pathlib import Path
import os


def main():
    init()
    try:
        conn = sqlite3.connect(Path(__file__).with_name("flavor.sqlite"))
    except Exception as e:
        print(f"Something went wrong: {e}")
        sys.exit(1)
    cursor = conn.cursor()
    cursor.execute("SELECT name,flavor FROM flavor ORDER BY RANDOM() LIMIT 1")
    (name, flavor) = cursor.fetchall()[0]
    print("-" * os.get_terminal_size().columns)
    print(f"'{flavor}'\n{Style.DIM} {name}")
    print("-" * os.get_terminal_size().columns)
    conn.close()


if __name__ == "__main__":
    main()
