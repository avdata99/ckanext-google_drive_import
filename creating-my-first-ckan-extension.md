# Goole Drive Sheet import as dataset in CKAN

Created following [the oficial tutorial](https://docs.ckan.org/en/2.8/extensions/tutorial.html#installing-the-extension).  
Extension name: _ckanext-google_drive_import_.  

Download and run the [docker-ckan repo](https://github.com/okfn/docker-ckan).  

Create the extension
```
docker-compose -f docker-compose.dev.yml exec ckan-dev /bin/bash -c "paster --plugin=ckan create -t ckanext ckanext-google_drive_import -o /srv/app/src_extensions"
```

Setup extension [the tutorial](https://docs.ckan.org/en/2.8/extensions/tutorial.html#installing-the-extension).  

```
docker-compose -f docker-compose.dev.yml exec ckan-dev /bin/bash -c "cd  /srv/app/src_extensions/ckanext-google_drive_import && python setup.py develop"
```

Add the extension to _production.ini_:

```
docker-compose -f docker-compose.dev.yml exec ckan-dev /bin/bash -c "vi /srv/app/production.ini"
# add this:
ckan.plugins = ... <other extensions> ... google_drive_import
# restart ckan for reload plugins (? not sure)
docker-compose -f docker-compose.dev.yml restart ckan-dev

```



```
```
```
```
```
```
```
```
```