# Clash Royale Deck Builder
#### Video Demo: [URL]
Coders:
- Alessandro Coen
- Kenneth Wiguna
---

## Overview

The Clash Royale Deck Builder is a Python-based application that helps players create Clash Royale decks. By allowing users to choose between one and three cards, the project uses a synergy map system to fill out the remainder of the 8-card deck. 
We defined a `main()` function within **project.py**, alongside custom functions that handle core tasks such as: 
`validate_cards`, 
`get_synergy_cards`,
`generate_deck.`
All of the functions are tested in **test_project.py** using pytest. Libraries beyond the Python standard library are listed in **requirements.txt**, enabling anyone to install and run the application.

---

## Files and Their Roles

- **project.py**  
Project.py contains the `main()` function. When you run `python project.py,` you are prompted to input 1–3 cards. Afterward, the script checks your card selection for validity (ensuring each card exists in our defined card pool), retrieves synergy cards based on that selection, and fills the deck to eight cards using a combination of synergy logic and random draws from the remaining pool. 
Three central functions: `validate_cards`, `get_synergy_cards`, and `generate_deck` helps the process flow.

**test_project.py**  
Each key function in **project.py** has a corresponding test method that checks for correct outcomes.
For example, `test_generate_deck` verifies that the final deck always has eight different cards, while `test_validate_cards` confirms that invalid user inputs (like misspelled or nonexistent cards) are denied. 

**requirements.txt**  
Flask is included here for the web interface, and pytest is required to run the test suite. These installments ensure that every aspect of the application—from card validation to synergy-driven deck assembly—functions consistently.

**app.py**  
Running `python app.py` will bring up a website where you can select your favorite cards in a form. The server then calls functions from **project.py** to generate a deck at the bottom of the page. This file allows our code to be visualized and presented with colors, bold texts, images, etc. 

**templates/index.html** and **static**   
The web interface’s visual components exist within **templates/index.html** (for structure and layout) and **static** (for images and optional CSS files). The card images must follow a strict naming convention such as how “Hog Rider” becomes “Hog_Rider.png.” This allows for a seamless interaction between the image and code function.

—--

## Core Logic and Design Choices

### Data Structures
For the application to quickly access the data it needs, we placed card attributes (elixir cost, rarity, and type) in a dictionary called CARDS_DATA.
Another dictionary called SYNERGY maps each card to a list of recommended cards. For example, if a user selects “Golem,” the program will automatically suggest related cards such as “Baby Dragon” or “Night Witch” to create effective deck combinations. 

### Functions and Testing
In **project.py**, three functions work together:
validate_cards(user_cards)
Validates the presence of each user-selected card in our dataset. The function returns False for unrecognized cards.
get_synergy_cards(card)
Gets synergy suggestions for a single card. Otherwise, we return an empty list to prevent unknowns from entering the data , as we do not have synergies with such cards.
generate_deck(user_cards)
First, it checks that the user has chosen between 1 and 3 valid cards. It then adds any relevant synergy cards to the deck and fills the remainder of the slots with random cards until the deck size is eight. 
Test_project is where all these functions are tested. All test functions verify typical usage along with edge cases like user-defined, invalid card names, or excess user-defined cards (cards selected) to ensure that the deck builder continues to work normally.

---

## Challenges and Future Improvements
Card picture naming proved surprisingly challenging. Forgetting to rename files like “Hog Rider. png” to “Hog_Rider. png” broken web interface images because, in our code, spaces are automatically replaced with underscores. It is quite difficult to balance how many synergy cards to add before just throwing in the random cards. An excess of them can yield repetitive, predictable decks; too few, and the strategic matches can be overlooked.

—--

## Conclusion
In summary, the **Clash Royale Deck Builder** uses data structures, synergy-based logic, and testing to create randomized decks for Clash Royale players. **project.py**allows users to generate decks directly in the console, while **app.py** presents an interface for a more image-rich experience. Design choices such as a synergy dictionary, random card filling, and naming conventions ensure that every deck generated is unique and effective in-game.  
The`main()` function contained custom functions, and a **requirements.txt** that captures all dependencies. Thank you for reading, and happy deck building!


