from typing import Iterator, Tuple, Any
from yarl import URL

from pyapp.conf.loaders import Loader, register


@register
class S3Loader(Loader):
    """
    Load S3
    """
    scheme = "s3"

    @classmethod
    def from_url(cls, url: URL) -> "Loader":
        pass

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        pass
