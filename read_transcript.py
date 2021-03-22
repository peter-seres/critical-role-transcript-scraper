from file_utils import load_json
from dataclasses import dataclass
from typing import List, Iterator
import re

players = ["TRAVIS", "LAURA", "BRIAN", "SAM", "LIAM", "ASHLEY", "TALIESIN", "MARISHA", "ALL", "ASHLY", "MARK", "DANI",
           "AUDIENCE"]
dm = "MATT"


@dataclass
class TextPiece:
    """ Data model for a singular piece of dialogue. """
    who: str
    text: str


def generate_text_pieces(episode_data: List[dict]) -> Iterator[TextPiece]:
    """ Generates all text pieces for a single episode. """

    person_hold = ""
    accumulated_string = ""

    for t in episode_data:

        text = t["text"]
        text = text.replace("\n", " ")

        pattern = r'([A-Z]{3,}):'

        split = re.split(pattern, text)

        if len(split) == 1:
            accumulated_string += split[0]

        if len(split) == 2:
            print("This shouldn't happen")
            raise Exception(f"Unhandled case. For string {text} with split: {split}")

        if len(split) == 3:
            before, person, after = split

            accumulated_string += " " + before

            if person == '':
                print(f"another edge case - null person: {person}, {text}, {split}")

            text_piece = TextPiece(who=person_hold, text=accumulated_string.strip())

            person_hold = person
            accumulated_string = after

            yield text_piece


if __name__ == '__main__':
    # All of it:
    data = load_json("data/transcripts_c2.json")

    # Just episode 1:
    ep1_data = data["0"]

    # Generate the text pieces:
    texts_ep1 = list(generate_text_pieces(episode_data=ep1_data))

    # Let's do all of it:
    texts = []
    for idx, ep_data in data.items():
        texts += list(generate_text_pieces(episode_data=ep_data))

    matt_texts = [t for t in texts if t.who == "MATT"]
    people = set([t.who for t in texts])

    m = parsing_mistakes = [t for t in texts if t.who not in players and t.who != "MATT"]


def test_regex_pattern():
    import re
    pattern = r'([A-Z]{3,}):'

    x = "just a normal string"
    y = "MATT: This starts a new one"
    z = "this has text before, MATT: wooah"

    print(re.split(pattern, x))
    print(re.split(pattern, y))
    print(re.split(pattern, z))

