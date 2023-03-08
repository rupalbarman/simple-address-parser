HOUSE_SHORT_NOTATIONS = (
    'no',
    'number',
    'flat',
    'apt',
    'apartment',
    'building',
    'bldg',
    'block',
)

STREET_SHORT_NOTATIONS = (
    'street',
    'st',
    'av',
    'avenue',
    'alley',
    'rd',
    'road',
    'town',
)


def get_house_score(token_index_map: dict, curr_idx: int, house_on_left=True) -> int:
    '''
    Returns a 'house' integer score which, if greater than 0, suggests the given token (curr_idx) could be a part
    of house number.

    Uses a bias to know whether a house number is present on the left or right side and uses this bias
    to assign scores to neighboring tokens.
    '''
    # set neighbour token based on house bias direction
    if house_on_left:
        _, next_house_score = token_index_map.get(curr_idx - 1, [None, 0])
    else:
        _, next_house_score = token_index_map.get(curr_idx + 1, [None, 0])

    curr_token, curr_house_score = token_index_map.get(curr_idx)

    # positive conventional house number checks
    if curr_token.isnumeric():
        curr_house_score = max(next_house_score, 0) + 1

    elif curr_token.isalnum() and any(n in curr_token for n in '1234567890'):
        curr_house_score = max(next_house_score, 0) + 1

    elif curr_token.lower() in HOUSE_SHORT_NOTATIONS:
        curr_house_score += 1

    elif len(curr_token) < 2:
        curr_house_score = max(next_house_score, 0) + 1

    # negative conventional house number checks
    if any(x in curr_token for x in STREET_SHORT_NOTATIONS):
        curr_house_score -= 1

    return curr_house_score


def parse(raw_address: str) -> tuple:
    '''
    Parses a given informal address into a tuple containing the house number
    and the street.
    '''
    house = ''
    street = ''

    # strip delimeters since we don't want to rely on it - BUT WE SHOULD!
    tokens = [t.replace(',', '') for t in raw_address.strip().split(' ')]
    token_index_map = {i: [v, 0] for i, v in enumerate(tokens)}

    i, j = 0, len(tokens) - 1

    # Lemma 1, house can either be on left or right. Identify the direction bias

    token_index_map[i][1] = get_house_score(token_index_map, i)
    token_index_map[j][1] = get_house_score(token_index_map, j)

    if token_index_map[i][1] < token_index_map[j][1]:
        # right bias
        for x in range(j-1, i+1, -1):
            token_index_map[x][1] = get_house_score(token_index_map, x)
    else:
        # left bias or bias not known
        # so we make it left bias only since it cannot both be same
        if token_index_map[i][1] == token_index_map[j][1]:
            token_index_map[i][1] = token_index_map[j][1] - 1

        for x in range(i+1, j-1):
            token_index_map[x][1] = get_house_score(token_index_map, x)

    for x in range(len(tokens)):
        if token_index_map[x][1] > 0:
            house += token_index_map[x][0] + ' '
        else:
            street += token_index_map[x][0] + ' '

    return house.strip(), street.strip()
