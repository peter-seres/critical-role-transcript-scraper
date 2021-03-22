from file_utils import load_json
from dataclasses import dataclass
from typing import List, Iterator


players = ["TRAVIS", "LAURA", "BRIAN", "SAM", "LIAM", "ASHLEY", "TALIESIN", "MARISHA"]
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

        # todo: sometimes there is content before the name!!!

        split = [s.strip() for s in text.split(":")]

        if len(split) == 1:
            accumulated_string += " " + split[0]

        elif len(split) == 2:
            person, string = split

            text_piece = TextPiece(who=person_hold, text=accumulated_string)

            person_hold = person
            accumulated_string = string

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
    for idx, episode_data in data.items():
        texts += list(generate_text_pieces(episode_data=episode_data))

    matt_texts = [t for t in texts if t.who == "MATT"]
    people = set([t.who for t in texts])
