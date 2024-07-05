# AI-Powered Text Summarization Tool

This Python script utilizes transformer-based models from the Hugging Face Transformers library to implement an advanced text summarization tool. The script provides functionality to input a text document or URL and produce a concise, coherent summary.

## Features

1. **Model Selection**: Incorporate options to select between different pre-trained models like BERT, GPT, or T5, showcasing the ability to implement and compare various AI models.
2. **Interactive User Input**: Allow users to input text directly or provide a URL to a webpage for summarization, demonstrating skills in handling and processing user inputs.
3. **Summarization Options**: Provide settings for the length of the summary, the style (e.g., bullet points or a paragraph), and whether to use sampling for generation.
4. **Command Line Interface (CLI)**: Implement a simple CLI that lets users interact with the script, providing options like help, version information, and settings via command line arguments.
5. **Performance Metrics**: Display metrics such as execution time and summary length, showing an understanding of performance evaluation in AI applications.
6. **Error Handling**: Robust error handling to manage common issues like network failures, invalid input, or model loading errors.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jaydxyz/ai-powered-text-summarization.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the AI-powered text summarization tool, run the script with the desired arguments:

```
python summarizer.py [--model MODEL] [--text TEXT] [--url URL] [--max_length MAX_LENGTH] [--min_length MIN_LENGTH] [--style {paragraph,bullet}] [--do_sample]
```

Arguments:
- `--model`: Transformer model to use for summarization (default: "sshleifer/distilbart-cnn-12-6").
- `--text`: Text to summarize.
- `--url`: URL of the webpage to summarize.
- `--max_length`: Maximum length of the summary (default: 150).
- `--min_length`: Minimum length of the summary (default: 50).
- `--style`: Style of the summary, either "paragraph" or "bullet" (default: "paragraph").
- `--do_sample`: Use sampling instead of greedy decoding.

Examples:
```
python summarizer.py --text "Your long text here..." --max_length 100 --style bullet --do_sample
```
```
python summarizer.py --url "https://example.com" --model t5-small --min_length 50
```

## Implementation Details

- **Language & Libraries**: Python, `transformers` for the AI model, `beautifulsoup4` and `requests` for scraping text from URLs, `argparse` for CLI implementation.
- **Model Deployment**: Use a lightweight model or distillation techniques if the focus is on speed and efficiency, or demonstrate the use of more complex models for better accuracy.
- **Error Handling**: The script now includes comprehensive error handling for various scenarios:
  - Network errors when fetching URLs
  - Invalid or missing input (text or URL)
  - Issues during model loading or text summarization
  - Timeout for URL requests to prevent hanging on slow or unresponsive websites

## Recent Improvements

1. Enhanced error handling and input validation
2. Added a timeout for URL requests
3. Improved bullet point formatting in the summary output
4. More informative error messages for different types of failures

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://requests.readthedocs.io/)
