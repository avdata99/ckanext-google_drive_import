import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.dictization.model_save import resource_dict_save
import logging
log = logging.getLogger(__name__)


class Google_Drive_ImportPlugin(plugins.SingletonPlugin):
    
    plugins.implements(plugins.IPackageController, inherit=True)

    # IPackageController
    def after_create(self, context, data):
        
        log.info('After Create GOOGLE DRIVE PLUGIN: Context: {}, Data: {}'.format(context, data))

        """ SAMPLE LOGs
        Context = {
            'allow_state_change': True,
            'allow_partial_update': True,
            'auth_user_obj': "USER OBJECT" ,
            '__auth_user_obj_checked': True,
            'session': " OBJECT sqlalchemy.orm.scoping.scoped_session",
            'user': 'ckan_admin',
            '__auth_audit': [],
            'model': 'MODULE ckan.model from /srv/app/src/ckan/ckan/model/__init__.pyc',
            'save': True,
            'message': ''
            }
        Data = {
            'maintainer': '',
            'name': 'polonia55644',
            'author': '',
            'author_email': '',
            'title': 'Dataset title',
            'notes': '',
            'owner_org': '60xxxxxxxxxxxxxxxxxxxx',
            'private': True,
            'maintainer_email': '',
            'url': 'https://docs.google.com/spreadsheets/d/1dUgDpVYDywwdqtWw0A8qqaCstgtb5GygsaTDRMIgUAo/edit?usp=drive_web&ouid=100530708543483213226',
            'state': 'draft',
            'version': '',
            'creator_user_id': '4eexxxxxxxxxxxxxxxxxxxxx',
            'id': '4f420a31-xxxxxxxxxxxxxxxx',
            'license_id': 'cc-by',
            'type': 'dataset',
            'tag_string': '',
            'tags': [],
            'extras': []
        }
        """

        url = data.get('url', None)
        log.info('GOOGLE DRIVE PLUGIN url: {}'.format(url))
        # detect google drive URLs
        # https://docs.google.com/spreadsheets/d/1dUgDpVYDywwdqtWw0A8qqaCstgtb5GygsaTDRMIgUAo/edit#gid=1559509753
        if url is None or not url.startswith('https://docs.google.com/spreadsheets'):
            return

        # I supouse never exists resources in creation time
        resources = data.get('resources', None)
        log.info('GOOGLE DRIVE PLUGIN Resources: {}'.format(resources))
        if resources is not None and len(resources) > 0:
            return 
        
        #TODO transform URL to get data as CSV
        #TODO Download CSV

        # save the resources (it works)
        #TODO lear URL an other params
        res_dict = {
                    # id: 0,
                    'url': 'http://no-se.com',
                    'format': 'CSV',
                    'description': 'Auto generated CSV from Google Drive Sheet Download',
                    'hash': '',
                    'package_id': data.get('id')
                }
        log.info('Save CSV data GOOGLE DRIVE PLUGIN as Resources: {}'.format(res_dict))
        resource = resource_dict_save(res_dict=res_dict, context=context)

        #TODO it worked but I can see the data after add a real resource in form. Prefill this with rsaved resource
        # Learn more about datasrt and resources. 
    
    