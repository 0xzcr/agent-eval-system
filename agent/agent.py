from langchain.agents import create_agent

from agent.models import model
from agent.objects import Answer
from agent.prompts import agent_system_prompt
from agent.tools import (
    calculate_right_refund,
    get_today_date,
    get_user_purchase_history,
    issue_refund_ticket,
)

agent = create_agent(
    model=model,
    tools=[
        get_user_purchase_history,
        calculate_right_refund,
        issue_refund_ticket,
        get_today_date,
    ],
    system_prompt=agent_system_prompt,
    response_format=Answer,
)
