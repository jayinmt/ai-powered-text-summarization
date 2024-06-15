import argparse
import time
from typing import List

import requests
from bs4 import BeautifulSoup
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def scrape_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return " ".join([p.get_text() for p in soup.find_all("p")])

def summarize_text(text: str, model_name: str, max_length: int, min_length: int, do_sample: bool) -> str:
    if model_name == "t5-small":
        model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
        tokenizer = AutoTokenizer.from_pretrained("t5-small")
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    else:
        summarizer = pipeline("summarization", model=model_name)

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]["summary_text"]

def display_summary(summary: str, style: str) -> None:
    if style == "bullet":
        summary_points = summary.split(". ")
        bullet_points = [f"- {point.capitalize()}." for point in summary_points]
        print("\n".join(bullet_points))
    else:
        print(summary)

def main(args: argparse.Namespace) -> None:
    if args.url:
        text = scrape_text_from_url(args.url)
    else:
        text = args.text

    start_time = time.time()
    summary = summarize_text(text, args.model, args.max_length, args.min_length, args.do_sample)
    end_time = time.time()

    print(f"\nSummary ({args.style} style):")
    display_summary(summary, args.style)

    print(f"\nSummary Length: {len(summary.split())} words")
    print(f"Execution Time: {end_time - start_time:.2f} seconds")

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
