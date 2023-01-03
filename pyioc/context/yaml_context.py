import yaml
from typing import Any, List
from pyioc.context.context import Context


def get_val(d: dict, key: str, types: List[Any] = [], default: Any = None) -> Any:
    if key not in d:
        if default != None:
            return default
        raise Exception(f"{key} missing from {d}")
    val = d[key]
    if types and type(val) not in types:
        raise Exception(
            "Unexpected type\n"
            + f"Type of {val} <<{key}>> not in ({[t for t in types]})"
        )
    return val


class YAMLContext(Context):
    __services: dict = {}
    __config: dict = {}

    def __init__(self, config_file: str):
        self.__config = yaml.safe_load(open(config_file, "r"))
        for service in self.__config["nuts"]:
            id = get_val(service, "id", [str])
            if id not in self.__services:
                self.__create_service(service)

    def __create_service(self, d: dict) -> None:
        id = get_val(d, "id", [str])
        cls = get_val(d, "class", [str])
        module_str = cls.split(":")[0]
        class_str = cls.split(":")[1]
        module = __import__(module_str)
        class_ = getattr(module, class_str)
        instance = class_()
        for property in d["properties"]:
            name = get_val(property, "name", [str])
            if "value" in property:
                value = get_val(property, "value", [])
                getattr(instance, f"set_{name}")(value)
            elif "ref" in property:
                ref = get_val(property, "ref", [str], default=None)
                if ref not in self.__services:
                    dependency = [d for d in self.__config["nuts"] if d["id"] == ref]
                    if len(dependency) != 1:
                        raise Exception(f"Unknown ref {ref}")
                    self.__create_service(dependency[0])
                getattr(instance, f"set_{name}")(self.__services[ref])
            else:
                raise Exception(f"Missing 'ref' or 'value' the {name} property of {id}")
        self.__services[id] = instance

    def get_nut(self, id: str) -> Any:
        return self.__services[id]
