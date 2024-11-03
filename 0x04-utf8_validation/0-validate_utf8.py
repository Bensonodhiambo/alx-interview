def validUTF8(data):
    num_continuation_bytes = 0

    for byte in data:
        # Get the least significant 8 bits
        byte = byte & 0xFF

        if num_continuation_bytes == 0:
            # Determine number of bytes in character based on the first byte
            if (byte >> 5) == 0b110:
                num_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_continuation_bytes = 3
            elif (byte >> 7):
                # If the byte starts with `10`, it's invalid at the beginning of a character
                return False
        else:
            # Check continuation byte format `10xxxxxx`
            if (byte >> 6) != 0b10:
                return False
            num_continuation_bytes -= 1

    return num_continuation_bytes == 0
