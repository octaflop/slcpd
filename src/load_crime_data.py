#!/usr/bin/python

import os
from urllib.request import urlretrieve

try:
    import click
except ImportError:
    print("Please `pip install Click` into your environment to continue!")

# use to allow -h for for help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


datasets = (
    {
        'year': '2007',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/p82y-bry5/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2007',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/h8d7-jp4e/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2008',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/gnbz-gub5/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2008',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/5f3u-md6v/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2009',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/86kk-a7va/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2009',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/v5p3-ghcp/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2010',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/wnzz-94g6/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2010',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/tdgj-y72g/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2011',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/u7f4-t2x3/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2011',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/6n3f-fxy7/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2012',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/wy4n-ink6/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2013',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/8b57-t7p2/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2013',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/uq2f-6aun/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2014',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/q8kg-i99f/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2014',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/bzjk-98k6/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2015',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/icir-dj48/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2016',
        'name': 'calls',
        'url': 'https://opendata.utah.gov/api/views/hmtz-uuer/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2016',
        'name': 'cases',
        'url': 'https://opendata.utah.gov/api/views/trgz-4r9d/rows.csv?accessType=DOWNLOAD'
    },
)


data_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..', 'data')


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option('1.0.0')
@click.pass_context
def cli(ctx):
    pass


@cli.command()
def load_crime_data():
    for ds in datasets:
        filename = 'slcpd_{}_{}.csv'
        save_path = os.path.abspath(os.path.join(
            data_path,
            filename.format(ds['name'], ds['year'])))
        click.echo('Saving to {} via url {}'.format(save_path, ds['url']))
        filename, headers = urlretrieve(ds['url'], save_path)
    return


if __name__ == '__main__':
    cli()
