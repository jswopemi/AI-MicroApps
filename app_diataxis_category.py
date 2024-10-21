APP_URL = "https://diataxis.streamlit.app"
Published=True

APP_TITLE = "Diataxis Categorizer"

APP_INTRO = """This app takes documentation content and categorizes it according to the Diataxis Framework (How-To, Concept, Reference, Quickstart)
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url": "https://docs.openedx.org/en/latest/documentors/concepts/content_types.html",
    "button_text":"Diataxis Types"
}

SYSTEM_PROMPT = """The user provides you instructional content and you return the diataxis type(s) for that content, along with percent probability of your certainty of your categorization. Your certainty always adds up to 100%. 

As a reminder, here are the diataxis types and how we categorize them: 

**How-to**
How-to topics provide direct and easy-to-follow instructions to accomplish specific goals. For example, topics provide the steps to create a new course subsection and to schedule a course.

**Quickstart**
Quickstart topics may seem similar to How-Tos but have a different focus. Quickstarts are specifically built for beginners and are meant to help them gain experience with the product. For example taking a course through the entire course lifecycle, even if there is no content, and it’s not exactly how you would do it with a real course, gives a beginner a meaningful experience that helps them better navigate the product.

**Reference**
Reference topics provide details about a function or feature of the Open edX platform. For example there are many details about course subsections such as the different publication states, grading configuration, and visibility that are not included in the how-to topic Create a Subsection but are fully described in the reference topic Course Subsections. These two topics are linked in See Also sections.

**Concept**
Concept topics provide best practices or other guidelines for using the Open edX platform. For example, the topics Crafting Effective Learning Objectives and Aligning End-of-Module Assessments to Learning Objectives are meant to provide guidelines for educators.
"""

PHASES = {
    "about": {
        "name": "Provide your document",
        "fields": {
            "document": {
                "type": "text_area",
                "height": 200,
                "label": """Please paste your full document below:""",
            }
        },
        "phase_instructions": """I will provide a document. Please return your diataxis categorization as taxonomy and certainy. Like this:
How-To (100%)

or this:

Reference (90%)
How-To (10%)
        """,
        "user_prompt": "Here is my document for categorization: {document}",
        "ai_response": True,
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

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
