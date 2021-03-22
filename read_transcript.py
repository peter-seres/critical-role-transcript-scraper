from file_utils import load_json
from dataclasses import dataclass
from typing import List, Iterator
import re

players = ["TRAVIS", "LAURA", "SAM", "LIAM", "ASHLEY", "TALIESIN", "MARISHA",
           "ASHLY", "DEBORAH", "SUMALEE", "KHARY", "MICA"]

dm = ["MATT", "MATTHEW"]
other = ["MARK", "DANI", "AUDIENCE", "BRIAN", "EVERYONE", "ALL", "BRANDON", "KEVIN", "MEREDITH", ""]

name_typos = {
    "MATT": ["MTT", "MATTHEW", "MTAT", "MAT", "AMTT", "MATTT"],
    "SAM": ["SAN", "SMA", "NOTT", "SASM"],
    "TRAVIS": ["TARVIS", "TRVS", "TRAVS", "TRAIVS", "FJORD", "TRAVIA"],
    "TALIESIN": ["TALIEISN", "TALISEIN", "TALISIN", "TALISEN", "MOLLY", "TALEISIN", "TALEISN"],
    "MARISHA": ["MAIRSHA", "MRAISHA", "ARISHA", "MARSISHA", "MATISHA", "MARIASHA", "MARISH", "MARISA", "MAISHA",
                "BEAU", "MARISAH", "MARSIAH", "MARSHA", "MARIHSA"],
    "LAURA": ["LAUR", "LAUAR", "LAUR", "LARUA", "LAIRA", "LAUDA", "LAUREN"],
    "LIAM": ["CALEB", "IAM", "LAIM"],
    "SUMALEE": ["NILA"],
    "ASHLEY": ["ASLHEY", "ASHEY", "YASHA", "AHSLEY", "ASHELY"]
}


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

    # filter out empty pieces:
    texts = [t for t in texts if t.who != '' and t.text != '']

    # Fix name typos:
    for t in texts:
        for k, v in name_typos.items():
            if t.who in v:
                t.who = k

    # Filter the weird mistakes where text field is a TextPiece:
    texts = [t for t in texts if type(t.text) is str]

    # Filter out non-player and non-dm dialogues:
    texts = [t for t in texts if t.who in players + dm]

    # todo: filter out commercials

    # DM spoken texts
    matt_texts = [t for t in texts if t.who == "MATT"]

    # Fun facts:
    word_count = sum([len(t.text.split()) for t in texts])
    word_count_matt = sum([len(t.text.split()) for t in matt_texts])


def test_regex_pattern():
    import re
    pattern = r'([A-Z]{3,}):'

    x = "just a normal string"
    y = "MATT: This starts a new one"
    z = "this has text before, MATT: wooah"

    print(re.split(pattern, x))
    print(re.split(pattern, y))
    print(re.split(pattern, z))
