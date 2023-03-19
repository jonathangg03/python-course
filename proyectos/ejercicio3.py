def palindrome(text):
    text = text.replace(" ", "").lower()
    first = 0
    last = len(text)-1
    result = True

    for _ in text:
        if last != -1:
            if text[first] != text[last]:
                result = False
            last -= 1
            first += 1

    print(result)
    return result


palindrome("Hola mundo")
palindrome("Amo la paloma")
palindrome("Abba")
palindrome("aaassssddd")
