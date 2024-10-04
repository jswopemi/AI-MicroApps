APP_TITLE = "Zodiac Symbol"
APP_INTRO = """This is a demonstration app that determines a users zodiac symbol based on their birth month and date. 
"""

APP_HOW_IT_WORKS = """
This app collects the name, birth Month, and birth date of the user, and provides them their Zodiac symbol. 
It utilizes the OpenAI and other AI APIs to send a custom prompt to AI with the user's inputs and returns the AI's response. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    
}

SYSTEM_PROMPT = """You are an expert in zodiac symbols. You know the accurate zodiac symbol based on a person's birth month and date, and you """

PHASES = {
    "name": {
        "name": "User Details",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "helper": "First name only, please",
                "value": "",
            },
            "month": {
                "type": "radio",
                "label": """What is your birth month?""",
                "options": ["January","February","March","April","May","June","July","August","September","October","November","December"],
            },
            "day": {
                "type": "number_input",
                "label": """What is your birth day?""",
                "min_value": 1,
                "max_value":31
            }


        },
        "phase_instructions": "",
        "user_prompt": "My name is {name}. I was born on {month} {day}. Please provide me my zodiac symbol, and give a short horoscope for the day.",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
        #"read_only_prompt": False
    }


}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Zodiac Predictor v1",
    "page_icon": "🌌",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())