import pytest

import task_service


## creat_task TESTS ##
def test_create_task_rejects_title():
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        task_service.create_task("   ")


def test_create_task_rejects_invalid_priority():
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task(
            "Test task",
            priority="critical"
        )

    assert str(exc_info.value) == (
        f"Priority must be one of {task_service.VALID_PRIORITIES}."
    )


def test_create_task_normalizes_and_passes_data_to_database(monkeypatch):
    captured_data = {}

    def fake_add_task(title, description=None, priority="medium", due_at=None):
        captured_data["title"] = title
        captured_data["description"] = description
        captured_data["priority"] = priority
        captured_data["due_at"] = due_at

        return 42

    monkeypatch.setattr(
        task_service.database,
        "add_task",
        fake_add_task
    )

    task_id = task_service.create_task(
        "  Study Docker  ",
        "  Learn container basics  ",
        "HIGH",
        None
    )

    assert task_id == 42
    assert captured_data["title"] == "Study Docker"
    assert captured_data["description"] == "Learn container basics"
    assert captured_data["priority"] == "high"
    assert captured_data["due_at"] is None


    ## get_task TESTS ##
    def test_get_task_returns_existing_task(monkeypatch):
        fake_task = {
            "id": 7,
            "title": "Study Docker",
            "status": "active"
        }

        def fake_get_task_by_id(task_id):
            return fake_task

        monkeypatch.setattr(
            task_service.database,
            "get_task_by_id",
            fake_get_task_by_id
        )

        result = task_service.get_task(7)

        assert result == fake_task