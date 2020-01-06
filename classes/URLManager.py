class URLManager:
    """Manages URLs from which pictures can be downloaded."""
    
    def __init__(self):
        self.queue = []
        self.visited_urls = set()


    def add_urls(self, urls):
        """Prepends URLs to the queue such that the oldest URLs will be used first.
        
        Arguments
        ---------
            urls {list|str} -- URLs to be added.
        """

        if type(urls) is str:
            urls_to_be_added = [urls]
        else:
            urls_to_be_added = urls

        self._prepend_to_queue(urls_to_be_added)


    def get_next_url(self):
        """Returns the oldest URL available.
        
        Returns
        -------
            str or None -- URL if one is available, None if queue is empty. By then, program
            should be terminated.
        """

        try:
            next_url = self.queue.pop()
        except IndexError:
            return None

        self.visited_urls.add(next_url)
        return next_url


    def get_visited_urls(self):
        """Getter for the visited URLs.
        
        Returns
        -------
            set -- The visited URLs.
        """

        return self.visited_urls

    
    def unvisited_urls_left(self):
        """Whether there are still unvisited URLs left.
        
        Returns
        -------
            bool -- True if there are unused URLs.
        """

        return len(self.queue) != 0

    ###################
    # Private methods #
    ###################

    def _prepend_to_queue(self, urls):
        """Inserts new URLs such that the older ones will be used first.
        
        Arguments
        ---------
            urls {list} -- The URLs to be inserted.
        """

        for url in urls:
            self.queue.insert(0, url)
