
def decrypt_char(char, key):
    """Decrypts a single character while preserving case."""
    if 'a' <= char <= 'z':  # Check if lowercase
        base = ord('a')
    elif 'A' <= char <= 'Z':  # Check if uppercase
        base = ord('A')
    else:
        return char  # Return unchanged if it's not a letter

    position = ord(char) - base
    new_position = (position - key) % 26
    return chr(new_position + base)  # Convert back to character


def decrypt_caesar(text, key):
    return ''.join(decrypt_char(char, key) for char in text)

# You may use your code from the previous assignment


def main():
    MESSAGE = """
    Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, "Yn no, Vlony?" (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy'm wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
    """
    print(decrypt_caesar(MESSAGE, 20))



if __name__ == "__main__":
    main()

