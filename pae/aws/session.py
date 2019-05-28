import botocore


class SessionFactory(ThreadLocalNamedSingletonFactory):
    """
    Factory for creating AWS sessions.
    """
    defaults = {
        "region_name": None,
        "aws_access_key_id": None,
        "aws_secret_access_key": None,
        "aws_session_token": None,
    }

    def create_instance(self, name=None):
        config = self.get(name)
        session = botocore.get_session()

        if config['region_name']:
            session.set_config_variable('region', config['region_name'])

        if config["aws_access_key_id"] or config["aws_secret_access_key"] or config["aws_session_token"]:
            session.set_credentials(
                config["aws_access_key_id"], config["aws_secret_access_key"], config["aws_session_token"])

        return session


session_factory = SessionFactory('AWS')
