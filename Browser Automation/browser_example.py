from connectonion import Agent
from connectonion.cli.browser_agent import BrowserAutomation

browser = BrowserAutomation()

agent = Agent("browser-bot", tools=[browser], model="gpt-4o-mini")

result = agent.input("Take a screenshot of example.com")

# result = agent.input("Navigate to example.com and take a screenshot")
# print(result)

# content = agent.input("Extract all the links from the page")
# print(content)

# agent.input("Fill the search box with 'AI Agents' and click search")