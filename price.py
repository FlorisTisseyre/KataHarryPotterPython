def price(basket):
    return priceOfStowedSeries(stowSeries(basket))


def stowSeries(basket):
    stowedSeries = []
    for book in basket:
        stowBook(book, stowedSeries)
    return stowedSeries


def stowBook(book, stowedSeries):
    serie = smallestAvailableSerie(book, stowedSeries)
    if serie != None:
        serie.append(book)
    else:
        stowedSeries.append([book])


def smallestAvailableSerie(book, stowedSeries):
    availableSeries = findAvailableSeries(book, stowedSeries)
    if len(availableSeries) > 0:
        return min(availableSeries, key=len)
    else:
        return None


def findAvailableSeries(book, stowedSeries):
    availableSeries = []
    for stowedSerie in stowedSeries:
        if book not in stowedSerie:
            availableSeries.append(stowedSerie)
    return availableSeries


def priceOfStowedSeries(stowedSeries):
    price = 0
    for stowedSerie in stowedSeries:
        price += len(stowedSerie) * 8 * rate(len(stowedSerie))
    return price


def rate(length):
    return {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}[length]