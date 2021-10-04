from datetime import datetime
from enum import Enum
from typing import List, Optional

from .channel import Channel
from .member import Member
from .message import Emoji, Sticker
from .misc import DictSerializerMixin
from .presence import PresenceUpdate
from .role import Role
from .user import User
from .voice import VoiceState


class GuildFeature(str, Enum):
    """
    An enumerable string-formatted class representing all of the features a guild can have.

    .. note:
        Equivalent of `Guild Features <https://discord.com/developers/docs/resources/guild#guild-object-guild-features>`_ in the Discord API.
    """

    __slots__ = (
        "ANIMATED_ICON",
        "BANNER",
        "COMMERCE",
        "COMMUNITY",
        "DISCOVERABLE",
        "FEATURABLE",
        "INVITE_SPLASH",
        "MEMBER_VERIFICATION_GATE_ENABLED",
        "NEWS",
        "PARTNERED",
        "PREVIEW_ENABLED",
        "VANITY_URL",
        "VERIFIED",
        "VIP_REGIONS",
        "WELCOME_SCREEN_ENABLED",
        "TICKETED_EVENTS_ENABLED",
        "MONETIZATION_ENABLED",
        "MORE_STICKERS",
        "THREE_DAY_THREAD_ARCHIVE",
        "SEVEN_DAY_THREAD_ARCHIVE",
        "PRIVATE_THREADS",
    )
    ANIMATED_ICON = "ANIMATED_ICON"
    BANNER = "BANNER"
    COMMERCE = "COMMERCE"
    COMMUNITY = "COMMUNITY"
    DISCOVERABLE = "DISCOVERABLE"
    FEATURABLE = "FEATURABLE"
    INVITE_SPLASH = "INVITE_SPLASH"
    MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
    NEWS = "NEWS"
    PARTNERED = "PARTNERED"
    PREVIEW_ENABLED = "PREVIEW_ENABLED"
    VANITY_URL = "VANITY_URL"
    VERIFIED = "VERIFIED"
    VIP_REGIONS = "VIP_REGIONS"
    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"
    TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
    MONETIZATION_ENABLED = "MONETIZATION_ENABLED"
    MORE_STICKERS = "MORE_STICKERS"
    THREE_DAY_THREAD_ARCHIVE = "THREE_DAY_THREAD_ARCHIVE"
    SEVEN_DAY_THREAD_ARCHIVE = "SEVEN_DAY_THREAD_ARCHIVE"
    PRIVATE_THREADS = "PRIVATE_THREADS"


class WelcomeChannels(DictSerializerMixin):
    """
    A class object representing a welcome channel on the welcome screen.

    .. note::
        ``emoji_id`` and ``emoji_name`` are given values respectively if the welcome channel
        uses an emoji.

    :ivar int channel_id: The ID of the welcome channel.
    :ivar str description: The description of the welcome channel.
    :ivar typing.Optional[int] emoji_id: The ID of the emoji of the welcome channel.
    :ivar typing.Optional[str] emoji_name: The name of the emoji of the welcome channel.
    """

    __slots__ = ("_json", "channel_id", "description", "emoji_id", "emoji_name")
    _json: dict
    channel_id: int
    description: str
    emoji_id: Optional[int]
    emoji_name: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WelcomeScreen(DictSerializerMixin):
    """
    A class object representing the welcome screen shown for community guilds.

    .. note::
        ``description`` is ambiguous -- Discord poorly documented this. :)

        We assume it's for the welcome screen topic.

    :ivar typing.Optional[str] description: The description of the welcome sceen.
    :ivar typing.List[interactions.api.models.guild.WelcomeChannels] welcome_channels: A list of welcome channels of the welcome screen.
    """

    __slots__ = ("_json", "description", "welcome_channels")
    _json: dict
    description: Optional[str]
    welcome_channels: List[WelcomeChannels]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class StageInstance(DictSerializerMixin):
    """
    A class object representing an instace of a stage channel in a guild.

    :ivar int id: The ID of the stage.
    :ivar int guild_id: The guild ID the stage is in.
    :ivar int channel_id: The channel ID the stage is instantiated from.
    :ivar str topic: The topic of the stage.
    :ivar int privacy_level: The "privacy"/inclusive accessibility level of the stage.
    :ivar bool discoverable_disabled: Whether the stage can be seen from the stage discovery.
    """

    __slots__ = (
        "_json",
        "id",
        "guild_id",
        "channel_id",
        "topic",
        "privacy_level",
        "discoverable_disabled",
    )
    _json: dict
    id: int
    guild_id: int
    channel_id: int
    topic: str
    privacy_level: int  # can be Enum'd
    discoverable_disabled: bool

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Guild(DictSerializerMixin):
    """
    A class object representing how a guild is registered.

    .. note::
        Most of these optionals are actually declared with their value
        upon instantiation but are kept like this since this class object
        is meant to be more broad and generalized.

    :ivar int id: The ID of the guild.
    :ivar str name: The name of the guild.
    :ivar typing.Optional[str] icon: The icon of the guild.
    :ivar typing.Optional[str] icon_hash: The hashed version of the icon of the guild.
    :ivar typing.Optional[str] splash: The invite splash banner of the guild.
    :ivar typing.Optional[str] discovery_splash: The discovery splash banner of the guild.
    :ivar typing.Optional[bool] owner: Whether the guild is owned.
    :ivar int owner_id: The ID of the owner of the guild.
    :ivar typing.Optional[str] permissions: The permissions of the guild.
    :ivar typing.Optional[str] region: The geographical region of the guild.
    :ivar typing.Optional[int] afk_channel_id: The AFK voice channel of the guild.
    :ivar int afk_timeout: The timeout of the AFK voice channel of the guild.
    :ivar typing.Optional[bool] widget_enabled: Whether widgets are enabled in the guild.
    :ivar typing.Optional[int] widget_channel_id: The channel ID of the widget in the guild.
    :ivar int verification_level: The level of user verification of the guild.
    :ivar int default_message_notifications: The default message notifications setting of the guild.
    :ivar int explicit_content_filter: The explicit content filter setting level of the guild.
    :ivar typing.List[interactions.api.models.role.Role] roles: The list of roles in the guild.
    :ivar typing.List[interactions.api.models.message.Emoji] emojis: The list of emojis from the guild.
    :ivar typing.List[interactions.api.models.guild.GuildFeature] features: The list of features of the guild.
    :ivar int mfa_level: The MFA level of the guild.
    :ivar typing.Optional[int] application_id: The application ID of the guild.
    :ivar typing.Optional[int] system_channel_id: The channel ID of the system of the guild.
    :ivar typing.Optional[int] rules_channel_id: The channel ID of Discord's defined "rules" channel of the guild.
    :ivar typing.Optional[datetime.datetime] joined_at: The timestamp the member joined the guild.
    :ivar typing.Optional[bool] large: Whether the guild is considered "large."
    :ivar typing.Optional[bool] unavailable: Whether the guild is unavailable to access.
    :ivar typing.Optional[int] member_count: The amount of members in the guild.
    :ivar typing.Optional[typing.List[interactions.api.models.presence.PresenceUpdate]] presences: The list of presences in the guild.
    :ivar typing.Optional[int] max_presences: The maximum amount of presences allowed in the guild.
    :ivar typing.Optional[int] max_members: The maximum amount of members allowed in the guild.
    :ivar typing.Optional[str] vanity_url_code: The vanity URL of the guild.
    :ivar typing.Optional[str] description: The description of the guild.
    :ivar typing.Optional[str] banner: The banner of the guild.
    :ivar int premium_tier: The server boost level of the guild.
    :ivar typing.Optional[int] premium_subscription_count: The amount of server boosters in the guild.
    :ivar str preferred_locale: The "preferred" local region of the guild.
    :ivar typing.Optional[int] public_updates_channel_id: The channel ID for community updates of the guild.
    :ivar typing.Optional[int] max_video_channel_users: The maximum amount of video streaming members in a channel allowed in a guild.
    :ivar typing.Optional[int] approximate_member_count: The approximate amount of members in the guild.
    :ivar typing.Optional[int] approximate_presence_count: The approximate amount of presences in the guild.
    :ivar typing.Optional[interactions.api.models.guild.WelcomeScreen] welcome_screen: The welcome screen of the guild.
    :ivar int nsfw_level: The NSFW safety filter level of the guild.
    :ivar typing.Optional[interactions.api.models.guild.StageInstance] stage_instances: The stage instance of the guild.
    :ivar typing.Optional[typing.List[interactions.api.models.message.Sticker]] stickers: The list of stickers from the guild.
    """

    _json: dict
    id: int
    name: str
    icon: Optional[str]
    icon_hash: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: Optional[bool]
    owner_id: int
    permissions: Optional[str]
    region: Optional[str]  # None, we don't do Voices.
    afk_channel_id: Optional[int]
    afk_timeout: int
    widget_enabled: Optional[bool]
    widget_channel_id: Optional[int]
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: List[Role]
    emojis: List[Emoji]
    features: List[GuildFeature]
    mfa_level: int
    application_id: Optional[int]
    system_channel_id: Optional[int]
    system_channel_flags: int
    rules_channel_id: Optional[int]
    joined_at: Optional[datetime]
    large: Optional[bool]
    unavailable: Optional[bool]
    member_count: Optional[int]
    voice_states: Optional[List[VoiceState]]
    members: Optional[List[Member]]
    channels: Optional[List[Channel]]
    threads: Optional[List[Channel]]  # threads, because of their metadata
    presences: Optional[List[PresenceUpdate]]
    max_presences: Optional[int]
    max_members: Optional[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: int
    premium_subscription_count: Optional[int]
    preferred_locale: str
    public_updates_channel_id: Optional[int]
    max_video_channel_users: Optional[int]
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
    welcome_screen: Optional[WelcomeScreen]
    nsfw_level: int
    stage_instances: Optional[StageInstance]
    stickers: Optional[List[Sticker]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GuildPreview(DictSerializerMixin):
    """
    A model representing the preview of a guild.

    ..note::
        This refers to the documentation `here <https://discord.com/developers/docs/resources/guild>_`

    :ivar int id: The ID of the guild.
    :ivar str name: The name of the guild.
    :ivar typing.Optional[str] icon: The icon of the guild.
    :ivar typing.Optional[str] splash: The invite splash banner of the guild.
    :ivar typing.Optional[str] discovery_splash: The discovery splash banner of the guild.
    :ivar typing.List[interactions.api.models.message.Emoji] emojis: The list of emojis from the guild.
    :ivar typing.List[interactions.api.models.guild.GuildFeature] features: The list of features of the guild.
    :ivar int approximate_member_count: The approximate amount of members in the guild.
    :ivar int approximate_presence_count: The approximate amount of presences in the guild.
    :ivar typing.Optional[str] description: The description of the guild.

    """

    _json: dict
    id: int
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    emoji: List[Emoji]
    features: List[GuildFeature]
    approximate_member_count: int
    approximate_presence_count: int
    description: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Invite(DictSerializerMixin):
    """The invite object."""

    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GuildTemplate(DictSerializerMixin):
    """An object representing the snapshot of an existing guild."""

    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: int
    creator: User
    created_at: datetime
    updated_at: datetime
    source_guild_id: int
    serialized_source_guild: Guild  # partial
    is_dirty: Optional[bool]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)