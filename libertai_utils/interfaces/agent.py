from pydantic import BaseModel

from libertai_utils.interfaces.subscription import SubscriptionAccount


class DeleteAgentBody(BaseModel):
    subscription_id: str
    password: str


class SetupAgentBody(DeleteAgentBody):
    account: SubscriptionAccount
