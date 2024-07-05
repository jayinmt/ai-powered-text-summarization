import argparse
import time
from typing import List
import requests
from bs4 import BeautifulSoup
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def scrape_text_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return " ".join([p.get_text() for p in soup.find_all("p")])
    except requests.RequestException as e:
        raise ValueError(f"Error fetching URL: {e}")

def summarize_text(text: str, model_name: str, max_length: int, min_length: int, do_sample: bool) -> str:
    try:
        if model_name == "t5-small":
            model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
            tokenizer = AutoTokenizer.from_pretrained("t5-small")
            summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        else:
            summarizer = pipeline("summarization", model=model_name)
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        return summary[0]["summary_text"]
    except Exception as e:
        raise ValueError(f"Error during summarization: {e}")

def display_summary(summary: str, style: str) -> None:
    if style == "bullet":
        summary_points = summary.split(". ")
        bullet_points = [f"- {point.strip().capitalize()}." for point in summary_points if point.strip()]
        print("\n".join(bullet_points))
    else:
        print(summary)

def main(args: argparse.Namespace) -> None:
    try:
        if args.url:
            text = scrape_text_from_url(args.url)
        elif args.text:
            text = args.text
        else:
            raise ValueError("Either --url or --text must be provided")

        if not text:
            raise ValueError("No text to summarize")

        start_time = time.time()
        summary = summarize_text(text, args.model, args.max_length, args.min_length, args.do_sample)
        end_time = time.time()

        print(f"\nSummary ({args.style} style):")
        display_summary(summary, args.style)
        print(f"\nSummary Length: {len(summary.split())} words")
        print(f"Execution Time: {end_time - start_time:.2f} seconds")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-Powered Text Summarization Tool")
    parser.add_argument("--model", type=str, default="sshleifer/distilbart-cnn-12-6", help="Transformer model to use for summarization")
    parser.add_argument("--text", type=str, help="Text to summarize")
    parser.add_argument("--url", type=str, help="URL of the webpage to summarize")
    parser.add_argument("--max_length", type=int, default=150, help="Maximum length of the summary")
    parser.add_argument("--min_length", type=int, default=50, help="Minimum length of the summary")
    parser.add_argument("--style", type=str, default="paragraph", choices=["paragraph", "bullet"], help="Style of the summary")
    parser.add_argument("--do_sample", action="store_true", help="Use sampling instead of greedy decoding")
    args = parser.parse_args()
    main(args)
