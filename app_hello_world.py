PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
                "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "sport": {
            	"type": "text_input",
            	"label": "What is one of your favorite sport?"
            }
        },
        "user_prompt": "My name is {name} and I like this sport: {sport}. Write an epic paragraph about me playing that sport.",
    },
}

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
