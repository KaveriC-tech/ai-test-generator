# AI Test Generator

A Python CLI tool that uses the **OpenAI API** to automatically generate **Selenium WebDriver** test cases from plain-English feature descriptions.

---

## What It Does

Instead of manually writing test cases, you describe a feature in plain English and the tool generates a complete, ready-to-run Selenium Python test for you.

**Example:**
```bash
python generate_tests.py "User should be able to log in with valid credentials"
```

**Output:**
A fully structured Selenium test with Page Object Model, explicit waits, and assertions — saved automatically to the `generated_tests/` folder.

---

## Tech Stack

- **Language:** Python
- **AI:** OpenAI API (GPT-3.5-turbo)
- **Testing:** Selenium WebDriver
- **Driver Management:** webdriver-manager
- **Pattern:** Page Object Model (POM)

---

## Project Structure
ai-test-generator/
├── generate_tests.py        # Main CLI script
├── requirements.txt         # Python dependencies
├── sample_output/
│   └── login_test_sample.py # Example of generated test output
└── README.md
---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/KaveriC-tech/ai-test-generator.git
cd ai-test-generator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your OpenAI API key**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**4. Run the generator**
```bash
python generate_tests.py "User should be able to log in with valid credentials"
```

**5. Find your generated test**
```bash
cd generated_tests/
```

---

## Sample Output

See [`sample_output/login_test_sample.py`](sample_output/login_test_sample.py) for an example of what the generator produces — including Page Object Model structure, explicit waits, and multiple test cases.

---

## Why This Project

AI-assisted test generation is an emerging skill in QA engineering in 2026. This tool demonstrates:
- Practical use of OpenAI API in a QA context
- Python scripting and CLI tool development
- Selenium WebDriver and Page Object Model
- Prompt engineering for consistent, structured output

---

## Author

**Kaveri C** — QA Automation Engineer
[LinkedIn](https://www.linkedin.com/in/c-kaveri789/) • [GitHub](https://github.com/KaveriC-tech)
