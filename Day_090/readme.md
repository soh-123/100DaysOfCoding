# Read My File

Read My File is an application designed to convert text files into audio and save them as audio files. This project utilizes the `gtts` (Google Text-to-Speech) library to convert the text content of various file formats into spoken words.

## Features
- **File Upload**: Users can upload text files in various formats such as PDF, DOCX, DOC, and TXT.
- **Text-to-Audio Conversion**: The application extracts the text content from the uploaded file using the `PyPDF2` library (specifically for PDF files) and converts it into an audio file using the Google Text-to-Speech service.
- **Language Selection**: The application supports text-to-speech conversion in different languages. Currently, the default language is set to English (`lang='en'`), but it can be easily customized to support other languages.
- **Output Audio File**: The generated audio file is saved as "welcome.mp3" in the `Day_090` directory, providing a convenient way for users to access and listen to the converted text.
- **User-friendly Interface**: The graphical user interface (GUI) allows users to interact with the application easily. They can upload files, initiate the conversion process, and receive status updates.

## Installation
To run the Read My File application, make sure you have the following dependencies installed:
- `gtts` library: Install using `pip install gtts`.
- `tkinter` library: Usually comes pre-installed with Python.
- `PyPDF2` library: Install using `pip install PyPDF2`.

Clone this repository to your local machine and run the script `read_my_file.py` using Python.

## Contributing
Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgements
This project utilizes the following libraries:
- [gtts](https://gtts.readthedocs.io/): A Python library for Google Text-to-Speech API.
- [tkinter](https://docs.python.org/3/library/tkinter.html): Python's standard GUI package.
- [PyPDF2](https://pythonhosted.org/PyPDF2/): A library for reading and manipulating PDF files.

Special thanks to the contributors and the open-source community for their valuable contributions.
