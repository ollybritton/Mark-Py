import random
import re

# === CHANGE THESE VARIABLES ===

FILE = "samples/interstellar.txt"
OUTPUT = "results/output.txt"

PARAGRAPHS_PER_FILE = 3
SENTENCES_PER_PARAGRAPH = 1
MAX_WORDS = 30
CHAIN_LENGTH = 2

# ==============================


class Markov:
    chain_length = CHAIN_LENGTH
    max_words = MAX_WORDS
    separator = "\x01"
    stop = "\x02"

    @classmethod
    def parse_messages(self, messages):
        chain_map = {}
        starting = []

        for i in range(len(messages)):
            message = messages[i].split(" ")
            messages[i] = messages[i] + " " + self.stop
            messages[i] = messages[i].split(" ")
            chains = []

            if message[0] not in starting:
                starting.append(message[0])

            for i in range(len(message) - self.chain_length):
                chains.append(message[i:i + self.chain_length + 1])

            for chain in chains:
                head = tuple(chain[:self.chain_length])
                tail = chain[self.chain_length:]

                if head in chain_map:
                    chain_map[head].append(tail[0])

                else:
                    chain_map[head] = tail

        return [starting, chain_map]

    @classmethod
    def create_message(self, chains):
        starting = random.choice(chains[0])
        chains = chains[1]

        curr = [starting]

        for _ in range(self.max_words):
            previous = curr[-1]
            possible = []

            if previous == self.stop:
                break

            for chain in chains:
                if chain[0] == previous:
                    possible.append(chain)

            if len(possible) == 0:
                break

            possible = random.choice(possible)
            curr.append(possible[1])
            curr.append(random.choice(chains[possible]))

        return " ".join(curr).strip("\x02")

    @classmethod
    def create_paragraph(self, chains, length=5):
        text = ""

        for _ in range(length):
            text += self.create_message(chains)
            text += "\n"

        return text

    @classmethod
    def parse_file(self, name):
        result = ""

        with open(name, "r") as f:
            result = f.read()

        result = result.split(".")
        result = list(map(lambda x: x.strip("\n"), result))
        result = list(map(lambda x: x.strip("\\n"), result))

        return self.parse_messages(result)

    @classmethod
    def message_from_file(self, name):
        return self.create_message(self.parse_file(name))

    @classmethod
    def paragraph_from_file(self, name, length=5):
        return self.create_paragraph(self.parse_file(name), length)


def main():
    text_map = Markov.parse_file(FILE)

    print(Markov.create_message(text_map))

    # for _ in range(PARAGRAPHS_PER_FILE):
    #     output += Markov.create_paragraph(text_map,
    #                                       SENTENCES_PER_PARAGRAPH) + "\n\n"

    # with open(OUTPUT, "w") as f:
    #     f.write(output)


if __name__ == '__main__':
    main()
