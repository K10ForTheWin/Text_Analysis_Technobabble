# Text_Anlaysis_Technobabble
NLP (Natural Language Processing) Using Star Trek scripts as training data.

<p align="justify">
Using the website http://chakoteya.net/StarTrek/index.html, which contains formatted scripts from all five Star Trek series, this program downloads all the webpages into text files, sanitizes and preprocessing those scripts to extract character names and dialogue from the text, and models the dialogue of the top 100 characters (as ranked by lines spoken) into word clouds of the speaker.  Word Clouds graphically represent most spoken words in both size and colour, with larger font sizes indicating higher frequencies and darker colours representing desner allocations of words within the text.
</p>

<img src="https://user-images.githubusercontent.com/43615563/55239413-a306f600-5204-11e9-95d5-38bdc4dd8716.png" width="100%"/>


htm-process.py
-Uses line comphrehensions to generate urls for series using episode number ranges.
-Uses BeautifulSoup to get the contents of the webpage, writes to plain text files

ProcessAllScripts-2.py
-Concatenates multiline character dialogue into single lines
-Saves character's spoken lines into dictionary where character name is the key and value is the dialogue
-Creates folder data_char_lines to store each series as a folder and each character's dialogue as a file within the appropriate series folder

FilterFiles.py
-Uses file size to calculate a cutoff point for character files to keep
-Natural cutoff occurs at top 100 characters

processWords.py
-loads in stopwords list (words to be removed from analysis) from nltk standard package and personal, curated list of stopwords collected through NLP projects in school
-Removes stopwords and punctuation from dialogue
-Counts words, sorts by count
-Makes a Word Cloud image of top words using Python package wordcloud

