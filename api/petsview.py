from connexion import NoContent
from aiohttp.web import View


class PetsView(View):
    method_decorators = []
    pets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get(self):
        return NoContent, 404
