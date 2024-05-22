from typing import List, Dict

def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    text = text.lower()
    word_list = text.split()
    word_count = {word: 0 for word in words}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
    return word_count


if __name__ == "__main__":
    assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                         ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
    print('OK')
