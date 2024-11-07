from enum import Enum

class Error(str, Enum):
    QRCODE_CREATION_INVALID = "qrcode.creation_invalid"
    QRCODE_READ_INVALID = "qrcode.read_invalid"
    QRCODE_CREATION_FAILED = "qrcode.creation_failed"
    QRCODE_READ_FAILED = "qrcode.read_failed"
    QRCODE_SUBMISSION_FAILED = "qrcode.submission_failed"
    INVALID_URL = "url.invalid"