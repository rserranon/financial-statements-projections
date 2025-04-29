# global_state.py

from typing import Self  # Python 3.11+

StateValue = int | float | str | bool | list[object] | dict[str, object]

class GlobalState:
    _instance: Self | None = None
    data: dict[str, StateValue]

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "data"):
            self.data = {}

    def set(self, key: str, value: StateValue) -> None:
        self.data[key] = value

    def get(self, key: str) -> StateValue | None:
        return self.data.get(key)
