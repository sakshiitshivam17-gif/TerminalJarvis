import os
import shutil
import subprocess

from google import genai
from google.genai import types


# ---------- CONFIGURATION ----------

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

SYSTEM_INSTRUCTION = """
You are Robo AI, a helpful multilingual assistant.

1. Answer the user's complete question directly.
2. Use the language the user prefers whenever possible.
3. Explain concepts clearly with examples when useful.
4. Do not start every answer with a greeting.
5. Give useful, complete answers rather than introductions only.
6. If you are unsure about something, say so honestly.
"""


# ---------- GEMINI CLIENT ----------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit(
        "ERROR: GEMINI_API_KEY is missing. Set it in your terminal first."
    )

client = genai.Client(api_key=api_key)


# ---------- TEXT TO SPEECH ----------

def speak(text):
    """Speak text aloud using spd-say on Linux."""
    if not text or not text.strip():
        return

    if shutil.which("spd-say") is None:
        print("[Voice unavailable: spd-say is not installed.]")
        return

    try:
        subprocess.run(
            ["spd-say", text],
            check=False,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"[Speech error: {error}]")


# ---------- AI RESPONSE ----------

def ask_ai(question):
    """Send a question to Gemini and return its answer."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                max_output_tokens=1000,
            ),
        )

        answer = response.text

        if answer and answer.strip():
            return answer.strip()

        return (
            "I couldn't generate a text answer. "
            "Please try asking in a different way."
        )

    except Exception as error:
        print(f"\n[Gemini API error: {error}]")
        return (
            "Sorry, I couldn't get an answer from Gemini. "
            "Please check your internet connection, API key, "
            "model availability, and API quota."
        )


# ---------- MAIN PROGRAM ----------

def main():
    print("=" * 40)
    print("       ROBO AI ASSISTANT")
    print("=" * 40)
    print("Ask me anything. Type 'exit' to quit.\n")

    speak("Hello! Robo AI is ready.")

    while True:
        try:
            question = input("You: ").strip()

            if question.lower() in ("exit", "quit", "bye"):
                print("Robo AI: Goodbye! Have a great day.")
                speak("Goodbye! Have a great day.")
                break

            if not question:
                continue

            print("\nRobo AI is thinking...")

            answer = ask_ai(question)

            print(f"\nRobo AI: {answer}\n")
            speak(answer)

        except KeyboardInterrupt:
            print("\nRobo AI: Goodbye!")
            break

        except EOFError:
            print("\nRobo AI: Input closed. Goodbye!")
            break


if __name__ == "__main__":
    main()
