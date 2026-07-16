from client import TabstackBrowserlessAutomationClient
client = TabstackBrowserlessAutomationClient()
print(client.find_nodes("<div>Hello</div><div>World</div>", "div"))