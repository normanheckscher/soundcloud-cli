from .client import get_client


def group(user_id):
    client = get_client()

    page_size = 100
    offset    = 0

    return client.get('/users/{0}/groups'.format(user_id), order='created_at',
                                                           limit=page_size,
                                                           offset=offset)
