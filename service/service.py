import aiohttp

class Service:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def fetch(self) -> str:
        resp = await self.session.get("https://httpbin.org/get")
        async with resp:
            data = await resp.json()
            return data["origin"]
