import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='PersonalizedNetworkingAssistant/1.0'
)

def get_fact(topic):
    page = wiki.page(topic)

    if page.exists():
        return page.summary[:500]

    return "No information found."