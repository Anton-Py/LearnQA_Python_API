class TestExempleShortPhrase():
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Длина фразы: '{phrase}' больше 15 символов"

