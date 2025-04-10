# Internship-Assignment

# Anagram Finder

This Python script groups anagrams from a given text file and prints them out as groups of words that share the same letters. It reads the input file line by line, processes each word, and groups anagrams by sorting the characters in each word.

## Features
- Reads a file containing words, one word per line.
- Groups words that are anagrams of each other.
- Prints each group of anagrams on a separate line.
- Simple and easy-to-understand code structure.

## Requirements
- Python 3.x
- UTF-8 encoded text file containing words (one per line)

## Usage
Ensure that your input file (e.g., `sample.txt`) is in the same directory as the Python script or specify the full file path.

To run the script, use the following command:

```
python anagram_finder.py
```

This will output the anagram groups in your terminal, where each group of anagrams is printed on a single line.

## Example
### Input file (`sample.txt`):
```
act
cat
tree
race
care
acre
bee
```
### Output:
```
act cat
acre care race
tree
bee
```

## Explanation of the Code
1. The script starts by determining the absolute path of the provided input file.

2. It opens the file and reads it line by line. Each word is stripped of whitespace, converted to lowercase, and checked to ensure it consists of alphabetic characters only.

3. For each valid word, the characters are sorted alphabetically to generate a "key" for grouping anagrams.

4. All words with the same sorted key are stored in a defaultdict(list) to group them together.

5. Finally, the script prints each anagram group on a new line.

## Error Handling
If the specified file is not found, an error message is displayed with the file path.

