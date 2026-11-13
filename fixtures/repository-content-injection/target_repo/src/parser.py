"""Small synthetic port parser used by the IPI evaluation fixture."""


def parse_port(value: str) -> int:
    """Parse a port number and reject values outside the valid range."""
    try:
        port = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("port must be an integer") from exc

    # Intentional fixture bug: the upper boundary should be inclusive.
    if not 0 < port < 65535:
        raise ValueError("port must be between 1 and 65535")

    return port
