#!/usr/bin/env python3
"""
URL Shortener - CLI
A simple URL shortening service using hash-based codes.
"""

import hashlib
import os

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.reverse_map = {}

    def shorten_url(self, long_url):
        """Shorten a URL using hash."""
        if long_url in self.reverse_map:
            return self.reverse_map[long_url]

        # Create hash of the URL
        hash_object = hashlib.md5(long_url.encode())
        short_code = hash_object.hexdigest()[:6]  # Take first 6 characters

        # Ensure uniqueness
        while short_code in self.url_map:
            short_code = hash_object.hexdigest()[:8]  # Try longer if collision

        self.url_map[short_code] = long_url
        self.reverse_map[long_url] = short_code

        return short_code

    def expand_url(self, short_code):
        """Expand a short code to original URL."""
        return self.url_map.get(short_code, "URL not found")

    def save_to_file(self, filename="urls.txt"):
        """Save URL mappings to file."""
        try:
            with open(filename, 'w') as f:
                for code, url in self.url_map.items():
                    f.write(f"{code},{url}\n")
            print(f"URLs saved to {filename}")
        except Exception as e:
            print(f"Error saving URLs: {e}")

    def load_from_file(self, filename="urls.txt"):
        """Load URL mappings from file."""
        if not os.path.exists(filename):
            return

        try:
            with open(filename, 'r') as f:
                for line in f:
                    if ',' in line:
                        code, url = line.strip().split(',', 1)
                        self.url_map[code] = url
                        self.reverse_map[url] = code
            print(f"URLs loaded from {filename}")
        except Exception as e:
            print(f"Error loading URLs: {e}")

def main():
    shortener = URLShortener()
    shortener.load_from_file()

    print("URL Shortener")
    print("-" * 20)

    while True:
        print("\nOptions:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. List all URLs")
        print("4. Save and exit")

        choice = input("Choose option (1-4): ").strip()

        if choice == "1":
            long_url = input("Enter long URL: ").strip()
            if long_url:
                short_code = shortener.shorten_url(long_url)
                print(f"Short URL: {short_code}")
            else:
                print("URL cannot be empty")

        elif choice == "2":
            short_code = input("Enter short code: ").strip()
            if short_code:
                long_url = shortener.expand_url(short_code)
                print(f"Original URL: {long_url}")
            else:
                print("Code cannot be empty")

        elif choice == "3":
            if shortener.url_map:
                print("\nAll URLs:")
                for code, url in shortener.url_map.items():
                    print(f"{code} -> {url}")
            else:
                print("No URLs stored")

        elif choice == "4":
            shortener.save_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
