# Beginner Security Automation Script (Selenium + Python)

This project is a cybersecurity automation script built using Python and Selenium.

It demonstrates how browser automation can be used to test authentication mechanisms in web applications.

---

## Overview

This script:

- Opens a login page
- Attempts multiple passwords automatically
- Detects successful login attempts
- Counts total attempts
- Simulates basic brute force behaviour

Target used for testing:

https://quotes.toscrape.com/login

This website is intentionally insecure and meant for automation practice.

---

## Installation

### 1. Install Python (if not installed)

```
python --version
```

If needed:

```
brew install python
```

### 2. Install Selenium

```
pip3 install selenium
```

### 3. Install ChromeDriver (macOS)

```
brew install chromedriver
```

Verify installation:

```
chromedriver --version
```

---

## How To Run

### 1. Clone The Repository

```
git clone https://github.com/coder0name0dre/login_tester.git
cd login_tester
```

### 2. Run The Script

```
python3 login_tester.py
```

Chrome will open automatically and attempt login using multiple passwords.

---

## Expected Output

Example terminal output:

```
Attempt #1

Trying password: 123456

Login Successful!

Total attempts made: 1
```

Because the practice site has weak autentication, many passwords may successfully log in.

---

## What This Project Demonstrates

This project introduces:

- Browser automation
- Form interaction with Selenium
- Basic authentication testing logic
- Looping and control flow in Python
- Security thinking and response validation

---

## Cybersecurity Context

In real world penetration testing, scripts like this can help test:

- Weak password policies
- Missing rate limiting
- Authentication bypass vulnerabilities
- Improper session handling

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/login_tester/blob/main/LICENSE).