Iris - Your AI-Powered Personal Assistant
Iris is an innovative AI-powered personal assistant designed to enhance your daily interactions with technology. By leveraging advanced natural language processing and speech synthesis technologies, Iris offers a seamless and engaging user experience. This project showcases the integration of multiple AI models and APIs to automate tasks, provide real-time information, and interact with users in a natural, conversational manner.

Features
Conversational AI: Powered by Google’s Gemini 1.5 model, Iris can engage in meaningful conversations, providing informative and contextually relevant responses.
Voice Interaction: Utilizes Microsoft's Edge TTS and Pygame for converting text into realistic speech, offering a dynamic and accessible way to interact.
Intent Recognition: Accurately understands and processes user commands to automate tasks, fetch information, and provide updates.
Task Automation: Capable of automating various activities, such as playing music on Spotify, getting weather reports, browsing YouTube, and delivering news updates.
Real-Time Interaction: Always ready to assist with a continuous loop awaiting user input, ensuring timely responses and prompt task execution.
Getting Started
Prerequisites
Python 3.x
Required libraries: google.generativeai, pygame, edge_tts, asyncio
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/iris-ai-assistant.git
cd iris-ai-assistant
Install the required packages:

bash
Copy code
pip install google-generativeai pygame edge-tts asyncio
Configure the Google Generative AI API:

Obtain an API key from Google and set it in your environment or directly in the code:
python
Copy code
genai.configure(api_key="YOUR_API_KEY")
Add your prompt in prompt.txt file located in the project directory.

Running Iris
Run the main script to start interacting with Iris:

bash
Copy code
python main.py
Usage
Demo Questions
General Conversation:

"Hi Iris, how are you today?"
"Tell me a joke."
Music Automation:

"Play some relaxing music."
"Can you play my favorite playlist on Spotify?"
Weather Reports:

"What's the weather like today in New York?"
"Is it going to rain tomorrow in London?"
YouTube Automation:

"Play the latest video from TED Talks on YouTube."
"Show me some workout videos on YouTube."
News Updates:

"What's the latest news?"
"Give me an update on today's top headlines."
Using Google Gemini AI:

"What's the capital of France?"
"Can you explain the theory of relativity?"
Contributing
We welcome contributions to enhance Iris. Feel free to fork the repository and create a pull request with your improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
