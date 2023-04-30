def get_card_from_file(card_name, file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    cards = {}
    current_card_title = ''
    current_card_data = []

    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            # Skip empty lines
            continue
        if stripped_line.isalnum():
            # If the line contains only alphanumeric characters, it's a new card title
            if current_card_title:
                # If we've already started reading a card, store it in the dictionary
                cards[current_card_title] = current_card_data
            current_card_title = stripped_line
            current_card_data = []
        else:
            # Otherwise, it's a line of data
            row_data = stripped_line.split(',')
            current_card_data.append(row_data)

    # Store the last card in the dictionary
    if current_card_title:
        cards[current_card_title] = current_card_data

    if cards[card_name]:
        return cards[card_name]
    else:
        KeyError('Card name not found in file')

