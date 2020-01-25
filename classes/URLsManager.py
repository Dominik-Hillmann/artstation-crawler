# Python libraries
import os
import json


class URLsManager:
    """Manages URLs from which pictures can be downloaded.
    It contains two lists: a list of already visited URLs and a list of URLs
    were not yet visited.
    """

    url_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'urls'))
    
    def __init__(self):
        self.queue = self._read_queue()
        self.visited = self._read_visited()

    
    def get_next_url(self):
        next_url = self.queue.pop()
        self.visited.add(next_url)
        self._write_queue()
        self._write_visited()

        return next_url


    def url_into_queue(self, url):
        if url not in self.visited:
            self.queue.append(url)
            self._write_queue()


    def urls_into_queue(self, urls):
        for url in urls:
            self.url_into_queue(url)

    
    def is_visited_url(self, url):
        return url in self.visited


    ###########
    # Private #
    ###########

    def _read_queue(self):
        with open(os.path.join(self.url_dir, 'queue.json'), 'r') as queue_file:
            queue = json.load(queue_file, encoding = 'utf-8')
            queue = queue.url_queue

            return queue


    def _read_visited(self):
        with open(os.path.join(self.url_dir, 'visited.json'), 'r') as visited_file:
            visited = json.load(visited_file, encoding = 'utf-8')
            visited = set(visited.visited_urls)

            return visited
    

    def _write_queue(self):
        with open(os.path.join(self.url_dir, 'queue.json'), 'w') as queue_file:
            json.dump(
                { 'url_queue': self.queue }, 
                queue_file,
                encoding = 'utf-8'
            )

    
    def _write_visited(self):
        with open(os.path.join(self.url_dir, 'visited.json'), 'w') as visited_file:
            json.dump(
                { 'visited_urls': list(self.visited) },
                visited_file,
                encoding = 'utf-8'
            )
