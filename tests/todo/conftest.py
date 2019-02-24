import pytest


@pytest.fixture()
def todo_repo(mocker):
    repo = TestTodoRepository()
    mock_repo = mocker.patch("app.todo.todo_repository_factory.TodoRepositoryFactory.create")
    mock_repo.return_value = repo
    return repo


class TestTodoRepository:
    def __init__(self, todos=None):
        self.todos = todos or []

    def read(self, todo_id):
        for todo in self.todos:
            if todo.todo_id == todo_id:
                return todo
        return None

    def add(self, todo):
        self.todos.append(todo)
        return todo

    def update(self, todo):
        return todo