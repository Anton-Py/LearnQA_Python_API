class TestExempleShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Длина фразы: '{phrase}' больше 15 символов"

#  pytest -s Lesson_3/test_example_10_short_phrase.py -k "test_short_phrase"

