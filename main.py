import dataclasses
import re
import time
import requests

from datetime import timedelta
from Crypto.Cipher import AES


class ReactLabBypassException(Exception):
    pass


@dataclasses.dataclass
class ReactLabBypass:
    """
    Обход защиты React Lab

    :param site Сайт на котором защита
    :param cookie_expires_at конечный срок действия cookie
    :param cookie cookie в формате "cookie_name=cookie_value"
    """
    site: str
    cookie_expires_at: float = 0
    cookie: str | None = None

    @property
    def is_cookie_expired(self) -> bool:
        """Проверка закончился ли срок действия cookie."""
        return self.cookie_expires_at - time.time() < 0

    @property
    def is_cookie_valid(self) -> bool:
        """Проверка валидности cookie"""
        return self.cookie and not self.is_cookie_expired

    def _get_cookie(self, html) -> str:
        """
        Расшифровывает данные на странице сохраняя и возвращая cookie
        в формате 'cookie_name=cookie_value'
        """
        line = html.splitlines()[-8]
        line = re.sub(
            r"\\x([A-F0-9]{2})",
            lambda m: chr(int(m.group(1), 16)),
            line
        )

        keys = re.findall(r"[a-f0-9]{32}", line)

        if not keys:
            raise ReactLabBypassException("cannot get keys")

        cookie_name = re.search(
            r'","cookie","(?P<name>[^"]+)',
            line
        ).group("name")

        key = bytes.fromhex(keys[0])
        iv = bytes.fromhex(keys[1])
        cipher = bytes.fromhex(keys[2])

        cookie_value = bytes.hex(AES.new(key, AES.MODE_CBC, iv=iv).decrypt(cipher))

        self.cookie = cookie_name + cookie_value
        self.cookie_expires_at = time.time() + timedelta(days=399).total_seconds()
        return self.cookie

    def get_cookie(self) -> str:
        """
        Возвращает cookie в формате 'cookie_name=cookie_value'
        Если cookie были получены ранее проверяет их на валидность,
        если валидны, то возвращает их, если нет, то запрашивает новые
        """
        if self.is_cookie_valid:
            return self.cookie

        response = requests.get(self.site)
        return self._get_cookie(response.text)
