
APP_URL = "https://diataxis.streamlit.app"
Published=True

APP_TITLE = "Essay Critique"

APP_INTRO = """This DEMO tool helps developmental writing students improve their paragraph-level writing. Students select a prompt, submit a sample paragraph, and receive detailed, supportive feedback in three key areas.
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url": "https://sheap.bubbleapps.io/critiquecrowd",
    "button_text":"Source"
}

SYSTEM_PROMPT = """The user will write a paragraph of content according to a thematic prompt. You will act as a university writing coach and provide them feedback and a score on their writing. 
"""

PHASES = {
    "about": {
        "name": "Provide your document",
        "fields": {
            "prompt": {
                "type": "radio",
                "options": ["Narrative Event", "Expository Paragraph","Persuasive Paragraph", "Comparitive Paragraph"],
                "label": "What kind of paragraph do you choose?"
            },
            "document": {
                "type": "text_area",
                "height": 200,
                "label": """Please respond to the writing prompt in one full paragraph:""",
            }
        },
        "phase_instructions": """The user has been instructed to respond to this writing prompt: Write a persuasive paragraph about a change you believe should be made in your community, school, or another group you are part of. This could be anything from improving facilities, changing policies, or introducing new activities. Clearly state your position and provide reasons and evidence to support why this change is necessary and how it will benefit the group.

Please provide them feedback on how well they followed those intructions and provide tips for improvement. 

        """,
        "user_prompt": "Here is my writing: {document}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """            
        1. Completeness
                2 points - Paragraph is of adequate length with a beginning, middle, and conclusion.
                0 points - Paragraph is not of adequate length with a beginning, middle, and conclusion.
        2. Prompt
                2 points - The paragraph meets the requirements of the prompt
                0 points - The paragraph does not meet the requirements of the prompt. 
                """,
        "allow_revisions": True,
        "allow_skip": False,
    }
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thanks for using this tool!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Diataxis Categorizer",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
