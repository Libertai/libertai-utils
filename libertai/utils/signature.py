from datetime import date

from libertai.interfaces.subscription import SubscriptionProvider, SubscriptionType


def get_subscribe_message(subscription_type: SubscriptionType, provider: SubscriptionProvider) -> str:
    return f"I confirm that I want to subscribe to LibertAI's {subscription_type.value} plan, using the '{provider.value}' provider, on this day ({date.today()})."


def get_unsubscribe_message(subscription_type: SubscriptionType, provider: SubscriptionProvider) -> str:
    return f"I confirm that I want to stop my subscription to LibertAI's {subscription_type.value} plan, using the '{provider.value}', on the day ({date.today()})."


def get_token_message() -> str:
    return f"I confirm that I want to create a token access to LibertAI, on the day ({date.today()})"
