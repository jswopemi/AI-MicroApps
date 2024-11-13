APP_URL = "https://clinical-chatbot.streamlit.app"
APP_IMAGE = "clinical_chatbot.webp"
PUBLISHED = True

APP_TITLE = "Clinical Chatbot"
APP_INTRO = """
In this interactive exercise, you will interact with a clinical chatbot that will help you understand your patient's condition. You must determine their primary complaint and provide a differential diagnosis.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way to interact with an AI-powered clinical chatbot.

The chatbot has been provided with a patient history and a list of symptoms. Your job is to determine the primary complaint and provide a differential diagnosis.

The user will be able to have a free-form conversation with the chatbot to clarify their condition. Then they will input their primary complaint and a differential diagnosis.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistant for a clinical simulation exercise for a student user who is playing the role of a doctor. You will answer the user's questions and sometime assess their accuracy.
"""

PHASES = {
    "interview": {
        "name": "Patient Interview: Donna",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Donna is a new patient in your office. She is a 65-year old woman who has been experiencing shortness of breath for the past 2 weeks. She is a smoker and has a history of hypertension. You only have <strong>15 minutes</strong> to interview Donna and determine her primary complaint and differential diagnosis. For this simulation, that means you'll be able to ask her up to 10 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "patient_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/donna.webp",
                "caption": "Your new patient Donna is a 65-year old woman with a history of hypertension and currently experiencing shortness of breath.",
            },

        
        
        }
    }
}


PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Clinical Chatbot",
    "page_icon": "⚕️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
