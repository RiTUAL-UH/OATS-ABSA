import xml.etree.ElementTree as ET
import string
import re

from sklearn.model_selection import train_test_split


# Convert character indices to word indices in the original text
def char_to_original_word_indices(text, start, end):
    return len(text[:start].split()), len(text[:start].split()) + len(text[start:end + 1].split()) - 1



# Convert XML to the second format
def xml_to_aste(xml_string):
    root = ET.fromstring(xml_string)
    polarity_map = {
        "Positive": "POS",
        "Negative": "NEG",
        "Neutral": "NEU",
        "Conflict": "NEU",
    }

    results = []

    for sentence in root.findall(".//sentence"):
        text = sentence.find("text").text
        if not text or text == '':
            continue
        tokens = text.split()
        opinions = []
        for opinion in sentence.findall(".//Opinion"):
            try:
                if len(opinion.attrib) == 0:
                    continue
                target_from_char = int(opinion.get("target_from"))
                target_to_char = int(opinion.get("target_to"))
                opinion_phrase_from_char = int(opinion.get("opinion_phrase_from"))
                opinion_phrase_to_char = int(opinion.get("opinion_phrase_to"))

                # Skip implicit targets or opinion phrases
                if target_from_char == target_to_char or opinion_phrase_from_char == opinion_phrase_to_char:
                    continue

                target_from_word, target_to_word = char_to_original_word_indices(text, target_from_char, target_to_char)
                opinion_from_word, opinion_to_word = char_to_original_word_indices(text, opinion_phrase_from_char,
                                                                                   opinion_phrase_to_char)

                target_words = list(range(target_from_word, target_to_word + 1))
                opinion_words = list(range(opinion_from_word, opinion_to_word + 1))

                opinions.append((target_words, opinion_words, polarity_map[opinion.get("polarity")]))
            except:
                print("Skipped an opinion in: ", text)
                pass

        formatted_sentence = " ".join(tokens)
        formatted_opinions = ", ".join(
            ["([{}], [{}], '{}')".format(", ".join(map(str, op[0])), ", ".join(map(str, op[1])), op[2]) for op in
             opinions])
        results.append("{}####[{}]".format(formatted_sentence, formatted_opinions))

    return results


for domain in ["amazon_ff", "coursera", "hotels"]:
    for data_file in [f"{domain}/quads/data.xml"]:
        with open(data_file, "r") as f:
            xml_data = f.read()
            # Convert XML to desired format
        output = xml_to_aste(xml_data)

        train, validation = train_test_split(output, test_size=0.2, shuffle=False, random_state=1234)
        validation, test = train_test_split(validation, test_size=0.5)
        with open(f"{domain}/aste/train.txt", "w+") as tr, open(
                f"../{domain}/aste/dev.txt",
                "w+") as vl, open(
            f"../{domain}/aste/test.txt", "w+") as te:
            tr.write("\n".join(train))
            vl.write("\n".join(validation))
            te.write("\n".join(test))
