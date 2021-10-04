from collections import OrderedDict
from datetime import datetime
from typing import List, Optional

from orjson import dumps

from .message import Emoji
from .misc import ClientStatus, DictSerializerMixin
from .user import User


class _PresenceParty(DictSerializerMixin):
    _json: dict
    id: Optional[str]
    size: Optional[List[int]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class _PresenceAssets(DictSerializerMixin):
    _json: dict
    large_image: Optional[str]
    large_text: Optional[str]
    small_image: Optional[str]
    small_text: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class _PresenceSecrets(DictSerializerMixin):
    _json: dict
    join: Optional[str]
    spectate: Optional[str]
    match: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class _PresenceButtons(DictSerializerMixin):
    _json: dict
    label: str
    url: str

    def __new__(cls, **kwargs) -> bytes:
        comb = OrderedDict()

        for kwarg in kwargs:
            comb.update({kwarg: kwargs[kwarg]})

        return dumps(comb)


class PresenceActivity(DictSerializerMixin):
    _json: dict
    name: str
    type: int
    url: Optional[str]
    created_at: int
    timestamps: Optional[datetime]
    application_id: Optional[int]
    details: Optional[str]
    state: Optional[str]
    emoji: Optional[Emoji]
    party: Optional[_PresenceParty]
    assets: Optional[_PresenceAssets]
    secrets: Optional[_PresenceSecrets]
    instance: Optional[bool]
    flags: Optional[int]
    buttons: Optional[_PresenceButtons]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PresenceUpdate(DictSerializerMixin):
    _json: dict
    user: User
    guild_id: int
    status: str
    activities: List[PresenceActivity]
    client_status: ClientStatus

    def __init__(self, **kwargs):
        super().__init__(**kwargs)