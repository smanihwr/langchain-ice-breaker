from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def crawl() -> str:
    pass


def lookup(name: str) -> str:
    print("entering linkedin lookup")

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """given the full name {name_of_person}, I want you to get me a link to their LinkedIn profile page.
                  your answer should container only a LinkedIn URL"""

    crawl_google_tool = Tool(
        name="Crawl Google 4 linkedin profile page",
        func=get_profile_url,
        description="useful when you need to get the LinkedIn page URL",
    )

    tools_for_agent = [crawl_google_tool]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    print("linkedin_profile_url found ", linkedin_profile_url)
    return linkedin_profile_url
