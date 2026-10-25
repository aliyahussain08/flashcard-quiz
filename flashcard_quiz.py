cards = {
    "The 4 Ps are product, price, place and...?": "promotion",
    "Total revenue minus total costs equals...?": "profit",
    "Rent doesn't change with output. What type of cost is it?": "fixed",
    "Which leadership style involves the leader making all decisions alone?": "autocratic",
    "Which theorist created the hierarchy of needs?": "maslow",
    "Which theorist believed workers are mainly motivated by money?": "taylor",
    "In PESTLE, what does the T stand for?": "technological",
    "In Ansoff's matrix, selling existing products in new markets is called...?": "market development",
    "What does the acid test ratio measure?": "liquidity",
    "A business's sales as a percentage of total market sales is called...?": "market share"
}

score = 0
for question, answer in cards.items():
    guess = input(question + " ")
    if guess.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong, it was:", answer)

print("You got", score, "out of", len(cards))
