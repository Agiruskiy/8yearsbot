import re

import pytest as pytest

eight_years_pattern = '(8|[вВ].?[сС].?[мМ].?)\s+[лЛ].[тТ]|(2014)'


class Test8YearsPattern:
    positive_cases = [
        "c 8 лет",
        "восемь лет",
        "восемь лет и один месяц",
        "Восемь лет",
        "восемь лет!",
        "восимь лет",
        "Восимь лет",
        "восимь лет!",
        "2014",
        "2014 год",
        "2014-го",
        "с 2014-го",
    ]

    @pytest.mark.parametrize("case", positive_cases)
    def test_positive(self, case):
        result = re.search(eight_years_pattern, case)
        assert result, case

    negative_cases = [
        "7 лет",
    ]

    @pytest.mark.parametrize("case", negative_cases)
    def test_negative(self, case):
        result = re.search(eight_years_pattern, case)
        assert not result, case
