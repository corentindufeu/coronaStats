from http.client import HTTPSConnection, HTTPResponse
from json import loads
from datetime import date


def api_communication(country):
    """return information of covid in real time of country in argument, from api covid-193 (rapidapi.com)"""

    conn = HTTPSConnection("covid-193.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "b8720768f1msh29e8c2d3c6dc72dp16a6e6jsn4d855b4ab5f2",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    conn.request("GET", "/history?country=" + country + "&day=" + str(date.today()), headers=headers)
    res: HTTPResponse = conn.getresponse()
    data: bytes = res.read()

    return data.decode("utf-8")


def non_breaking_spaces_number(number):
    """add space every 3 numbers for readability"""
    number = list(number.strip())
    y: int = len(number)
    for i in range(y):
        y -= 1
        if i % 3 == 0:
            number[y] += " "
    number = "".join(number)
    return number


def search_stats(data_transfer, key, *args):
    """get api dict and keys, and return all information recherche"""
    for i in args:
        stat: str = str(data_transfer[0]["response"][0][key][i])
        stat: str = non_breaking_spaces_number(stat)
        data_transfer[1].update({i+"_"+key: stat})


def search_information(country):
    data = api_communication(country)
    data = loads(data)
    if data['results'] == 0:
        return

    allInformation: dict = {}

    # country information
    country: str = str(data["response"][0]["country"])
    population: str = str(data["response"][0]["population"])
    population: str = non_breaking_spaces_number(population)
    allInformation.update({'population': population, 'country': country})

    # stats
    data_transfer: tuple = (data, allInformation)
    search_stats(data_transfer, "cases", "active", "new", "critical", "recovered", "total")
    search_stats(data_transfer, "deaths", "new", "total")
    search_stats(data_transfer, "tests", "total")

    return allInformation

