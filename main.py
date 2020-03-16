"""This script collects pictures from a certain website to train a GAN later on."""

# Python libraries
from pprint import pprint
# Main classes
from classes.URLsManager import URLsManager
from classes.URLsExtractor import URLsExtractor
from classes.BrowserWrapper import BrowserWrapper
# Utility classes
from utils.ParameterParser import ParameterParser
from utils.Logger import Logger


def main():
    params = ParameterParser().get_params()
    urls_manager = URLsManager(
        params['search_terms'], 
        params['n_pics_in_batch'], 
        params['number_pictures']
    )    
    browser = BrowserWrapper(params['search_terms'], params['target_directory'])
    logger = Logger(params['log_file_directory'])

    try:
        logger.info('Started new session for search terms {}.'.format(
            ' '.join(params['search_terms'])
        ))
        if params['links_only']:
            logger.info('Using URL search-only mode.')
        elif params['pictures_only']:
            logger.info('Using picture download-only mode.')        

        while not urls_manager.total_pic_number_collected():
            collect_urls(params, urls_manager, browser, logger)            
            logger.info('Collected full batch of URLs. {} in queue.'.format(urls_manager.in_queue()))
            download_pics(params, urls_manager, browser, logger)
            logger.info('Downloaded all images from current batch, collecting new URLs.')

    except KeyboardInterrupt:
        logger.warn('Keyboard interrupt, trying to make URL lists persistent...')
        urls_manager.print_url_list_sizes()
        urls_manager.write_urls()

    finally:
        exit()
    

def collect_urls(params, urls_manager, browser, logger):
    if params['pictures_only']:
        return

    while not urls_manager.urls_exceed_batch_size(params['links_only']):
        browser.load_more_imgs()
        markup = browser.get_search_markup()
        urls = URLsExtractor(markup).get_urls()
        urls_manager.urls_into_queue(urls)
        
        if params['links_only']:
            logger.info('Now {} in queue.'.format(urls_manager.in_queue()))


def download_pics(params, urls_manager, browser, logger):
    if params['links_only']:
        return

    while urls_manager.urls_left():
        url = urls_manager.get_next_url()
        browser.screenshot(url)
        logger.info('Downloaded {}.'.format(url))


if __name__ == '__main__':
    main()
