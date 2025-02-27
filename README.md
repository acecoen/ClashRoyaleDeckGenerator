**Project**: Clash Royale Deck-Builder Project

**VIDEO DEMONSTRATION:**

**Description**

This is the Clash Royale Deck-Builder Project, where the aim of the project is to create a Python-based code that will create custom decks based on 1-3 user-chosen cards for the game Clash Royale. Using a synergy system, this project lets users build their decks by allowing them to add cards they want to use while making sure their individual synergies work together. The generated deck includes eight cards, with the user-specified cards at its center. 

**Structure & Functions**

project.mainloop() contains the main logic.py, which has a main()` function driving the user interface and program flow.

-- There are three other top-level (i.e., not nested) functions in project.py that deal with all main functionalities:`

`Hashes are as mentioned above: validate_cards(preferred_cards):

get_synergy_cards(card)

build_deck(preferred_cards)

**Testing with pytest**

project: We have at least three custom functions in here. py that are extensively tested in test_project. py using pytest.

To test each function, name the test function according to test_.

**Packaging & Requirements**
The requirements.txt file in the project's root folder contains all the external or pip-installable libraries we depend on. For instance, in this file we have included pytest because we use that to run our test suite.

**Project Description**
The Clash Royale Deck-Builder Project is a deck generator that put cards together based on a synergy dictionary. Clash Royale is a Supercell mobile game where players fight opponents using decks of eight cards. Deck-building is involved combining of tanks, support units, spells, and defensive buildings. We automated part of the synergy logic, providing users a straightforward way to find new (or less obvious) card pairings.

**Concept explained:**

The user specifies the cards they want to include (from one to three).

The program verifies that those selected cards are valid by comparing them against an internal pool of cards.

For each valid preferred card, the program looks in a synergy dictionary to find companion cards that are known to work well with that card.

After synergy cards have been added, the system completely fills the remaining deck slots (with a limit of eight total) with random selections from the remaining pool, thus ensuring a full deck.

This STR(x) application implements a simple synergy dictionary in its first version. Another way to advance the system is to assign each Clash Royale card a specific role such as the bomb tower as a building or the giant as tank. This would in theory create better decks, however this did not align with our goal of generating purely random decks. Nonetheless, it is something to consider if we were to improve the code and deck generator to produce more effective decks. 

**Projec files and functions:**

- project.py: This file holds the primary logic of that program. It holds:

- The main() function asks the user for their favorite cards, calls our helper functions, and outputs the resulting deck.

- validate_cards(preferred_cards): verifies if all user-typed card numbers exist in the list of known cards. It returns a list of invalid entries if there are any invalid cards.

- get_synergy_cards(card): searches for synergy relationships in our dictionary for a card. When the card is identified, it returns a generated list of partner cards.

- Build_deck(preferred_cards): This function combines user-selected cards, synergy suggestions, and random selections (if necessary) to create a full deck of eight cards.

- test_project.py: The code contains a set of pytest-based unit tests that verify the correct functioning of each of our three bespoke functions. Not only does this confirm that the program works as it should, but it also showcases the best practice of test-driven or test-influenced development.

Test_validate_cards() ensures that valid card names pass and flags invalid ones.

- test_get_synergy_cards(): returns previously stored synergy cards for known cards, while non-displayed cards have empty results and unknown cards return only an empty card.

- Test_build_deck(): confirms the creation of an 8-card deck with user-selected cards, synergy suggestions, and random fillers.

- requirements.txt: This is a plain text file that contains any libraries or frameworks that this project needs to run. On the other hand, here, the only external dependency is PyTest for testing. But as you grow the project—say, by adding a web framework like Flask—you’d attach that to this file so that others can install all dependencies easily.

**Synergy Dictionary**

One of the design elements we have is our synergy dictionary, SYNERGY_DICT. We’ve defined a few similar cards like “Hog Rider” and “Giant” to complement the cards. This is an oversimplification of the actual synergy map of Clash Royale, but it shows how the logic could scale.

**Randomness**

After adding synergy cards to the deck, randomly select up to eight cards from the available card pool. Particularly, this means that although these types of cards provide a degree of variety, players may see certain archetypes repeating if a small dictionary is used or if synergy cards are not strong enough. One future improvement might be to track roles (e.g., building-targeting, anti-air, splash-damage) to keep the decks balanced.

**Testing**

We chose PyTest, as it is a a lightweight and powerful testing framework that integrates with Python pretty well. Our tests are quite simple, but they provide a solid baseline to check that the basic functionality still works as expected when the code changes.

**How to Install and Run**

Clone or download the repository from GitHub, making sure to include project.py, test_project.py, requirements.txt, and README. All of these (e.g., apples and oranges as well as md` itself) are located in the root directory.

**Install Dependencies: Run**

pip install -r requirements.txt

