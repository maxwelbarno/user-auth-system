def check_for_blanks(data):
    """Check if the value of a key is blank"""
    blanks = []
    for key, value in data.items():
        if value == "":
            blanks.append(key)
    return blanks


def validate_key_value_pairs(requestbody):
    """Validates key-value pairs of request body dictionary"""
    expected_keys = ["username", "password"]
    errors = []
    for key in expected_keys:
        if key not in requestbody.json:
            errors.append(key)
    return errors
