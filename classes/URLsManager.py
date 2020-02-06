# Python libraries
from os import path
import os
import json


class URLsManager:
    """Manages URLs from which pictures can be downloaded.
    It contains two lists: a list of already visited URLs and a list of URLs
    were not yet visited.
    """

    url_dir = path.abspath(path.join(__file__, '..', '..', 'urls'))
    
    def __init__(self, search_terms):
        self.search_dir_name = '_'.join(search_terms)
        self._create_seach_dir()
        self.queue = self._read_queue()
        self.visited = self._read_visited()
        print(self.queue, self.visited)

    
    def get_next_url(self):
        next_url = self.queue.pop()
        self.visited.add(next_url)
        self._write_queue(self.queue)
        self._write_visited(self.visited)

        return next_url


    def url_into_queue(self, url):
        if url not in self.visited:
            self.queue.append(url)
            self._write_queue(self.queue)


    def urls_into_queue(self, urls):
        for url in urls:
            self.url_into_queue(url)

    
    def is_visited_url(self, url):
        return url in self.visited


    ###################
    # Private methods #
    ###################

    def _read_queue(self):
        with open(path.join(self.url_dir, self.search_dir_name, 'queue.json'), 'r') as queue_file:
            queue = json.load(queue_file, encoding = 'utf-8')
            queue = queue['url_queue']

            return queue


    def _read_visited(self):
        with open(path.join(self.url_dir, self.search_dir_name, 'visited.json'), 'r') as visited_file:
            visited = json.load(visited_file, encoding = 'utf-8')
            visited = set(visited['visited_urls'])

            return visited
    

    def _write_queue(self, queue):
        with open(path.join(self.url_dir, self.search_dir_name, 'queue.json'), 'w') as queue_file:
            json.dump(
                { 'url_queue': queue }, 
                queue_file,
                encoding = 'utf-8'
            )

    
    def _write_visited(self, visited):
        with open(path.join(self.url_dir, self.search_dir_name, 'visited.json'), 'w') as visited_file:
            json.dump(
                { 'visited_urls': list(visited) },
                visited_file,
                encoding = 'utf-8'
            )

    
    def _create_seach_dir(self):
        all_search_term_dir_names = os.listdir(self.url_dir)
        if self.search_dir_name not in all_search_term_dir_names:
            os.mkdir(path.join(self.url_dir, self.search_dir_name))
            self._write_queue([])
            self._write_visited([])
            print('Created new search term directory because search terms were not encountered before.')
