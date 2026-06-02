# LinkedIn AI Auto Job Applier 🤖

This is a web scraping bot that automates the process of job applications on LinkedIn. It searches for jobs relevant to you, answers questions in the application form, customizes your resume based on collected job information (skills required, description, company info, etc.), and applies to the job. **It can apply to 100+ jobs in less than 1 hour.**

## 📽️ See it in Action
[![Auto Job Applier demo video](https://github.com/GodsScion/Auto_job_applier_linkedIn/assets/100998531/429f7753-ebb0-499b-bc5e-5b4ee28c4f69)](https://youtu.be/gMbB1fWZDHw)

---

## 🚀 Installation (From Scratch)

[![Auto Job Applier setup tutorial video](https://github.com/user-attachments/assets/9e876187-ed3e-4fbf-bd87-4acc145880a2)](https://youtu.be/f9rdz74e1lM?si=4fRBcte0nuvr6tEH)
*(Recommended to watch the [tutorial video](https://youtu.be/f9rdz74e1lM) for setup guidance)*

### Prerequisites
- [Python 3.10+](https://www.python.org/downloads/) (Ensure Python is added to your system PATH).
- [Google Chrome](https://www.google.com/chrome) installed in its default location.

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/GodsScion/Auto_job_applier_linkedIn.git
   cd Auto_job_applier_linkedIn
   ```

2. **Set Up a Virtual Environment**
   Creating a virtual environment ensures dependencies don't conflict with your system Python packages.
   ```bash
   python3 -m venv venv
   ```
   **Activate the environment:**
   - **On macOS/Linux:** `source venv/bin/activate`
   - **On Windows:** `venv\Scripts\activate`

3. **Install Dependencies**
   While your virtual environment is active, run:
   ```bash
   pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
   ```

4. **Install ChromeDriver (Optional)**
   - **Note:** If you set `stealth_mode = True` in `config/settings.py` later on, you can skip this step entirely.
   - **On Windows:** Double-click `setup/windows-setup.bat` to automatically install the correct driver.
   - **On macOS/Linux:** Download the [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) matching your Chrome version and place it where Chrome is installed.

---

## 🔧 Configuration

Before starting the bot, you **must** configure your settings in the `/config` folder:

1. **`personals.py`**: Enter your details (name, phone number, address, etc.).
2. **`questions.py`**: Provide default answers for application questions. Also, specify your default resume path (e.g., `default_resume_path = "all resumes/default/resume.pdf"`).
3. **`search.py`**: Define your job search preferences, filters, and keywords.
4. **`secrets.py` (Optional)**: Provide your LinkedIn username, password, and OpenAI API Key (for tailored resumes/cover letters). If left default, the bot will use your saved browser profile or ask you to log in manually.
5. **`settings.py`**: Adjust bot settings like stealth mode, click intervals, keep screen awake, etc.

---

## 💻 Running the Application

Ensure your virtual environment is activated (`source venv/bin/activate` or `venv\Scripts\activate`), then run the following from the project root:

- **Start the Job Applier Bot:**
  ```bash
  python runAiBot.py
  ```

- **View Applied Jobs History Dashboard:**
  ```bash
  python app.py
  ```
  Open your web browser and go to `http://localhost:5000`.

---

## 🤝 Contributing

Contributions are heavily appreciated! Please see our [**Contributor Guidelines**](CONTRIBUTING.md) to get started.

## 🗓️ Changelog

To see what's new and read about past updates, check out our [**Major Updates History**](CHANGELOG.md).

---

## 📜 Disclaimer

**This program is for educational purposes only. Usage is at your own risk.** By downloading, using, or interacting with this program, you agree to abide by all the Terms, Conditions, Policies, and Licenses mentioned. Please adhere to LinkedIn's terms of service pertaining to web scraping. The creators bear no responsibility for any misuse, damages, or legal consequences resulting from its usage.

See [AGPLv3 LICENSE](LICENSE) for more info.

## 💬 Community & Support
- **Discord Server:** [Join here](https://discord.gg/fFp7uUzWCY)
- **GitHub Discussions:** [Join the conversation](https://github.com/GodsScion/Auto_job_applier_linkedIn/discussions)

**Author:** Sai Vignesh Golla ([LinkedIn](https://www.linkedin.com/in/saivigneshgolla/), [Twitter/X](https://x.com/saivigneshgolla))
