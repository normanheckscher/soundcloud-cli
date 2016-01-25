from .. import settings
from .client import get_client


def groupshare(group_id=None, track_id=None):

    client = get_client()

    # contribute track to group
    return client.post('/groups/%d/contributions' % group_id, track={'id': track_id})
