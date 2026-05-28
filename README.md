# AI-Assisted Test Case Generator

A Python-based AI-assisted testing utility that converts plain-English functional requirements into structured Selenium WebDriver automation scripts using OpenAI models. The tool helps reduce manual test design effort while promoting scalable automation practices such as Page Object Model (POM) and reusable test architecture.

---

## Overview

Traditional test case creation can be repetitive and time-consuming. This project leverages the OpenAI API to automatically generate Selenium WebDriver test scripts from natural-language requirements, enabling QA engineers to accelerate test design and improve productivity.

The generated output follows automation best practices, including Page Object Model (POM), explicit waits, reusable methods, and structured assertions.

---

## Tech Stack

* **Language:** Python
* **AI Integration:** OpenAI API (GPT-3.5-turbo)
* **Automation Framework:** Selenium WebDriver
* **Driver Management:** webdriver-manager
* **Design Pattern:** Page Object Model (POM)
* **Execution:** Command Line Interface (CLI)

---

## Features

* Converts plain-English requirements into Selenium automation scripts
* Generates structured Page Object Model (POM) code
* Includes explicit waits and validation assertions
* Reduces manual test case creation effort
* Produces reusable automation templates
* Command-line based workflow for rapid test generation
* Demonstrates practical AI integration for QA engineering

---

## Project Structure

```text
ai-test-generator/
├── generate_tests.py
├── requirements.txt
├── sample_output/
│   └── login_test_sample.py
└── README.md
```

### Folder Description

* **generate_tests.py** – Main CLI application that interacts with the OpenAI API
* **requirements.txt** – Project dependencies
* **sample_output/** – Example generated Selenium test scripts
* **README.md** – Project documentation

---

## How It Works

### Step 1: Provide a Requirement

```bash
python generate_tests.py "User should be able to log in with valid credentials"
```

### Step 2: AI Processes the Requirement

The application sends the requirement to the OpenAI API with a structured prompt designed to generate high-quality Selenium automation code.

### Step 3: Test Script Generation

The tool automatically generates:

* Page Object Model structure
* Selenium test script
* Explicit waits
* Validation assertions
* Reusable automation components

### Step 4: Save Output

Generated scripts are automatically saved for further execution and customization.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KaveriC-tech/ai-test-generator.git
cd ai-test-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure OpenAI API Key

Linux/macOS:

```bash
export OPENAI_API_KEY="your-api-key"
```

Windows:

```cmd
set OPENAI_API_KEY=your-api-key
```

---

## Running the Application

Execute the generator with a requirement:

```bash
python generate_tests.py "User should be able to log in with valid credentials"
```

---

## Execution Example

### Input

```bash
python generate_tests.py "User should be able to log in with valid credentials"
```

### Generated Output

The tool generates:

* Login Page Object
* Selenium automation script
* Explicit waits for elements
* Assertions for successful login
* Reusable test structure following POM principles

Example output file:

```text
generated_tests/login_test.py
```

---

## Sample Output

A sample generated automation script can be found here:

```text
sample_output/login_test_sample.py
```

The generated script demonstrates:

* Page Object Model implementation
* Selenium WebDriver automation
* Explicit waits
* Assertion handling
* Reusable automation patterns

---

## Why This Project

This project was built to explore how AI can improve software quality engineering workflows by automating repetitive test design activities.

It demonstrates:

* Practical use of OpenAI API in QA automation
* Python scripting and CLI development
* Selenium WebDriver automation
* Prompt engineering techniques
* Automated test generation workflows
* Scalable test architecture practices

---

## Key Learning Outcomes

* Building AI-assisted developer tools
* Integrating external APIs into automation workflows
* Generating structured automation code from natural-language inputs
* Applying Page Object Model principles
* Creating reusable QA productivity solutions

---

## Future Enhancements

* Playwright test generation support
* API test case generation using Postman collections
* CI/CD pipeline integration
* Support for multiple automation frameworks
* Web-based user interface
* Enhanced prompt optimization for improved output accuracy
* Support for BDD-style test generation
* Automatic test data generation

---

## Execution Preview

Add screenshots of:

* CLI execution
* Generated Selenium output
* Project workflow

Example:

```markdown
![Execution Preview](./screenshots/execution-preview.png)
```

---

## Author

**Kaveri C**
QA Automation Engineer

LinkedIn: https://www.linkedin.com/in/c-kaveri789/

GitHub: https://github.com/KaveriC-tech

---

Built to demonstrate AI-assisted QA workflows, automation engineering practices, and practical applications of generative AI in software testing.
