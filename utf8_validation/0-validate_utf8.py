#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determine if a data set represents valid UTF-8 encoding."""

    bytes_remaining = 0
    next_min = 0x80
    next_max = 0xBF

    for num in data:
        byte = num & 0xFF

        if bytes_remaining == 0:
            if byte <= 0x7F:
                continue
            elif 0xC2 <= byte <= 0xDF:
                bytes_remaining = 1
            elif byte == 0xE0:
                bytes_remaining = 2
                next_min = 0xA0
            elif 0xE1 <= byte <= 0xEC or 0xEE <= byte <= 0xEF:
                bytes_remaining = 2
            elif byte == 0xED:
                bytes_remaining = 2
                next_max = 0x9F
            elif byte == 0xF0:
                bytes_remaining = 3
                next_min = 0x90
            elif 0xF1 <= byte <= 0xF3:
                bytes_remaining = 3
            elif byte == 0xF4:
                bytes_remaining = 3
                next_max = 0x8F
            else:
                return False
        else:
            if not next_min <= byte <= next_max:
                return False

            bytes_remaining -= 1
            next_min = 0x80
            next_max = 0xBF

    return bytes_remaining == 0


if __name__ == "__main__":
    pass
