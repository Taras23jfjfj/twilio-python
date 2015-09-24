import os


def get_cert_file():
    """ Get the cert file location or bail """
    # XXX - this currently fails test coverage because we don't actually go
    # over the network anywhere. Might be good to have a test that stands up a
    # local server and authenticates against it.
    try:
        # Apparently __file__ is not available in all places so wrapping this
        # in a try/catch
        current_path = os.path.realpath(__file__)
        ca_cert_path = os.path.join(current_path, '..', '..', 'conf', 'cacert.pem')
        return os.path.abspath(ca_cert_path)
    except Exception:
        # None means use the default system file
        return None

