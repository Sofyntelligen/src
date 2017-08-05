
from django_user_agents.utils import get_user_agent


def getSO(request):
    user_agent = get_user_agent(request)
    #print(user_agent.os.family)

    if user_agent.os.family == 'Windows 7':
        return 2
    if user_agent.os.family == 'Windows 8':
        return 3
    if user_agent.os.family == 'Windows 10':
        return 4
    if user_agent.os.family == 'WINDOWS SERVER':
        return 5
    if user_agent.os.family == 'Ubuntu':
        return 6
    if user_agent.os.family == 'LINUX DEBIAN':
        return 7
    if user_agent.os.family == 'MAC OS':
        return 8

    return 1


def getBrowser(request):
    user_agent = get_user_agent(request)
    #print(user_agent.browser.family)

    if user_agent.browser.family == 'Chrome':
        return 2
    if user_agent.browser.family == 'Firefox':
        return 3
    if user_agent.browser.family == 'IE':
        return 4
    if user_agent.browser.family == 'Safari':
        return 5
    if user_agent.browser.family == 'Opera':
        return 6

    return 1

