
# Voice Assistant

This is a Python-based voice assistant that can perform various tasks such as playing songs on YouTube, opening websites, searching the web, and fetching summaries from Wikipedia. The project utilizes several libraries to achieve these functionalities: `speech_recognition`, `pyttsx3`, `pywhatkit`, `webbrowser`, and `wikipedia`.

## Author

- **Muhammad Yousaf**
- **Email:** yousafsahiwal3@gmail.com

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `webbrowser`
  - `wikipedia`

You can install the required libraries using pip:

```sh
pip install speechrecognition pyttsx3 pywhatkit wikipedia
```

## How It Works

1. **Initialization**:
   - The script initializes the speech recognizer and the text-to-speech engine.

2. **Listening for Commands**:
   - The assistant listens for voice commands using the computer's microphone.
   - It processes the audio input to convert it into text using Google's speech recognition service.

3. **Handling Commands**:
   - Based on the recognized text, the assistant can:
     - Play a song on YouTube.
     - Open YouTube or Google in a web browser.
     - Perform a Google search.
     - Fetch a summary from Wikipedia.
   - If the command is not recognized, it prompts the user to try again.

4. **Continuous Interaction**:
   - The assistant continues to listen and respond to commands in a loop until the user says "exit" or "stop".

## Usage

1. **Run the Script**:
   - Execute the script using Python.

```sh
python voice_assistant.py
```

2. **Interact with the Assistant**:
   - After running the script, the assistant will greet you and start listening for commands.
   - Speak commands such as:
     - "Play [song name]"
     - "Open YouTube"
     - "Open Google"
     - "Search [query]"
     - "Who is [person]" or "What is [topic]"

3. **Exit the Assistant**:
   - To stop the assistant, say "exit" or "stop".

## Example Commands

- "Play Shape of You"
- "Open YouTube"
- "Open Google"
- "Search weather today"
- "Who is Albert Einstein"

## Notes

- Ensure your microphone is working and not muted.
- The assistant requires an internet connection for speech recognition and accessing online content.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README provides an overview of the project, instructions for setup and usage, and example commands to help users interact with the voice assistant effectively.
