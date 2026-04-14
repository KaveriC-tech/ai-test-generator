import sys
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_selenium_test(feature_description):
    prompt = f"""
You are a QA automation engineer. Generate a Python Selenium test case for the following feature:

Feature: {feature_description}

Requirements:
- Use pytest as the test framework
- Use Selenium WebDriver with Chrome
- Use webdriver-manager to manage ChromeDriver
- Use Page Object Model pattern
- Include proper assertions
- Add clear comments
- Use explicit waits instead of time.sleep()
- Return only the Python code, no explanations

Generate the test code now:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert QA automation engineer who writes clean, professional Selenium Python test code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.3
    )

    return response.choices[0].message.content

def save_test_to_file(test_code, feature_description):
    filename = feature_description[:30].strip().lower()
    filename = filename.replace(" ", "_").replace("/", "_") + "_test.py"
    output_dir = "generated_tests"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(test_code)
    return filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_tests.py \"your feature description here\"")
        print("Example: python generate_tests.py \"User should be able to log in with valid credentials\"")
        sys.exit(1)

    feature_description = " ".join(sys.argv[1:])
    print(f"\nGenerating Selenium test for: {feature_description}")
    print("Please wait...\n")

    test_code = generate_selenium_test(feature_description)

    print("Generated Test Code:")
    print("=" * 60)
    print(test_code)
    print("=" * 60)

    filepath = save_test_to_file(test_code, feature_description)
    print(f"\nTest saved to: {filepath}")
    print("Done!")

if __name__ == "__main__":
    main()
