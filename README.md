
# We do NOT and WILL not have any Crypto Projects, they are a complete SCAM


## This project is not releated with any crypto currencies.



<br>
<br>
<br>
<br>
<br>
<br>






<div align= "center">
    <h1><img src="assets/image.svg " height="28px" /> Tiger: Neuralink for your AI Agents</h1>
</div>

<p align="center">
  <a href="#setup">Setup</a> •
</p>

<p align="center">
<b>Integrations:</b>
  <a href="#crewai-integration">crewAI Integration</a> •
  <a href="#langchain-integration">LangChain Integration</a> •
  <a href="#autogen-integration">AutoGen Integration</a> •
    <a href="#signin-to-telegram">Telegram Integration</a> •
</p>

<p align="center">
<b>Sources:</b>
  <a href="#currently-tools">Currently Tools</a> •
  <a href="#creating-your-own-tiger">Custom Tools (On-Prem Docker)</a> •
  <a href="#public-dashboard">Public Dashboard</a> •
</p>

<br>
<div align="center">
<img src="assets/overview.png" >
</div>
<br>

# What is Tiger?

Tiger is a community-driven project developing a reusable and integrated tool ecosystem for LLM Agent Revolution. It utilizes Upsonic for isolated tool storage, profillibg and for the automatic generation of documents. With Tiger, you can create a customized environment for your agents or leverage the robust and publicly maintained Tiger 🐅 curated by the community itself.

## Details

Tiger, influenced by [Neuralink](https://neuralink.com/), provides an AI-oriented computer interface with threads connected to the LLM interface. It offers a platform for AIs to control a computer by simply 'thinking'.

With Tiger, your LLM agents can write and execute code, use search engines, manage your calendar, control your mouse and keyboard, speak into your headphones, and much more. Essentially, anything conceived by your agent, Tiger will transform into concrete actions. This embodies the core philosophy of the Tiger project – to harness AI intelligence to generate tangible actions and support standard infrastructures. Our goals include:

- Providing a **Utility point** for agent tools across any framework that utilizes a function call mechanism,
- Building and nurturing a **Community of tool support** across diverse technologies and disciplines,
- Developing a **Free, Open and MIT** licensed tool library for the AI agent ecosystem.


# Setup

Tiger projects have a general usage public library at [tiger.upsonic.co](https://tiger.upsonic.co). Its include the tools that in `tools` library. For usage this you can use the standart connection that in upsonic python library. After installing the `upsonic` library we will use the Tiger object wand integrate to your agents.

- Tiger requires equal or higher python version to 3.8

```console
pip3 install upsonic
```

## Currently Tools

We are working on Upsonic and the tools that inside the `tools` folder is sending to public tiger in each release. We are aiming to create tools without any api key and just like normal human events like searching on google with mouse, keyboard and browser.

- App
  - open
  - close

- browser
  - open_url

- Interpreter

  - python
    - check_package
    - execute
    - install_package
  - sh
    - execute

- Search

  - google
  - duckduckgo
  - read_website

- System

  - os_name
  - architecture
  - python_version
  - clipboard
    - copy

- Knowledge
  - put
  - pull
  - delete
  - index
  - reset

- Communication
  - telegram
    - as_user
      - delete_message
      - get_last_dialogs
      - get_last_messages
      - send_message
      - signin

If you want to add functions to public and strongest Tiger you can see to [Adding Tools](#adding-tools) section.

## Public Dashboard

For the public Tiger you can see the functions and their documentations and readmes in [tiger.upsonic.co](https://tiger.upsonic.co). You can use this place for documentation also.

**Auth**

- username: tiger
- password: tiger

<br>
<div align="center">
<img src="assets/dashboard.png" width="700px">
</div>
<br>

## Documentation of Tiger Tools

Thanks to Upsonic we just write the codes and its gives us an storage system with detailed documentation and cpu ram usage for each function. Also you can make search and use functions in your other projects with connection code.

**Auth**

- username: tiger
- password: tiger

<br>
<div align="center">
<img src="assets/documentation.png" width="700px">
</div>
<br>

# crewAI Integration
Tiger project aim is being available for most popular agent framworks like `crewAI`. In this example you can see the easiest tool integration for an AI agent. We are asking for who is Onur Atakan ULUSOY and waits.

```console
pip3 install crewai 'crewai[tools]'
```

```python
# Geting the tiger tools
from upsonic import Tiger
tools = Tiger().crewai()



from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=OPENAI_API_KEY)



from crewai import Agent, Task, Crew, Process

researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="You are graduated from Research section of University",
  verbose=True,
  allow_delegation=False,
  tools=tools,
  llm=llm
)


task1 = Task(
  description="""Who is Onur Atakan ULUSOY""",
  expected_output="Full analysis report of Onur Atakan ULUSOY and putting the report to knowledge",
  agent=researcher
)


crew = Crew(
  agents=[researcher],
  tasks=[task1],
  verbose=2,
)


result = crew.kickoff()
```

# LangChain Integration

```console
pip3 install langchain langchain-openai
```

Tiger is able to make a collabration for sharing tools with LangChain agents with this your agents will able to use Tiger functions. In this example we are asking for an multiplation question and the agent will use the tiger  and after that its write a python code and tiger will give the result in behind. With this agent will able to make mathematical operations in just two lines of code.

```python
# Geting the tiger tools
from upsonic import Tiger
tools = Tiger().langchain()



# Generating Agent and executor with tiger tool set
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent

llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=OPENAI_API_KEY)
prompt = hub.pull("hwchase17/openai-functions-agent")
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# Asking for 15231 * 64231
agent_executor.invoke({"input": "What is the result of 15231 * 64231"})

```

# AutoGen Integration

```console
pip3 install pyautogen
```

Tiger is also have a integration with AutoGen agents. You can put a tiger to your AutoGen agents. In this examples we will use the 'interpreter.python' module and with this your autogen agent able to run and view result of python codes. With this your agent will able to wait 2 second as we request.

```python
# Generating Agents with tiger tool set
from typing_extensions import Annotated
import autogen

config_list = [
    {
        'model': 'gpt-4-0125-preview',
        'api_key': OPENAI_API_KEY,
    },
]

llm_config = {
    "config_list": config_list,
    "timeout": 120,
}
chatbot = autogen.AssistantAgent(
    name="chatbot",
    system_message="For coding tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done.",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
)



# Geting the tiger tools
from upsonic import Tiger
Tiger().autogen(chatbot, userproxy)



# Asking sleep 2 second
user_proxy.initiate_chat(
        chatbot,
        message="What is Upsonic.co",
    )
```

## Signin to Telegram
The user who wants to use telegram functionalities in their LLM agents must trig the signin function before all. For this you can use this function and its will ask for phone number and verification code.

```python
from upsonic import Tiger

Tiger().get("communication.telegram.as_user.signin__user")()
```

## Adding Tools

Tiger project is open to any contribution for public tiger, also in the bottom we have another way to create your own, offline tiger. For adding the public tiger you should create a pull request with your new tool.

1. Create a python file in `tiger/tools` section.
   for ex: `tiger/tools/interpreter/python/execute.py`

2. Write your function in this format

```python
#imports

def my_function(query:str) -> str:
    return query + " hi"


tool_name = "test.my_function"
tool_obj = my_function
tool_requirements = ["beautifulsoup4==4.12.3"]
```

3. Create the pull request. When its merged its will be available at public Tiger and dashboard.

## Creating your Own Tiger

For creating your own tiger you should install a Upsonic On-Prem docker container. Its will give a dashboard for viewing your own tools and will make documentation automatic. After that you should use the Upsonic Client to connect your On-Prem for this you should get the connection code from your dashboard and finaly you use the tiger function in upsonic client.

[Installation document](https://docs.upsonic.co/on-prem/getting_started/install_on_prem)

```python
#from upsonic import Tiger
#Tiger().autogen(chatbot, userproxy)

# to

#Your Upsonic Connection Code

upsonic.autogen(chatbot, userproxy)
```

## Star History

<br>
<div align="center">

<img src="https://api.star-history.com/svg?repos=Upsonic/Tiger&type=Date" width="600px">

</div>
<br>
