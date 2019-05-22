import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Google_Drive_ImportPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm, inherit=True)

    # IDatasetForm

    def _add_country_codes(self, schema):
        # Add our custom country_code metadata field to the schema.
        schema.update({
                'country_code': [toolkit.get_validator('ignore_missing'),
                                toolkit.get_converter('convert_to_tags')('country_codes')]
                })
        return schema
    
    def _add_custom_text(self, schema):
        schema.update({
            'custom_text': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]})
        return schema


    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(Google_Drive_ImportPlugin, self).create_package_schema()
        schema = self._add_country_codes(schema)
        schema = self._add_custom_text(schema)
        return schema
    
    def update_package_schema(self):
        schema = super(Google_Drive_ImportPlugin, self).update_package_schema()
        schema = self._add_country_codes(schema)
        schema = self._add_custom_text(schema)
        return schema

    def show_package_schema(self):
        schema = super(Google_Drive_ImportPlugin, self).show_package_schema()
        schema = self._add_country_codes(schema)
        schema = self._add_custom_text(schema)
        return schema
    
    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        package_types = super(Google_Drive_ImportPlugin, self).package_types()
        if package_types is None:
            package_types = []
        return package_types + ['Google Drive Sheet']

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True
    
    """
    def package_form(self, package_type=None):
        return 'package/form.html'
    """

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'google_drive_import')