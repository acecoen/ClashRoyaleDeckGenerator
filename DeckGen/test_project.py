import pytest
from project import validate_cards, get_synergy_cards, generate_deck, CARD_POOL, SYNERGY

def test_validate_cards_valid():
    # Test with valid cards.
    assert validate_cards(["Hog Rider", "Musketeer"]) == True

def test_validate_cards_invalid():
    # Test with one invalid card.
    assert validate_cards(["Hog Rider", "Invalid Card"]) == False

def test_get_synergy_cards_existing():
    # Test retrieving synergy cards for a card that has a defined synergy list.
    expected = SYNERGY.get("Hog Rider", [])
    assert get_synergy_cards("Hog Rider") == expected

def test_get_synergy_cards_nonexistent():
    # Test for a card with no synergy mapping.
    assert get_synergy_cards("Cannon") == []

def test_generate_deck_size():
    # Test that the generated deck always has exactly 8 cards.
    user_cards = ["Hog Rider"]
    deck = generate_deck(user_cards)
    assert len(deck) == 8

def test_generate_deck_contains_user_cards():
    # Test that the deck always includes the user's chosen cards.
    user_cards = ["Miner", "Golem"]
    deck = generate_deck(user_cards)
    for card in user_cards:
        assert card in deck

def test_generate_deck_max_user_cards():
    # Test with the maximum of 3 user-selected cards.
    user_cards = ["Hog Rider", "Miner", "Golem"]
    deck = generate_deck(user_cards)
    assert len(deck) == 8
    for card in user_cards:
        assert card in deck

def test_generate_deck_invalid_user_cards_count():
    # Test that an invalid number of user cards raises a ValueError.
    with pytest.raises(ValueError):
        generate_deck([])  # No cards provided.
    with pytest.raises(ValueError):
        generate_deck(["Hog Rider", "Miner", "Golem", "Musketeer"])  # More than 3 cards.