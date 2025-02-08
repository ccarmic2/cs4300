import pytest

def task():
    print("Hello, World!")

def test_task(capfd):
    task()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Hello, World!"
