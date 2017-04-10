"""How long will it take the train to reach its final destination?"""

import pytest

from solutions.kyu_7.how_long_will_it_take_the_train_to_reach_its_final_destination import reach_destination

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5,10), 'The train will be there in 0.5 hours.'),
        ((80,20), 'The train will be there in 4 hours.'),
        ((80,80), 'The train will be there in 1 hour.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert reach_destination(*args) == expected
