import re

# 정규 표현식 패턴
#raw string notation
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# 이메일 주소 샘플 리스트
email_samples = [
    "user@example.com",
    "first.last@example.co.jp",
    "john.doe123@sub.domain.co.uk",
    "invalid-email",
    "not_an_email@",
    "@missing_username.com",
    "user@.com",
    "user@sub@domain.com",
    "user@domain",
    "user@123.45",
]

# 각 샘플에 대해 이메일 주소 체크
for email in email_samples:
    match = re.search(email_pattern, email)
    if match:
        print(f"'{email}'은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"'{email}'은(는) 유효하지 않은 이메일 주소입니다.")