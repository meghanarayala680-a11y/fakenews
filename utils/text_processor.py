# text_processor.py

"""
This module provides functions for processing and analyzing news text and URLs.
"""

import re
import requests
from urllib.parse import urlparse


def clean_text(text):
    """
    Cleans the input text by removing unnecessary characters.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text


def extract_urls(text):
    """
    Extracts URLs from the given text using regex.
    """
    url_pattern = r'(https?://[\w-]+(\.[\w-]+)+(/[^\s]*)?)'
    return re.findall(url_pattern, text)


def analyze_urls(urls):
    """
    Analyzes a list of URLs, returning their domain names.
    """
    domains = []
    for url in urls:
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc
        if domain not in domains:
            domains.append(domain)
    return domains
