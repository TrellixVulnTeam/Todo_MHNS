from app.todo.domains.todo import Todo
from app.todo.domains.todo_type import TodoType


class Habit(Todo):
    def __init__(self,
                 todo_id=None,
                 todo_owner=None,
                 name=None,
                 description=None,
                 points_per=None,
                 completion_points=None,
                 frequency=None,
                 period=None,
                 buffer=None,
                 categories=None,
                 tags=None,
                 actions=None,
                 created_date=None,
                 modified_date=None):
        super().__init__(todo_id=todo_id,
                         todo_owner=todo_owner,
                         name=name,
                         description=description,
                         todo_type=TodoType.HABIT,
                         completion_points=completion_points,
                         categories=categories,
                         tags=tags,
                         actions=actions,
                         created_date=created_date,
                         modified_date=modified_date)
        self.points_per = points_per or 0
        self.frequency = frequency
        self.period = period
        self.buffer = buffer

    def to_dict(self):
        todo_dict = super().to_dict()
        todo_dict.update({
            "pointsPer": self.points_per,
            "frequency": self.frequency,
            "period": {
                "periodType": self.period.period_type.name,
                "amount": self.period.amount,
                "start": self.period.start
            },
            "buffer": {
                "bufferType": self.buffer.buffer_type.name,
                "amount": self.buffer.amount,
            }
        })
        return todo_dict
