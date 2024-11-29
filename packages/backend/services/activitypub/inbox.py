import aiohttp
from apsig import draftVerifier

from ...broker import broker

@broker.task
async def process_stream(data: dict):
    
    pass