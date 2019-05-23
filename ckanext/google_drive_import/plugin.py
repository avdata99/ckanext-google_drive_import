import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import logging
log = logging.getLogger(__name__)


class Google_Drive_ImportPlugin(plugins.SingletonPlugin):
    
    plugins.implements(plugins.IPackageController, inherit=True)

    # IPackageController
    def after_create(self, context, data):
        
        log.info('After Create GOOGLE DRIVE PLUGIN: Context: {}, Data: {}'.format(context, data))
        url = data.get('url', None)
        log.info('GOOGLE DRIVE PLUGIN url: {}'.format(url))
        # detect google drive URLs
        # https://docs.google.com/spreadsheets/d/1dUgDpVYDywwdqtWw0A8qqaCstgtb5GygsaTDRMIgUAo/edit?usp=drive_web&ouid=100530708543483213226
        if url is None or not url.startswith('https://docs.google.com/spreadsheets'):
            return

        # si no tiene recursos, crearlos
        resources = data.get('resources', None)
        log.info('GOOGLE DRIVE PLUGIN Resources: {}'.format(resources))
        if resources is None or len(resources) > 0:
            return 
        
    
    