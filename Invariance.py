def process_strings(strings: list[str]) -> None:
    for s in strings:
        print(s)


# В Python списки инвариантны
names: list[str] = ["Alice", "Bob"]
process_strings(names)  # Это OK

objects: list[object] = ["Alice", "Bob"]
process_strings(objects)  # Incorrect type, хотя str наследуется от object
