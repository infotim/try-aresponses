import aiohttp.web
import pytest

from .service import Service

pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")

@pytest.mark.asyncio
async def test_real_response():
    s = Service()
    r = await s.fetch()
    assert r != "127.0.0.1"

@pytest.mark.asyncio
async def test_mock_response(aresponses):
    aresponses.add(
        "httpbin.org",
        "/get",
        "GET",
        response=aiohttp.web.json_response({"origin":"127.0.0.1"}) # ! SIC !
        )
    s = Service()
    r = await s.fetch()
    assert r == "127.0.0.1"
