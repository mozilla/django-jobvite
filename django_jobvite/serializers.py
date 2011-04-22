try:
    import json
except ImportError:
    import simplejson as json


def serialize(results):
    """Serialize a ``QueryDict`` into json."""
    serialized = {}
    for result in results:
        serialized.update(result.to_dict())
    return json.dumps(serialized, indent=4)
