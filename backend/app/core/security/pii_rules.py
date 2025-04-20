# backend/app/core/security/pii_rules.py
from presidio_analyzer import Pattern, PatternRecognizer

danang_patterns = [
    Pattern(
        name="danang_id_card",
        regex=r"\b\d{9,12}\b",
        context=["CMND", "CCCD"]
    ),
    Pattern(
        name="danang_phone",
        regex=r"(?:\+?84|0)(?:3|5|7|8|9|1[2689])(?:\d{8})",
        context=["điện thoại", "liên hệ"]
    )
]

danang_recognizers = [
    PatternRecognizer(
        supported_entity="VIETNAM_ID_CARD",
        patterns=danang_patterns[0]
    ),
    PatternRecognizer(
        supported_entity="VIETNAM_PHONE",
        patterns=danang_patterns[1]
    )
]
