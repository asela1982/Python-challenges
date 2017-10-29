# * Import a text file filled with a paragraph of your choosing.

# * Assess the passage for each of the following:

#   * Approximate word count

#   * Approximate sentence count

#   * Approximate letter count (per word)

#   * Average sentence length (in words)

# ```
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4
# ```

import os

filepath = os.path.join(".","input.txt")

words_count = {}


with open(filepath) as fh: 
    # lines = fh.read() # read all the lines
    # print(lines)

    for row in fh:
        # print(row.split()) # split by whitespaces
        words = row.split()
        for word in words:
            if word in words_count:
                words_count[word] = words_count[word] + 1
            else:
                words_count[word] = 1

print(words_count)