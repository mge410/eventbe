import datetime

import django.contrib.auth.models
import django.contrib.auth.tokens
import django.utils.crypto
import django.utils.http


class TokenGeneratorWithTimestamp(
    django.contrib.auth.tokens.PasswordResetTokenGenerator
):
    def __init__(self, timestamp: int) -> None:
        self.timestamp = timestamp
        super().__init__()

    def check_token(
        self, user: django.contrib.auth.models.AbstractBaseUser, token: str
    ) -> bool:
        if not (user and token):
            return False

        try:
            ts_b36, _ = token.split('-')
            legacy_token = len(ts_b36) < 4
        except ValueError:
            return False

        try:
            ts = django.utils.http.base36_to_int(ts_b36)
        except ValueError:
            return False

        if not django.utils.crypto.constant_time_compare(
            self._make_token_with_timestamp(user, ts), token
        ):
            if not django.utils.crypto.constant_time_compare(
                self._make_token_with_timestamp(user, ts, legacy=True),
                token,
            ):
                return False

        now = self._now()
        if legacy_token:
            ts *= 24 * 60 * 60
            ts += int(
                (
                    now - datetime.combine(now.date(), datetime.time.min)
                ).total_seconds()
            )
        if (self._num_seconds(now) - ts) > self.timestamp:
            return False

        return True


token_7_days = TokenGeneratorWithTimestamp(604800)
