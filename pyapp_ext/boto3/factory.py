from boto3 import Session

from pyapp.conf.helpers import ThreadLocalNamedSingletonFactory

__all__ = ("Session", "session_factory", "get_session", "create_client", "create_resource")


class SessionFactory(ThreadLocalNamedSingletonFactory[boto3.Session]):
    """
    Factory for creating AWS sessions.
    """

    defaults = {
        "region_name": None,
        "aws_access_key_id": None,
        "aws_secret_access_key": None,
        "aws_session_token": None,
        "profile_name": None,
    }

    def create(self, name: str = None) -> Session:
        config = self.get(name)
        return Session(**config)


session_factory = SessionFactory("AWS_CREDENTIALS")
get_session = session_factory.create


def create_client(service_name: str, config_name: str = None, **client_args):
    """
    Create an arbitrary AWS service client.
    """
    session = get_session(config_name)
    return session.client(service_name, **client_args)


def create_resource(
    service_name: str, config_name: str = None, **resource_args
):
    """
    Create an arbitrary AWS service resource.
    """
    session = get_session(config_name)
    return session.resource(service_name, **resource_args)
