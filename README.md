# Assignment 11 - Gemini Essay PDF Generator

A Python application that uses Google's Gemini AI to generate academic essays from research questions and save them as properly formatted PDF documents.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project leverages Google's Gemini AI API to create comprehensive academic essays based on user-provided research questions. The application generates well-structured essays in markdown format with academic sections (abstract, introduction, theory, analysis, conclusions, and references), then converts them to professional-looking PDF documents.

## Requirements

- Python 3.8+
- Google Gemini API key
- Internet connection for API access

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:
    ```bash
    cd ass_11
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your Google Gemini API key:
    ```bash
    export GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

Run the application to generate essays:

```bash
# Execute the main script
python main.py
```

## Features

- Generate academic essays from research questions.
- Convert markdown essays to PDF format.
- Automatically structure essays with academic sections.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).