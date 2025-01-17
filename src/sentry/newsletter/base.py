from __future__ import annotations

from typing import Any, Sequence

from sentry.models.user import User
from sentry.utils.services import Service


class Newsletter(Service):
    __all__ = (
        "is_enabled",
        "get_default_list_id",
        "get_default_list_ids",
        "get_subscriptions",
        "update_subscription",
        "update_subscriptions",
        "create_or_update_subscription",
        "create_or_update_subscriptions",
        "optout_email",
    )

    DEFAULT_LISTS = (1,)
    DEFAULT_LIST_ID = DEFAULT_LISTS[0]

    enabled = False

    def is_enabled(self) -> bool:
        return self.enabled

    def optout_email(self, email, **kwargs):
        raise NotImplementedError

    """
    Replacements for the functions below that only accept a single list_id argument
    """

    def get_default_list_ids(self) -> tuple[int, ...]:
        return self.DEFAULT_LISTS

    def get_subscriptions(self, user):
        return None

    def update_subscriptions(
        self,
        user: User,
        *,
        list_ids: Sequence[int] | None = None,
        subscribed: bool = True,
        create: bool | None = None,
        verified=None,
        subscribed_date=None,
        unsubscribed_date=None,
        **kwargs,
    ):
        return None

    def create_or_update_subscriptions(
        self,
        user: User,
        *,
        list_ids: Sequence[int] | None = None,
        subscribed: bool = True,
        verified=None,
        subscribed_date=None,
        unsubscribed_date=None,
        **kwargs: Any,
    ):
        return self.update_subscriptions(
            user=user,
            list_ids=list_ids,
            subscribed=subscribed,
            verified=verified,
            subscribed_date=subscribed_date,
            unsubscribed_date=unsubscribed_date,
            create=True,
            **kwargs,
        )

    """
    These methods are deprecated in favor of the corresponding functions that
    accept multiple list IDs
    """

    def get_default_list_id(self) -> int:
        return self.DEFAULT_LIST_ID

    def update_subscription(
        self,
        user: User,
        *,
        list_id: int | None = None,
        subscribed: bool = True,
        create: bool | None = None,
        verified=None,
        subscribed_date=None,
        unsubscribed_date=None,
        **kwargs: Any,
    ):
        return None

    def create_or_update_subscription(
        self,
        user: User,
        *,
        list_id: int | None = None,
        subscribed: bool = True,
        verified=None,
        subscribed_date=None,
        unsubscribed_date=None,
        **kwargs: Any,
    ):
        return self.update_subscription(
            user=user,
            list_id=list_id,
            subscribed=subscribed,
            verified=verified,
            subscribed_date=subscribed_date,
            unsubscribed_date=unsubscribed_date,
            create=True,
            **kwargs,
        )
