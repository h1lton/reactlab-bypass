import dataclasses

import pytest
import requests

from main import ReactLabBypass


@dataclasses.dataclass
class SiteData:
    url: str
    cookie_name: str


sites_data = [
    SiteData("https://radmir.online", "R3ACTLBPROTECT="),
    SiteData("https://arizona-rp.com", "R3ACTLAB-ARZ="),
]


@pytest.mark.parametrize("site_data", sites_data)
def test_get_cookie(site_data: SiteData):
    rlb = ReactLabBypass(site_data.url)
    cookie = rlb.get_cookie()
    assert cookie.startswith(site_data.cookie_name)
    assert cookie == rlb.cookie
    assert cookie == rlb.get_cookie()


@pytest.mark.parametrize("site_data", sites_data)
def test_valid_cookie(site_data):
    rlb = ReactLabBypass(site_data.url)
    response = requests.get(site_data.url, headers={"cookie": rlb.get_cookie()})
    assert "Please turn JavaScript on and reload the page." not in response.text


@pytest.mark.parametrize("site_data", sites_data)
def test_checking_cookie(site_data):
    rlb = ReactLabBypass(site_data.url)
    assert rlb.cookie_expires_at == 0
    assert rlb.is_cookie_expired
    assert not rlb.is_cookie_valid

    rlb.get_cookie()
    assert rlb.cookie_expires_at != 0
    assert not rlb.is_cookie_expired
    assert rlb.is_cookie_valid
