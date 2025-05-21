from silent_auction import find_winner

def test_find_winner_success():
    bidders = [{"name": 'Aksel', "bid": 150},
               {"name": 'Izet', "bid": 350},
               {"name": 'Harley', "bid": 40}
    ]
    expected = 'Izet'
    result = find_winner(bidders=bidders)
    assert(expected==result)
    
def test_find_winner_fail():
    bidders = [{"name": 'Aksel', "bid": 150},
               {"name": 'Izet', "bid": 350},
               {"name": 'Harley', "bid": 40}
    ]
    expected = 'Aksel'
    result = find_winner(bidders=bidders)
    assert(expected!=result)