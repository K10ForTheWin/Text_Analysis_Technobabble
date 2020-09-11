# Text_Anlaysis_Technobabble
### NLP (Natural Language Processing) Using Star Trek scripts as training data.

<p align="justify">
Using the website http://chakoteya.net/StarTrek/index.html, which contains formatted scripts from all five Star Trek series, this program downloads all the webpages into text files, sanitizes and preprocessing those scripts to extract character names and dialogue from the text, and models the dialogue of the top 100 characters (as ranked by lines spoken) into word clouds of the speaker.  Word Clouds graphically represent most spoken words in both size and colour, with larger font sizes indicating higher frequencies and darker colours representing desner allocations of words within the text.
</p>

<img src="https://raw.githubusercontent.com/K10ForTheWin/Text_Analysis_Technobabble/master/wordcloud_out/Barclay.png" width="100%"/>

### Python file descriptions

### htm-process.py
  - Call this method first to scrape website for scripts
  -Uses line comphrehensions to generate urls for series using episode number ranges.
  -Uses BeautifulSoup to get the contents of the webpage, writes to plain text files

### ProcessAllScripts-2.py
  - Extracts lines of dialogue from full script, ignoring erroneous text
  - Concatenates multiline character dialogue into single lines
  - Saves character's spoken lines into dictionary where {key: value} are represented as {character_name: lines_of_dialogue}.
  - Generates content for data_char_lines, with a folder per series with character's dialogue as text files stored within the folder.

### FilterFiles.py
  - Uses file size to calculate a cutoff point for character files to keep
  - Natural cutoff occurs at top ~100 characters

### processWords.py
  - Uses files in resources/ folder to create stopwords list (words to be removed from analysis) from nltk standard package and personal, curated list of stopwords collected       through NLP projects in school.
  - Removes stopwords and punctuation from words dictionary.
  - Create word frequency dictionary per character.
  - Generates a Word Cloud image of top words for files listed in char_lines_top_100

