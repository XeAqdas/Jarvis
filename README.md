# 🎤 Jarvis - An AI Python Voice Assistant

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet powerful voice-activated personal assistant built in Python. "Jarvis" listens for a wake word, processes your spoken commands, and responds with voice feedback, performing tasks like opening websites, playing music, fetching news, and answering questions.

***

## ✨ Features

* **Wake Word Activation:** Jarvis stays dormant until you say "Jarvis" to activate it.
* **Voice Commands:** Control a variety of tasks using natural language.
* **Web Browsing:** Open popular websites like Google, YouTube, Facebook, and LinkedIn.
* **Music on Demand:** Instantly play any song on YouTube.
* **News Headlines:** Get the latest top news headlines from around the world.
* **Real-time Weather:** Ask for the current weather in any city.
* **AI-Powered Q&A:** Ask any question and get an intelligent response from a powerful language model (GPT-3.5 Turbo via OpenRouter).
* **Voice Feedback:** All responses and actions are confirmed with audible speech (but subjected to the working of pyttsx3 module in your system).

***

## ⚙️ Technology Stack

* **Core Language:** Python 3.10
* **Speech Recognition:** `speech_recognition` (using Google's Speech Recognition API)
* **Audio Input:** `sounddevice` & `numpy`
* **Text-to-Speech:** `pyttsx3`
* **Web Automation:** `webbrowser` & `pywhatkit`
* **API Communication:** `requests`

***

## 🔧 Setup and Installation

Follow these steps to get Jarvis running on your local machine.

### **Prerequisites**

* **Python 3.10:** This project has been tested and is stable on Python 3.10. Newer versions may cause dependency issues.
* A working **microphone**.
* An active **internet connection**.

### **Installation Steps**

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/xeaqdas/jarvis.git](https://github.com/xeaqdas/jarvis.git)
    cd jarvis
    ```

2.  **Create and Activate a Virtual Environment**
    It's highly recommended to use a virtual environment to keep dependencies isolated.

    * **Windows (PowerShell):**
        ```powershell
        # Create the environment using Python 3.10
        py -3.10 -m venv .venv
        # Activate it
        .\.venv\Scripts\Activate.ps1
        ```

    * **macOS / Linux:**
        ```bash
        # Create the environment using Python 3.10
        python3.10 -m venv .venv
        # Activate it
        source .venv/bin/activate
        ```

3.  **Install Required Packages**
    Due to potential network issues with the `speech_recognition` package, we will install it in two steps for reliability.

    * **Step A: Install the main packages**
        ```bash
        pip install pyttsx3 sounddevice numpy requests pywhatkit
        ```

    * **Step B: Manually install `speech_recognition`**
        1.  Download the package "wheel" file from this official link: [SpeechRecognition-3.10.1-py3-none-any.whl](https://files.pythonhosted.org/packages/b3/74/471a2911b3b804533b6528f0e93a6c5f7e7c9561055a47141505586b586e/SpeechRecognition-3.10.1-py3-none-any.whl)
        2.  Save this `.whl` file directly into your project folder (`jarvis-voice-assistant`).
        3.  Install it from the local file:
            ```bash
            pip install SpeechRecognition-3.10.1-py3-none-any.whl
            ```

***

## 🔑 Configuration: API Keys

This assistant requires three API keys to function fully. These must be set as **environment variables**.

1.  **NewsAPI:** For news headlines.
    * Get your free key from [newsapi.org](https://newsapi.org).
    * Set the environment variable: `NEWS_API_KEY`

2.  **OpenWeatherMap:** For weather information.
    * Create a free account and get your key from [home.openweathermap.org/api\_keys](https://home.openweathermap.org/api_keys).
    * **Note:** New keys can take up to 2 hours to activate.
    * Set the environment variable: `OPENWEATHERMAP_API_KEY`

3.  **OpenRouter:** For the general Q&A feature.
    * Get your free key from [openrouter.ai](https://openrouter.ai).
    * Set the environment variable: `OPENROUTER_API_KEY`

#### **How to Set Environment Variables**

* **Windows (PowerShell - for the current session):**
    ```powershell
    $env:NEWS_API_KEY="your_key_here"
    $env:OPENWEATHERMAP_API_KEY="your_key_here"
    $env:OPENROUTER_API_KEY="your_key_here"
    ```
    *(For a permanent solution, search for "Edit the system environment variables" in the Start Menu.)*

* **macOS / Linux (for the current session):**
    ```bash
    export NEWS_API_KEY="your_key_here"
    export OPENWEATHERMAP_API_KEY="your_key_here"
    export OPENROUTER_API_KEY="your_key_here"
    ```
    *(For a permanent solution, add these lines to your `~/.bashrc` or `~/.zshrc` file.)*

***

## 🚀 Usage

Once the setup and configuration are complete, running the assistant is simple.

1.  Make sure your virtual environment is active.
2.  Run the main script from your terminal:
    ```bash
    python main.py
    ```
3.  Wait for the greeting. You will see "Say 'Jarvis' to activate..." in the terminal.
4.  Say the wake word "Jarvis".

#### **Example Commands:**
* "Jarvis... open Google."
* "Jarvis... play Believer by Imagine Dragons."
* "Jarvis... what's the latest news?"
* "Jarvis... what's the weather in Mumbai?"
* "Jarvis... what is the theory of relativity?"

***

## 🖼️ Screenshots

<img width="1920" height="1080" alt="Screenshot (148)" src="https://github.com/user-attachments/assets/fe99e993-640e-4b87-b1ca-9f5dd792d582" />
<img width="1920" height="1080" alt="Screenshot (149)" src="https://github.com/user-attachments/assets/6e28d7fb-74c9-4895-b27e-505c819bdcf0" />
<img width="1920" height="1080" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/2e0d6ecf-d9d6-45cf-8d66-ad9e335b2907" />
<img width="1920" height="1080" alt="Screenshot (151)" src="https://github.com/user-attachments/assets/db1aa60a-a2be-4802-b4a4-cf1a291765dc" />

***

## 💡 Future Improvements

* [ ] Implement a graphical user interface (GUI).
* [ ] Add more integrations (e.g., Spotify, calendar).
* [ ] Implement custom wake word detection.
* [ ] Store conversation history.

***

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
