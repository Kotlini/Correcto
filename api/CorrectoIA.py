import enchant as enchant


def correct_spelling(text):
    d = enchant.Dict("fr_FR")

    words = text.split()

    corrected_text = []
    for word in words:
        if not d.check(word):
            suggestions = d.suggest(word)
            if len(suggestions) > 0:
                corrected_text.append(suggestions[0])
            else:
                corrected_text.append(word)
        else:
            corrected_text.append(word)

    corrected_text = " ".join(corrected_text)

    return corrected_text