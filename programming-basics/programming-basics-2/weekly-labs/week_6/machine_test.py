from machine import TextMachine
from machine import Text

def test_TextMachineClass():
    """
    Print Done if all tests passed
    """
    print("Testing TextMachine class...")
    # Each text has three properties: type of the text,
    # number of texts fo this type and the price of each type text
    text1 = Text('short', 75, 125)
    assert text1.kind == 'short'
    assert text1.number == 75
    assert text1.price == 125

    text2 = Text('long', 25, 245)
    assert text2.kind == 'long'

    # Text machines can contain different number of texts.
    tm1 = TextMachine(text1, text2)
    # assert tm1.texts == [text1, text2], tm1.texts
    assert str(tm1.texts) == '[<75 short texts, ₴1.25 each>, <25 long texts, ₴2.45 each>]', str(tm1.texts)
    assert str(tm1) == "Text Machine: 75 short texts, ₴1.25 each; 25 long texts, ₴2.45 each", str(tm1)
    assert tm1.texts_count() == (75, 25)
    #To show current status we need two extra
    #atributes: current_order and current_charge
    assert tm1.current_order is None
    assert tm1.current_charge == 0
    assert tm1.current_price is None

    # When the user inserts money and text type, the machine returns
    # a message about their status and any change they need as a tuple.
    assert tm1.insert_money(20, 'short') == "For a short text, you are still owe ₴1.05"
    assert tm1.current_order == 'short'
    assert tm1.current_price == 125
    assert tm1.current_charge == 20
    assert tm1.texts_count() == (75, 25)
    assert tm1.insert_money(5, 'short') == "For a short text, you are still owe ₴1.00"
    assert tm1.current_charge == 25

    # When the user has paid enough money, they get a text and
    # the money owed resets.
    assert tm1.insert_money(100, 'short') == "Got a text!"
    assert tm1.texts_count() == (74, 25)
    assert tm1.current_order is None
    assert tm1.current_charge == 0
    assert str(tm1) == "Text Machine: 74 short texts, ₴1.25 each; 25 long texts, ₴2.45 each"

    # If the user pays too much money, they get their change back
    # with the text.
    assert tm1.insert_money(500, 'long') == "Got a text! You can buy: 2 short texts or 1 long text."
    assert tm1.current_charge == 255
    assert tm1.texts_count() == (74, 24)
    assert tm1.current_order is None
    assert tm1.current_price is None
    assert str(tm1) == "Text Machine: 74 short texts, ₴1.25 each; 24 long texts, ₴2.45 each"

    # Machines can be placed in different places
    tm1.add_texts(Text('middle', 50, 185))
    assert str(tm1) == "Text Machine: 74 short texts, ₴1.25 each; 24 long texts, ₴2.45 each; 50 middle texts, ₴1.85 each"

    # Machines can become empty
    tm2 = TextMachine(Text('short', 1, 125), Text('long', 1, 245))
    assert str(tm2) == 'Text Machine: 1 short text, ₴1.25 each; 1 long text, ₴2.45 each'
    assert tm2.texts_count() == (1, 1)
    assert tm2.insert_money(125, "short") == "Got a text!"
    assert tm2.texts_count() == (0, 1)
    assert tm2.insert_money(125, "short") == "Such kind of the text is finished."
    assert tm2.texts_count() == (0, 1)
    assert tm2.insert_money(120, "long") == "Got a text!"
    assert tm2.texts_count() == (0, 0)
    assert str(tm2) == "Text Machine: 0 texts."

    # Once a machine is empty, 
    # it should not accept money until it is restocked.
    assert tm2.insert_money(25, "short") == "Such kind of the text is finished."
    assert tm2.current_charge == 25
    tm2.add_texts(Text('short', 20, 125))
    tm2.add_texts(Text('long', 20, 245))
    assert tm2.texts_count() == (20, 20)
    assert str(tm2) == 'Text Machine: 20 short texts, ₴1.25 each; 20 long texts, ₴2.45 each'
    assert tm2.insert_money(25, "short") == "For a short text, you are still owe ₴0.75"

    # We should be able to test machines for basic functionality
    tm3 = TextMachine(Text('short', 25, 100), Text('long', 25, 200))
    tm4 = TextMachine(Text('short', 25, 100), Text('long', 25, 200))
    tm5 = TextMachine(Text('long', 25, 200), Text('short', 25, 100))
    tm6 = TextMachine(Text('short', 25, 120), Text('long', 25, 245))
    tm7 = "Text Machine"
    assert isinstance(tm3, TextMachine)
    assert tm3 == tm4
    assert tm3 == tm5
    assert tm3 != tm6
    assert tm3 != tm7  # should not crash!
    tm_set = set()
    assert tm3 not in tm_set
    tm_set.add(tm4)
    assert tm3 in tm_set
    tm_set.remove(tm4)
    assert tm3 not in tm_set
    assert tm4.insert_money(50, "short") == "For a short text, you are still owe ₴0.50"
    assert tm3 != tm4

    print("Done!")


if __name__ == "__main__":
    test_TextMachineClass()
