"""Lesson 3. Task 5"""

print("Привет, README!")

text = (
    "Lorem Ipsum - это текст-«рыба», часто используемый в печати и веб-дизайне. "
    "Lorem Ipsum."
)
print(text)


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Привет, {name}"


hello_world = "мир"
numbers = [1, 2, 3, 4, 5]

print(add(5, 10))
print(greet("Luke Skywalker"))
print(greet(hello_world))