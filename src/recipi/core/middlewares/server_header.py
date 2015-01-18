# -*- coding: utf-8 -*-
import pkg_resources


class ServerHeaderMiddleware(object):
    distribution_version = pkg_resources.get_distribution('recipi').version

    def process_response(self, request, response):
        response['Server'] = 'Recipi/{0}'.format(self.distribution_version)
        return response
