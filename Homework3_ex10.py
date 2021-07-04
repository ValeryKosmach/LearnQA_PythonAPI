class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase should be less than 15 characters, your phrase {len(phrase)} characters"
