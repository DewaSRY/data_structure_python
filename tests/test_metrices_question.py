""" 

"""

from src.matrices_question import (
    Metric,
    deptFirstSearch_metric,
    breadFirstSearch_metric,
)
from unittest import TestCase


class TestMetric(TestCase):

    def setUp(self) -> None:
        self.myMetric: Metric = Metric(
            metric=[
                [0, 1],
                [2, 3],
            ]
        )

    def test_traverse_metric(self):
        assert self.myMetric.right() == 1
        assert self.myMetric.down() == 3
        assert self.myMetric.left() == 2
        assert self.myMetric.up() == 0

    def test_deptFirstSearch_metric(self):
        actual = deptFirstSearch_metric(metric=self.myMetric)
        assert actual == [0, 1, 3, 2]

    def test_breadFirstSearch_metric(self):
        actual = breadFirstSearch_metric(metric=self.myMetric)
        assert actual == [0, 1, 2, 3]
