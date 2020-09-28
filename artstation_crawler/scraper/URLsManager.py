# Python libraries
from os import path
import os
import json


class URLsManager:
    """Manages URLs from which pictures can be downloaded.
    It contains two lists: a list of already visited URLs and a list of URLs
    were not yet visited.
    Args:
        search_terms (List[str]): The terms which you search on artstation.
        batch_size ([type]): Number of images handled at once.
        total_pic_number ([type]): Maximum number of images to be downloaded.    
    """

    url_dir = path.abspath(path.join(__file__, '..', '..', 'urls'))
    
    def __init__(self, search_terms, batch_size, total_pic_number):
        self.search_dir_name = '_'.join(search_terms)
        self._create_seach_dir()
        self.queue = self._read_queue()
        self.visited = self._read_visited()
        
        self.batch_size = batch_size
        self.total_pic_number = total_pic_number

    
    def get_next_url(self):
        """Get the next URL in line.

        Returns:
            str: The next URL.
        """

        if len(self.queue) == 0:
            return None

        next_url = self.queue.pop()
        self.visited.add(next_url)
        self._write_queue(self.queue)
        self._write_visited(self.visited)

        return next_url


    def urls_into_queue(self, urls):
        """Put the URLs into queue.

        Args:
            urls (List[str]): The URLs which will be put into queue.
        """

        if urls is None:
            return

        for url in urls:
            self.url_into_queue(url)


    def url_into_queue(self, url):
        """Put this URL into queue.

        Args:
            url (str): The URL to be put into queue.
        """

        if url not in self.visited:
            self.queue.append(url)
            self._write_queue(self.queue)


    def total_pic_number_collected(self):
        """Whether the maximum number of images has been collected.

        Returns:
            bool: Whether the maximum has been collected.
        """

        return len(self.visited) >= self.total_pic_number

    
    def is_visited_url(self, url):
        """Whether this URL was already visited.

        Args:
            url (str): The URL.

        Returns:
            bool: Visitation status.
        """

        return url in self.visited


    def urls_exceed_batch_size(self, url_search_mode):
        """Whether there are enough URLs in queue.

        Args:
            url_search_mode (bool): Whether the program runs in the URL search only mode.

        Returns:
            bool: Whether this is true.
        """

        if url_search_mode:
            # If we only search for URLs, then the batch size never exceeds. 
            return False
        else:
            return len(self.queue) > self.batch_size


    def in_queue(self):
        """Number of URLs in queue.

        Returns:
            int: Number in queue.
        """

        return len(self.queue)

    
    def urls_left(self):
        """Whether there are still URLs left to be queried.

        Returns:
            bool: Whether this is true.
        """

        return len(self.queue) > 0

    
    def write_urls(self):
        """Save the current status of visited URLs and URLs in queue to disk."""

        self._write_queue(self.queue)
        self._write_visited(self.visited)

    
    def print_url_list_sizes(self):
        """Prints information if a keyboard interrupt happens."""

        print('Writing managed URLs due to keyboard interrupt: {} in queue and {} visited.'.format(
            str(len(self.queue)),
            str(len(self.visited))
        ))


    ###################
    # Private methods #
    ###################

    def _read_queue(self):
        """The URLs in queue.

        Returns:
            List[str]: The URLs.
        """

        with open(path.join(self.url_dir, self.search_dir_name, 'queue.json'), 'r') as queue_file:
            queue = json.load(queue_file, encoding = 'utf-8')
            queue = queue['url_queue']

            return queue


    def _read_visited(self):
        """The visited URLs.

        Returns:
            [List[str]]: The visited URLs.
        """

        with open(path.join(self.url_dir, self.search_dir_name, 'visited.json'), 'r') as visited_file:
            visited = json.load(visited_file, encoding = 'utf-8')
            visited = set(visited['visited_urls'])

            return visited
    

    def _write_queue(self, queue):
        """Write the queue to disk.

        Args:
            queue (List[str]): The queue.
        """

        with open(path.join(self.url_dir, self.search_dir_name, 'queue.json'), 'w') as queue_file:
            json.dump(
                { 'url_queue': queue }, 
                queue_file,
                encoding = 'utf-8'
            )

    
    def _write_visited(self, visited):
        """Write visited URLs to disk.

        Args:
            visited (List[str]): The visited URLs.
        """

        with open(path.join(self.url_dir, self.search_dir_name, 'visited.json'), 'w') as visited_file:
            json.dump(
                { 'visited_urls': list(visited) },
                visited_file,
                encoding = 'utf-8'
            )

    
    def _create_seach_dir(self):
        """Cretes serach term directory if there isn't one."""

        all_search_term_dir_names = os.listdir(self.url_dir)
        if self.search_dir_name not in all_search_term_dir_names:
            os.mkdir(path.join(self.url_dir, self.search_dir_name))
            self._write_queue([])
            self._write_visited([])
            print('Created new search term directory because search terms were not encountered before.')
