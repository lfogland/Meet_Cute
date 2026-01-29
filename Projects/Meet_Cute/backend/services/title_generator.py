import random

def generate_title(story_text: str, city: str | None = None):
    story_text = story_text.lower()

    objects = ["coffee", "croissant", "train", "book", "umbrella", "seat"]
    found_object = None

    for obj in objects:
        if obj in story_text:
            found_object = obj
            break

    templates = [
        "The Last {}",
        "Before the {}",
        "An Ordinary {}",
        "Just One {}",
        "The {} That Started It All"
    ]

    if found_object:
        title = random.choice(templates).format(found_object.capitalize())
    elif city:
        title = f"A Small Moment in {city}"
    else:
        title = "An Ordinary Moment"

    return title
