#!/usr/bin/python

import os
import wget
import urllib

try:
    import click
except ImportError:
    print("Please `pip install Click` into your environment to continue!")

# use to allow -h for for help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


datasets = (
    {
        'year': '2016',
        'url': 'https://opendata.utah.gov/api/views/hmtz-uuer/rows.csv?accessType=DOWNLOAD'
    },
    {
        'year': '2015',
        'url': 'https://opendata.utah.gov/api/views/icir-dj48/rows.csv?accessType=DOWNLOAD'
    }
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
        filename = 'slcpd_calls_{}.csv'
        save_path = os.path.join(data_path, filename.format(ds['year']))
        click.echo('Saving to {} via url {}'.format(save_path, ds['url']))
        filename, headers = urllib.request.urlretrieve(ds['url'], save_path)
    return


if __name__ == '__main__':
    cli()
