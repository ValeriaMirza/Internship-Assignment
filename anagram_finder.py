import os
from collections import defaultdict

def find_anagrams(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    if not os.path.exists(file_path):
        print(f"Error: File '{filename}' not found in {script_dir}")
        return

    anagram_groups = defaultdict(list)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            if word.isalpha():
                sorted_word = ''.join(sorted(word))
                anagram_groups[sorted_word].append(word)

    for group in anagram_groups.values():
        print(" ".join(group))

if __name__ == "__main__":
    find_anagrams("sample.txt")
