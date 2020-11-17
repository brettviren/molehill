#!/usr/bin/env python3
'''
Main CLI to molehill
'''
import click
import molehill
import molehill.rc


@click.group()
@click.pass_context
def cli(ctx):
    '''
    molehill command line interface
    '''
    ctx.obj = {}


@cli.command()
def version():
    'Print the version'
    click.echo(molehill.__version__)


@cli.command()
@click.argument("config")
def rc(config):
    '''
    Start an RC process
    '''
    cfg = molehill.cfg.load(config)
    # molehill.cfg.validate(cfg)
    molehill.rc.run(cfg)


def main():
    'Main molehill'
    cli(obj=None)


if '__main__' == __name__:
    main()
