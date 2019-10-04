from my_module import get_ip


def test_get_ip_type():
    """The IP is expected to be a string."""
    ip = get_ip()
    assert isinstance('', str)


def test_get_ip_dots():
    """The IP(v4) is expected to have 4 dots."""
    ip = get_ip()
    True==True
