from file_utils import load_json
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TextPiece:
    who: str
    text: str


players = ["TRAVIS, LAURA, BRIAN, SAM, ASHLEY, TALESIN, MARISHA"]
dm = "MATT"


class Episode:
    def __init__(self, episode_data: List[dict]):
        self.texts = []

        # Iterate through the text elements and parse out who's talking.
        # The person talking is only specified when it changes, so there is a string buffer,

        person_hold = ""
        accumulated_string = ""

        for t in episode_data:

            text = t["text"]
            text = text.replace("\n", " ")
            split = [s.strip() for s in text.split(":")]

            if len(split) == 1:
                accumulated_string += " " + split[0]

            elif len(split) == 2:
                person, string = split

                text_piece = TextPiece(who=person_hold, text=accumulated_string)
                self.texts.append(text_piece)

                person_hold = person
                accumulated_string = string


if __name__ == '__main__':
    data = load_json("data/transcripts_c2.json")
    ep1 = Episode(episode_data=data["0"])
