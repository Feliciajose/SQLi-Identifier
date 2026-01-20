# ⚡ SQLi-Identifier

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Feliciajose/SQLi-Identifier?style=for-the-badge)](https://github.com/Feliciajose/SQLi-Identifier/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Feliciajose/SQLi-Identifier?style=for-the-badge)](https://github.com/Feliciajose/SQLi-Identifier/network)
[![GitHub issues](https://img.shields.io/github/issues/Feliciajose/SQLi-Identifier?style=for-the-badge)](https://github.com/Feliciajose/SQLi-Identifier/issues)
[![GitHub license](https://img.shields.io/github/license/Feliciajose/SQLi-Identifier?style=for-the-badge)](LICENSE) <!-- TODO: Add actual license file or specify license if known -->

**A powerful Python command-line tool for automated SQL injection vulnerability detection in web applications.**

</div>

## 📖 Overview

SQLi-Identifier is a specialized Python CLI tool designed to help security researchers and developers quickly identify potential SQL injection vulnerabilities. It automates the process of probing web applications with various SQLi payloads and analyzing responses for characteristic error messages or time-based delays, providing a robust first line of defense in web security assessments.

## ✨ Features

- **Error-Based SQLi Detection**: Automatically identifies common SQL error messages in HTTP responses.
- **Time-Based Blind SQLi**: Detects vulnerabilities by observing time delays in responses to specific payloads.
- **Batch Scanning**: Scan multiple URLs efficiently by providing a list from a file.
- **Customizable Requests**: Configure User-Agent strings and proxy settings for tailored scanning.
- **Rate Limiting**: Set delays between requests to avoid overwhelming target servers or triggering WAFs.
- **Interactive Progress Bar**: Visual feedback during batch scanning with `tqdm`.
- **Colored Terminal Output**: Enhanced readability of scan results and status updates.

## 🛠️ Tech Stack

- **Runtime**: Python 3.x
- **Package Management**: Pipenv
- **Core Libraries**:
    - ![Requests](https://img.shields.io/badge/requests-python-blue.svg?style=for-the-badge&logo=python) - HTTP library for making web requests.
    - ![BeautifulSoup4](https://img.shields.io/badge/beautifulsoup4-web_parsing-green.svg?style=for-the-badge&logo=python) - For parsing HTML and XML documents.
    - ![Colorama](https://img.shields.io/badge/colorama-terminal_colors-purple.svg?style=for-the-badge) - For cross-platform colored terminal output.
    - ![tqdm](https://img.shields.io/badge/tqdm-progress_bars-orange.svg?style=for-the-badge) - For fast, extensible progress bars.
    - ![urllib3](https://img.shields.io/badge/urllib3-http_client-lightgrey.svg?style=for-the-badge) - An HTTP client for Python, often a dependency for `requests`.
    - ![Certifi](https://img.shields.io/badge/certifi-ssl_certs-lightgreen.svg?style=for-the-badge) - SSL Certificates for Python.

## 🚀 Quick Start

### Prerequisites
- Python 3.x (3.6 or higher recommended)
- Pipenv (can be installed via `pip install pipenv`)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Feliciajose/SQLi-Identifier.git
    cd SQLi-Identifier
    ```

2.  **Install dependencies using Pipenv**
    ```bash
    pipenv install
    ```

3.  **Activate the project's virtual environment**
    ```bash
    pipenv shell
    ```

### Usage

The tool is executed directly using Python within the activated virtual environment.

### Basic Scan

Scan a single URL for SQL injection vulnerabilities:

```bash
python scan.py --url "http://example.com/vulnerable?id=1"
```

### Scan from a File

Provide a file containing a list of URLs (one URL per line) for batch scanning:

```bash
# Example urls.txt content:
# http://example.com/page1?param=1
# http://example.com/page2?id=2
# ...

python scan.py --file urls.txt
```

### Advanced Options

You can customize the scan with additional parameters:

-   **Set a delay between requests (in seconds):**
    ```bash
    python scan.py --url "http://example.com/test?item=5" --delay 2
    ```

-   **Specify a custom User-Agent string:**
    ```bash
    python scan.py --url "http://example.com/data?key=abc" --user-agent "Mozilla/5.0 (SQLi-Scanner)"
    ```

-   **Use an HTTP/S proxy:**
    ```bash
    python scan.py --url "http://example.com/query?val=xyz" --proxy "http://localhost:8080"
    ```

### Available Commands

| Option          | Description                                                               |
|-----------------|---------------------------------------------------------------------------|
| `--url <URL>`   | Target URL to scan for SQL injection vulnerabilities.                     |
| `--file <PATH>` | Path to a file containing a list of URLs to scan.                         |
| `--delay <SEC>` | Delay between requests in seconds (default: 0).                           |
| `--user-agent <UA>` | Custom User-Agent string for HTTP requests.                             |
| `--proxy <PROXY_URL>` | HTTP/S proxy to use (e.g., `http://localhost:8080`).                    |
| `--help`        | Show the help message and exit.                                           |

## 📁 Project Structure

```
SQLi-Identifier/
├── Pipfile         # Pipenv dependency management file
├── scan.py         # Main script for SQL injection detection
└── .gitignore      # Ignored files (e.g., __pycache__, .venv)
```

## ⚙️ Configuration

All configuration is handled via command-line arguments as detailed in the [Usage](#usage) section. There are no separate configuration files.

## 🤝 Contributing

We welcome contributions! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

### Development Setup for Contributors
1.  Fork the repository.
2.  Clone your forked repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/SQLi-Identifier.git
    cd SQLi-Identifier
    ```
3.  Install dependencies:
    ```bash
    pipenv install --dev # Use --dev if there were dev dependencies, otherwise just pipenv install
    ```
4.  Activate the virtual environment:
    ```bash
    pipenv shell
    ```
5.  Make your changes to `scan.py` or add new files.
6.  Test your changes thoroughly.
7.  Commit your changes and push to your fork.
8.  Open a pull request to the `main` branch of the original repository.

## 📄 License

This project is currently without an explicit license. Please contact the author for licensing information. <!-- TODO: Add actual license file or specify license if known -->

## 🙏 Acknowledgments

-   The `requests` library for simplifying HTTP requests.
-   `beautifulsoup4` for robust HTML parsing.
-   `colorama` for enhancing terminal output.
-   `tqdm` for providing elegant progress bars.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/Feliciajose/SQLi-Identifier/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Feliciajose

</div>
