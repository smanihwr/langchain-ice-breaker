from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
Boyan Slat (born 27 July 1994)[2][3] is a Dutch inventor and entrepreneur.[4] A former aerospace engineering student,[5][6] he is the CEO of The Ocean Cleanup.[7]

Initial interest in plastic pollution
In 2011, Slat went diving and found that the amount of plastic surpassed the number of fish in the area he explored. He made ocean plastic pollution the subject of a high school project examining why it was considered impossible to clean up. He later came up with the idea of building a passive plastic catchment system, using circulating ocean currents to net plastic waste, which he presented at a TEDx talk in Delft in 2012.[8][9]

Slat discontinued his aerospace engineering studies at TU Delft to devote his time to developing his idea. He founded The Ocean Cleanup in 2013, and shortly after, his TEDx talk went viral after being shared on several news sites.[8]

"Technology is the most potent agent of change. It is an amplifier of our human capabilities", Slat wrote in The Economist. "Whereas other change-agents rely on reshuffling the existing building blocks of society, technological innovation creates entirely new ones, expanding our problem-solving toolbox."[10]
"""

if __name__ == "__main__":
    print("Hello Langchain!!")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
