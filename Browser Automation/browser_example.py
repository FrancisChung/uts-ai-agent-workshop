from connectonion import Agent
from connectonion.tools import BrowserTool

browser = BrowserTool()

agent = Agent("browser-bot", tools=[browser])

result = agent.input("Navigate to example.com and take a screenshot")
print(result)

content = agent.input("Extract all the links from the page")
print(content)

agent.input("Fill the search box with 'AI Agents' and click search")