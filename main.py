import random
import markovify

# === CHANGE THESE VARIABLES ===

FILE = "samples/shakespeare.txt"
OUTPUT = "results/output.txt"

PARAGRAPHS_PER_FILE = [10, 30]
SENTENCES_PER_PARAGRAPH = [2, 6]
CHAIN_LENGTH = 2

# ==============================


def create_model_from_file(file_name, stae_size=CHAIN_LENGTH):
    with open(file_name, "r") as f:
        return markovify.Text(f.read(), state_size=CHAIN_LENGTH)


def random_bounded_number(bounds):
    if type(bounds) == int:
        return bounds

    else:
        return random.randint(bounds[0], bounds[1])


def main():
    new_text = ""

    text_model = create_model_from_file(FILE)
    print(text_model.make_sentence())

    for _ in range(random_bounded_number(PARAGRAPHS_PER_FILE)):
        for _ in range(random_bounded_number(SENTENCES_PER_PARAGRAPH)):
            new_sentence = text_model.make_sentence()

            while new_sentence == None:
                new_sentence = text_model.make_sentence()

            new_text += " " + new_sentence

        new_text += "\n\n"

    with open(OUTPUT, "w") as f:
        f.write(new_text)


if __name__ == '__main__':
    main()
