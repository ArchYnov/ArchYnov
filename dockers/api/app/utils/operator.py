
import re

OPERATOR_TYPES_MONGO = {
    "=": "$eq",
    "!=": "$ne",
    ">": "$gt",
    ">=": "$gte",
    "<": "$lt",
    "<=": "$lte",
    "[]": "$in",
    "[!]": "$nin",
}


def check_operator(operator: str):
    if operator not in OPERATOR_TYPES_MONGO.values():
        raise Exception("Invalid operator")

def check_property(properties: dict, property: str):
    if property not in properties.__fields__.keys():
        raise Exception("Invalid property")

def get_operator(operator: str) -> str:
    if operator not in OPERATOR_TYPES_MONGO.keys():
        return None
    return OPERATOR_TYPES_MONGO[operator]

def get_filter(filters: list) -> dict:
    regex = r"(?P<property>\w+)(?P<operater><>|>=|<=|!=|=|>|<|\[]|\[!]|)(?P<value>.*)"
    filters = [re.finditer(regex, f) for f in filters]
    # print(filters)
    filter = {}
    for f in filters:
        for match in f:
            property = match.group("property")
            operator = match.group("operater")
            value = match.group("value")
            filter[property] = {
                "operator": get_operator(operator),
                "value": value,
            }
    return filter

def get_value_type(model: dict, key: str, value: str) -> str | int | float | bool | list:
    model_type =  model.__fields__[key].type_
    if model_type == bool:
        return True if value.lower() == "true" else False
    elif model_type == int:
        return int(value)
    elif model_type == float:
        return float(value)
    elif model_type == list:
        return value.split(",")
    else:
        return value
