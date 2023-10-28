from typing import List, Dict


# This is global singleton manager
class Locator:
    def __init__(self):
        self.globals: Dict[type, any] = dict()

    # Register instance by its type
    def register(self, instance: any) -> None:
        self.globals[type(instance)] = instance

    def get(self, key: type) -> any:
        return self.globals.get(key)

    def __getitem__(self, key: type) -> any:
        return self.globals[key]

    def __setitem__(self, key: type, value: any) -> None:
        self.globals[key] = value


class G:
    __instance: Locator = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance: Locator = Locator()
        return cls.__instance
