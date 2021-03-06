class Validator:
    """
    Class to provide validation for queries
    """
    def isValidSearchQuery(self, searchQuery):
        """
        Check whether query is a valid search query
        """
        if len(searchQuery) != 4:
            return False
        validSearchQueries = [["search", "client", "name"],
                              ["search", "movie", "title"],
                              ["search", "movie", "description"],
                              ["search", "movie", "genre"]]
        isValidQuery = False
        for query in validSearchQueries:
            if query[0] == searchQuery[0] and query[1] == searchQuery[1] and query[2] == searchQuery[2]:
                    isValidQuery = True
        return isValidQuery

    def isValidStatsQuery(self, statsQuery):
        """
        Check whether query is a valid stats query
        """
        if len(statsQuery) != 2 and len(statsQuery) != 3:
            return False
        if len(statsQuery) == 2:
            validStatsQueries = [["active", "clients"], ["now", "rented"], ["late", "rentals"]]
            isValidQuery = False
            for query in validStatsQueries:
                if query[0] == statsQuery[0] and query[1] == statsQuery[1]:
                    isValidQuery = True
        elif len(statsQuery) == 3:
            validStatsQueries = [["most", "rented", "days"], ["most", "rented", "times"]]
            isValidQuery = False
            for query in validStatsQueries:
                if query[0] == statsQuery[0] and query[1] == statsQuery[1] and query[2] == statsQuery[2]:
                    isValidQuery = True
        return isValidQuery

    def isValidRemoveQuery(self, removeQuery):
        if len(removeQuery) != 2:
            return False
        if not removeQuery[1].isdigit():
            return False
        return True

    def isValidUpdateQueryWithNumberOfElements(self, updateQuery, numberOfElements):
        if len(updateQuery) != numberOfElements:
            return False
        if not updateQuery[1].isdigit():
            return False
        return True



