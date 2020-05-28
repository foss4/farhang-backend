def group_by_key(data: list, key_name: str):
    keys = set([item[key_name] for item in data])
    return [
        {
            "title": key,
            "results": [item for item in data if item[key_name] == key]
        } for key in keys
    ]
