from enum import Enum

from pydantic import BaseModel

from libertai_utils.interfaces.subscription import SubscriptionAccount


class AgentPythonPackageManager(str, Enum):
    poetry = "poetry"
    requirements = "requirements"
    pyproject = "pyproject"


class AgentUsageType(str, Enum):
    fastapi = "fastapi"
    python = "python"


class BaseDeleteAgentBody(BaseModel):
    subscription_id: str
    password: str


class BaseSetupAgentBody(BaseDeleteAgentBody):
    account: SubscriptionAccount


class UpdateAgentResponse(BaseModel):
    instance_ip: str
    error_log: str


class AddSSHKeyAgentBody(BaseModel):
    secret: str
    ssh_key: str


class AddSSHKeyAgentResponse(BaseModel):
    error_log: str
