"""
Scrapy Probe

See documentation in docs/topics/probe.rst
"""

from scrapy.command import ScrapyCommand


class Command(ScrapyCommand):

    requires_project = False
    #default_settings = {'KEEP_ALIVE': True, 'LOGSTATS_INTERVAL': 0}

    def syntax(self):
        return "[url|text]"

    def long_desc(self):
        return "Interactive console for scraping the given url and text"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)

    def run(self, args, opts):

        # TODO
        # get url argument
        # get text argument
        # see if better way to get args
        # see if args is a valid url use is_url(args[0])
        # if any fail print help to command line
        # Need studie what to do next after get args
        url = args[0] if args else None # ?ME: studie this if
        text = args[1]
