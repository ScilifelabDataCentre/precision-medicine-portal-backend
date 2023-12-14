
def payload_is_valid(payload, expected_arguments) -> bool:
    for arg in expected_arguments:
        if arg not in payload:
            return False
    return True