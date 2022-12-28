def rank_wealth(balance: float | int | None) -> str | None:
    if balance is None:
        return None

    wealth_ranks = {
        '1': 'Shrimp',
        '10': 'Crab',
        '50': 'Octopus',
        '100': 'Fish',
        '500': 'Dolphin',
        '1000': 'Shark',
        '5000': 'Whale',
    }

    try:
        balance = str(float(balance))
    except ValueError as e:
        raise ValueError('balance must be an integer or a float') from e

    return wealth_ranks.get(balance, 'HumpBack Whale')
