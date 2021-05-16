from backend.utils.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number = 157
    hex_number = hex(original_number)[2:]

    binary_string = hex_to_binary(hex_number)

    assert int(binary_string, 2) == original_number
