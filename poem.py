import nltk
import pronouncing
import random

dictionary = {
    "NN": ["love", "life", "dream", "hope", "star", "flower", "heart", "world", "light", "night"],
    "NNS": ["friends", "birds", "songs", "words", "eyes", "skies", "trees", "leaves", "seas", "dreams"],
    "VB": ["sing", "dance", "write", "read", "play", "fly", "run", "walk", "smile", "cry"],
    "VBD": ["sang", "danced", "wrote", "read", "played", "flew", "ran", "walked", "smiled", "cried"]
}

rhyme_schemes = {
    1: ["A"],
    2: ["AA", "BB"],
    3: ["ABA"],
    4: ["AABB", "ABAB"],
    5: ["AABBA", "ABBAA"],
    6: ["AABBAA", "ABABAB"],
    7: ["AABBABA", "ABABABA"],
    8: ["AABBCCDD", "ABABCDCD"],
    9: ["AABBCCDDA", "ABABCDCDD"],
    10: ["AABBCCDDEE", "ABABCDCDEE"]
}

syllables_per_line = 8

def generate_poem(topic):
    tokens = nltk.word_tokenize(topic)
    tags = nltk.pos_tag(tokens)

    words, rhymes = [], []

    for tag in tags:
        word = random.choice(dictionary.get(tag[1], [tag[0]]))
        words.append(word)

    topic_length = len(words)
    rhyme_scheme = rhyme_schemes.get(topic_length, ["A"] * topic_length)

    for rhyme_pattern in rhyme_scheme:
        rhyme_words = []
        for i, letter in enumerate(rhyme_pattern):
            if letter not in rhymes:
                rhyme_list = pronouncing.rhymes(words[i])
                rhyme = words[i] if len(rhyme_list) == 0 else random.choice(rhyme_list)
                rhymes.append((letter, rhyme))
            else:
                rhyme = [r[1] for r in rhymes if r[0] == letter][0]
            rhyme_words.append(rhyme)

        words = rhyme_words

    poem = " ".join(words)
    return poem.capitalize()

if __name__ == "__main__":
    topic = input("Enter a topic for the poem: ")
    poem = generate_poem(topic)
    print(poem)
