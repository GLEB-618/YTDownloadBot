from contextlib import asynccontextmanager
import re, tempfile, shutil


def is_url(text: str) -> bool:
    return bool(re.match(r'https?://\S+', text.strip()))

@asynccontextmanager
async def async_tempdir():
    tmpdir = tempfile.mkdtemp()
    try:
        yield tmpdir
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)