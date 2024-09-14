import asyncio
import edge_tts
import re


# Change these variables according to your needs
TEXT_FILE = "file.txt"  # Your text file
VOICE_MALE = "lo-LA-ChanthavongNeural"  # Male voice
VOICE_FEMALE = "lo-LA-KeomanyNeural"  # Female voice


def get_first_paragraph(text: str) -> str:
    """Extracts the first paragraph from the text."""
    paragraphs = text.split("\n\n")  # Split text into paragraphs
    return paragraphs[0] if paragraphs else ""


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to remove invalid characters."""
    return re.sub(r'[\/:*?"<>|]', "", filename)  # Remove illegal characters for filenames


async def amain(text: str, output_file: str, voice: str) -> None:
    """Main function to convert text to speech"""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


if __name__ == "__main__":
    # Choose between male and female voice
    use_male_voice = False  # Change to True for male voice
    selected_voice = VOICE_MALE if use_male_voice else VOICE_FEMALE

    # Read text from file
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract the first paragraph
    first_paragraph = get_first_paragraph(text)

    # Sanitize the first paragraph to use as the output filename (limited to 50 characters)
    output_filename = sanitize_filename(first_paragraph[:50].strip()) + ".mp3"

    # Run the TTS process
    asyncio.run(amain(first_paragraph, output_filename, selected_voice))

    print(f"{output_filename}")
