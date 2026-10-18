# RoboAi — Voice-Powered AI Assistant

**Turning understanding into action, in your own language.**

RoboAi is a Python-based AI assistant designed to make AI more accessible through text responses, spoken answers, multilingual interaction, and browser-based task automation.

## ✨ Features

- **AI-powered answers:** Uses the Google Gemini API to answer user questions.
- **Voice output:** Speaks responses aloud using `spd-say` on supported Linux systems.
- **Multilingual interaction:** Includes language options such as English, Hindi, Hinglish, Bengali, Tamil, Telugu, Marathi, Gujarati, and Punjabi.
- **Guided assistance:** Aims to explain tasks step by step and help users troubleshoot problems.
- **Web task automation:** Integrates the TinyFish API to attempt browser-based tasks through the `/web` command.
- **Customizable Python code:** Developers can adapt the assistant to their own workflows.

## 🛠️ Tech Stack

- Python
- Google Gemini API (`google-genai`)
- TinyFish API
- `spd-say` for speech output
- Linux terminal

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sakshiitshivam17-gif/RoboAi.git
cd RoboAi
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install the packages used by the project:

```bash
pip install google-genai tinyfish requests
```

If the repository includes a `requirements.txt` file, use it instead:

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Set your Gemini API key in the terminal:

```bash
export GEMINI_API_KEY="your_gemini_api_key"
```

For web automation, set your TinyFish API key:

```bash
export TINYFISH_API_KEY="your_tinyfish_api_key"
```

Replace the example values with your own keys. **Never commit API keys or `.env` files to GitHub.**

### 5. Run RoboAi

If `main4.py` is the version you want to run:

```bash
python main4.py
```

## 🌐 Web Automation

RoboAi uses the `/web` command to request browser-based tasks through TinyFish.

Example commands inside the application:

```text
/web find the top 3 laptops under 60000 on amazon.in
/web https://news.ycombinator.com get the top 5 headlines
```

Website compatibility and results depend on the automation service, website access, and API configuration.

Always review browser actions. Use dummy information for testing forms, and do not submit forms or perform consequential actions without explicit confirmation.

## 🔐 Security

- Keep API keys private.
- Do not upload `.env` files or credentials.
- Review automation steps before allowing important actions.
- Use test data when experimenting with form automation.

## 🎯 Vision

RoboAi aims to bridge the gap between technical knowledge and practical action by helping users understand instructions and interact with digital tools in their preferred language.

The long-term goal is to make digital tasks easier for beginners through accessible explanations, voice output, and guided workflows.

## 👨‍💻 Author

**Sakshit Shivam**

GitHub: [@sakshiitshivam17-gif](https://github.com/sakshiitshivam17-gif)

---

*RoboAi — From understanding to action.*

