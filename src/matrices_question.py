""" 

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class MetricCoordinate:
    coll: int
    row: int

    def __init__(self, coll: int, row: int) -> None:
        self.coll = coll
        self.row = row

    def leftCoordinate(self) -> Self:
        return MetricCoordinate(coll=self.coll, row=self.row - 1)

    def rightCoordinate(self) -> Self:
        return MetricCoordinate(coll=self.coll, row=self.row + 1)

    def upCoordinate(self) -> Self:
        return MetricCoordinate(coll=self.coll - 1, row=self.row)

    def downCoordinate(self) -> Self:
        return MetricCoordinate(coll=self.coll + 1, row=self.row)


class Metric:

    def __init__(self, metric: list[list[int]] = [[]]) -> None:
        self.metric = metric
        self.current_coll = 0
        self.current_row = 0

    def getCoordinate(self):
        return MetricCoordinate(coll=self.current_coll, row=self.current_row)

    def setCoordinate(self, coordinate: MetricCoordinate):
        self.current_coll = coordinate.coll
        self.current_row = coordinate.row

    def size(self):
        return len(self.metric) * len(self.metric[0])

    def getValue(self):
        return self.metric[self.current_coll][self.current_row]

    def setValue(self, value: int):
        self.metric[self.current_coll][self.current_row] = value

    def left(self):
        if self._canLeft():
            self.current_row -= 1
            return self.metric[self.current_coll][self.current_row]
        return -1

    def right(self):
        if self._canRight():
            self.current_row += 1
            return self.metric[self.current_coll][self.current_row]
        return -1

    def up(self):
        if self._canUp():
            self.current_coll -= 1
            return self.metric[self.current_coll][self.current_row]
        return -1

    def down(self):
        if self._canDown():
            self.current_coll += 1
            return self.metric[self.current_coll][self.current_row]
        return -1

    def nextLeft(self) -> int:
        if self._canLeft():
            return -self.metric[self.current_coll][self.current_row - 1]
        return -1

    def nextRight(self):
        if self._canRight():
            return self.metric[self.current_coll][self.current_row + 1]
        return -1

    def nextUp(self):
        if self._canUp():
            return self.metric[self.current_coll - 1][self.current_row]
        return -1

    def nextDown(self):
        if self._canDown():
            return self.metric[self.current_coll + 1][self.current_row]
        return -1

    def _canLeft(self):
        return self.current_row - 1 > -1

    def _canRight(self):
        return self.current_row + 1 < len(self.metric[0])

    def _canUp(self):
        return self.current_coll - 1 > -1

    def _canDown(self):
        return self.current_coll + 1 < len(self.metric)


""" 
Metric depthFirstSearch
"""


def deptFirstSearch_metric(metric: Metric) -> list[int]:
    currentMetric = metric
    return _deptFirstSearch_metric(metric=currentMetric)


def moveMetric(metric: Metric) -> bool:
    canMove = False

    if metric.nextRight() != -1:
        metric.right()
        canMove = True
    elif metric.nextDown() != -1:
        metric.down()
        canMove = True
    elif metric.nextLeft() != -1:
        metric.left()
        canMove = True
    elif metric.nextUp() != -1:
        metric.up()
        canMove = True

    return canMove


def _deptFirstSearch_metric(metric: Metric, result: list[int] = []) -> list[int]:
    result.append(metric.getValue())
    metric.setValue(value=-1)

    if moveMetric(metric=metric):
        return _deptFirstSearch_metric(metric=metric, result=result)
    return result


""" 
Metric bread first search
"""


def _fillMetricQueue(
    metric: Metric, queue: list[MetricCoordinate], currentCoordinate: MetricCoordinate
) -> list[MetricCoordinate]:
    if metric.nextRight() != -1:
        queue.append(currentCoordinate.rightCoordinate())
    if metric.nextDown() != -1:
        queue.append(currentCoordinate.downCoordinate())
    if metric.nextLeft() != -1:
        queue.append(currentCoordinate.leftCoordinate())
    if metric.nextUp() != -1:
        queue.append(currentCoordinate.upCoordinate())
    return queue


def breadFirstSearch_metric(metric: Metric) -> list[int]:
    result: list[int] = []
    queue: list[MetricCoordinate] = [metric.getCoordinate()]

    while len(result) != metric.size():
        currentCoordinate = queue.pop(0)
        metric.setCoordinate(currentCoordinate)
        result.append(metric.getValue())
        metric.setValue(-1)
        _fillMetricQueue(
            metric=metric, queue=queue, currentCoordinate=currentCoordinate
        )

    return result
