import json

from attrdict import AttrDict


def myjsonload(filename):
    """Load contents of "filename", which should be in /tmp/ and
    return the equivalent Python object.
    """
    f = open(f"/tmp/{filename}")
    contents = f.read()

    # check if JSON was copied from Chrome
    if contents[0] in ("'", '"'):
        contents = contents[1:-1]
    f.close()
    return AttrDict(json.loads(contents))
