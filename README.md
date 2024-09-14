# Text-to-speech-Lao 
 Text to speech Lao 


Key Features:
Extracting the First Paragraph: The function get_first_paragraph splits the text into paragraphs using two consecutive newlines (\n\n). The first paragraph is selected.

Filename Sanitization: The sanitize_filename function removes characters that are illegal in filenames, such as \/:*?"<>|. This ensures that the extracted text can be safely used as a file name.

Filename Limitation: The output file name is limited to the first 50 characters of the paragraph to avoid overly long file names.

Voice Selection: The script still allows switching between male and female voices based on the use_male_voice toggle.

Output:
Audio File Name: The first 50 characters of the first paragraph from the text file will be used as the output MP3 file name.
This should meet your need for extracting the first paragraph and using it as the output file name.
