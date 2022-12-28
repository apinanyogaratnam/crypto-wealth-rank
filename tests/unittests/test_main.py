import contextlib
from crypto_wealth_rank.main import rank_wealth


class TestMain:
    def test_rank_wealth_return_value(self: 'TestMain'):
        assert rank_wealth(100) == 'Fish'

    def test_greetings_return_type(self: 'TestMain'):
        assert isinstance(rank_wealth(100), str)

    def test_all_possible_returns(self: 'TestMain'):
        assert rank_wealth(1) == 'Shrimp'
        assert rank_wealth(10) == 'Crab'
        assert rank_wealth(50) == 'Octopus'
        assert rank_wealth(100) == 'Fish'
        assert rank_wealth(500) == 'Dolphin'
        assert rank_wealth(1000) == 'Shark'
        assert rank_wealth(5000) == 'Whale'
        assert rank_wealth(6000) == 'HumpBack Whale'

    def test_error_handling(self: 'TestMain'):
        assert rank_wealth(None) is None

        result = None
        with contextlib.suppress(ValueError):
            result = rank_wealth('gibberish')
        assert isinstance(result, None)

    def test_negative_values(self: 'TestMain'):
        assert rank_wealth(-10) == 'Shrimp'
