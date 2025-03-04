import random

# Comprehensive card data dictionary including Mega Knight and Archer Queen
CARDS_DATA = {
    "Hog Rider": {"elixir": 4, "rarity": "Epic", "type": "Troop"},
    "Musketeer": {"elixir": 4, "rarity": "Rare", "type": "Troop"},
    "Fireball": {"elixir": 4, "rarity": "Rare", "type": "Spell"},
    "Skeletons": {"elixir": 1, "rarity": "Common", "type": "Troop"},
    "Ice Spirit": {"elixir": 1, "rarity": "Common", "type": "Troop"},
    "Golem": {"elixir": 8, "rarity": "Epic", "type": "Troop"},
    "Baby Dragon": {"elixir": 4, "rarity": "Rare", "type": "Troop"},
    "Mega Minion": {"elixir": 3, "rarity": "Rare", "type": "Troop"},
    "Lightning": {"elixir": 6, "rarity": "Epic", "type": "Spell"},
    "Night Witch": {"elixir": 4, "rarity": "Legendary", "type": "Troop"},
    "Miner": {"elixir": 3, "rarity": "Epic", "type": "Troop"},
    "Poison": {"elixir": 4, "rarity": "Epic", "type": "Spell"},
    "Bats": {"elixir": 2, "rarity": "Common", "type": "Troop"},
    "Goblin Gang": {"elixir": 3, "rarity": "Common", "type": "Troop"},
    "Barbarian Barrel": {"elixir": 4, "rarity": "Rare", "type": "Spell"},
    "Elixir Collector": {"elixir": 6, "rarity": "Rare", "type": "Building"},
    "Cannon": {"elixir": 3, "rarity": "Common", "type": "Building"},
    "Wizard": {"elixir": 5, "rarity": "Rare", "type": "Troop"},
    "Valkyrie": {"elixir": 4, "rarity": "Rare", "type": "Troop"},
    "Spear Goblins": {"elixir": 2, "rarity": "Common", "type": "Troop"},
    "Minion Horde": {"elixir": 5, "rarity": "Rare", "type": "Troop"},
    "Inferno Tower": {"elixir": 5, "rarity": "Rare", "type": "Building"},
    "Electro Wizard": {"elixir": 4, "rarity": "Legendary", "type": "Troop"},
    "Royal Giant": {"elixir": 6, "rarity": "Rare", "type": "Troop"},
    "Mini P.E.K.K.A": {"elixir": 4, "rarity": "Rare", "type": "Troop"},
    "Three Musketeers": {"elixir": 9, "rarity": "Epic", "type": "Troop"},
    "Executioner": {"elixir": 5, "rarity": "Epic", "type": "Troop"},
    "Bowler": {"elixir": 5, "rarity": "Rare", "type": "Troop"},
    "Rocket": {"elixir": 6, "rarity": "Epic", "type": "Spell"},
    "Tornado": {"elixir": 3, "rarity": "Epic", "type": "Spell"},
    "Battle Ram": {"elixir": 5, "rarity": "Rare", "type": "Troop"},
    "Cannon Cart": {"elixir": 5, "rarity": "Rare", "type": "Troop"},
    "Flying Machine": {"elixir": 4, "rarity": "Rare", "type": "Troop"},
    "Dark Prince": {"elixir": 4, "rarity": "Legendary", "type": "Troop"},
    # New cards added:
    "Mega Knight": {"elixir": 7, "rarity": "Legendary", "type": "Troop"},
    "Archer Queen": {"elixir": 6, "rarity": "Legendary", "type": "Troop"}
}

# The card pool is the list of all card names
CARD_POOL = list(CARDS_DATA.keys())

# Comprehensive synergy mapping including new cards
SYNERGY = {
    "Hog Rider": ["Musketeer", "Fireball", "Skeletons", "Ice Spirit"],
    "Musketeer": ["Hog Rider", "Skeletons"],
    "Fireball": ["Hog Rider", "Musketeer"],
    "Skeletons": ["Hog Rider", "Musketeer"],
    "Ice Spirit": ["Hog Rider", "Musketeer"],
    "Golem": ["Baby Dragon", "Mega Minion", "Lightning", "Night Witch"],
    "Baby Dragon": ["Golem", "Mega Minion", "Lightning"],
    "Mega Minion": ["Golem", "Baby Dragon"],
    "Lightning": ["Golem", "Night Witch"],
    "Night Witch": ["Golem", "Lightning"],
    "Miner": ["Poison", "Bats", "Goblin Gang", "Barbarian Barrel"],
    "Poison": ["Miner", "Bats"],
    "Bats": ["Miner", "Goblin Gang"],
    "Goblin Gang": ["Miner", "Bats"],
    "Barbarian Barrel": ["Miner", "Goblin Gang"],
    "Elixir Collector": ["Wizard", "Valkyrie"],
    "Cannon": ["Wizard", "Valkyrie"],
    "Wizard": ["Elixir Collector", "Cannon", "Valkyrie"],
    "Valkyrie": ["Wizard", "Cannon"],
    "Spear Goblins": ["Hog Rider", "Musketeer"],
    "Minion Horde": ["Three Musketeers", "Baby Dragon", "Mega Minion"],
    "Inferno Tower": ["Electro Wizard", "Mini P.E.K.K.A", "Executioner"],
    "Electro Wizard": ["Inferno Tower", "Royal Giant", "Battle Ram", "Mini P.E.K.K.A"],
    "Royal Giant": ["Electro Wizard", "Mini P.E.K.K.A", "Bowler", "Tornado"],
    "Mini P.E.K.K.A": ["Electro Wizard", "Royal Giant"],
    "Three Musketeers": ["Minion Horde", "Hog Rider", "Skeletons"],
    "Executioner": ["Goblin Gang", "Bats", "Bowler"],
    "Bowler": ["Executioner", "Rocket"],
    "Rocket": ["Tornado", "Electro Wizard", "Fireball"],
    "Tornado": ["Rocket", "Wizard"],
    "Battle Ram": ["Royal Giant", "Electro Wizard"],
    "Cannon Cart": ["Goblin Gang", "Skeletons", "Fireball"],
    "Flying Machine": ["Wizard", "Electro Wizard", "Ice Spirit"],
    "Dark Prince": ["Executioner", "Bowler", "Skeletons"],
    # Synergy for new cards:
    "Mega Knight": ["Goblin Gang", "Skeletons", "Night Witch"],
    "Archer Queen": ["Musketeer", "Fireball", "Hog Rider"]
}

def validate_cards(user_cards):
    """
    Ensure all user-chosen cards are in the available pool.
    """
    for card in user_cards:
        if card not in CARD_POOL:
            return False
    return True

def get_synergy_cards(card):
    """
    Return synergy cards for the given card.
    """
    return SYNERGY.get(card, [])

def generate_deck(user_cards):
    """
    Generate an 8-card deck based on the user's selected cards.
    """
    if not (1 <= len(user_cards) <= 3):
        raise ValueError("You must select between 1 and 3 cards.")
    
    deck = list(user_cards)
    
    synergy_candidates = []
    for card in user_cards:
        synergy_candidates.extend(get_synergy_cards(card))
    
    # Remove duplicates and cards already selected
    synergy_candidates = list(dict.fromkeys([c for c in synergy_candidates if c not in deck]))
    
    for card in synergy_candidates:
        if len(deck) >= 8:
            break
        deck.append(card)
    
    remaining_choices = [card for card in CARD_POOL if card not in deck]
    while len(deck) < 8:
        if not remaining_choices:
            break
        chosen = random.choice(remaining_choices)
        deck.append(chosen)
        remaining_choices.remove(chosen)
    
    return deck[:8]

def main():
    """
    Console-based version for testing.
    """
    print("Welcome to the Clash Royale Deck Builder!")
    print("Available cards:")
    for card in CARD_POOL:
        details = CARDS_DATA[card]
        print(f"{card} - Elixir: {details['elixir']}, Rarity: {details['rarity']}, Type: {details['type']}")
    
    user_input = input("Enter 1 to 3 of your favorite cards (comma separated): ")
    user_cards = [card.strip() for card in user_input.split(",") if card.strip()]
    
    if not (1 <= len(user_cards) <= 3):
        print("Error: Please enter between 1 and 3 cards.")
        return
    
    if not validate_cards(user_cards):
        print("Error: One or more of your chosen cards are not in the available card pool.")
        return
    
    deck = generate_deck(user_cards)
    print("\nYour generated deck:")
    for card in deck:
        details = CARDS_DATA[card]
        print(f"{card} - Elixir: {details['elixir']}, Rarity: {details['rarity']}, Type: {details['type']}")

if __name__ == "__main__":
    main()