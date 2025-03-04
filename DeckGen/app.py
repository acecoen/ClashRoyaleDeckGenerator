from flask import Flask, render_template, request
from project import CARD_POOL, CARDS_DATA, validate_cards, generate_deck

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    deck = None
    error = None
    if request.method == 'POST':
        user_cards_input = request.form.get('cards')
        if user_cards_input:
            user_cards = [card.strip() for card in user_cards_input.split(',') if card.strip()]
            if not (1 <= len(user_cards) <= 3):
                error = "Please enter between 1 and 3 cards."
            elif not validate_cards(user_cards):
                error = "One or more of your chosen cards are not in the available card pool."
            else:
                deck = generate_deck(user_cards)
    return render_template('index.html', deck=deck, error=error, card_pool=CARD_POOL, card_data=CARDS_DATA)

if __name__ == '__main__':
    app.run(debug=True)