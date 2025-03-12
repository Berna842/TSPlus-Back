#!python

import click    #type: ignore
import uvicorn  #type: ignore

@click.group
def cli() -> None:
    ...

@cli.command()
@click.option('--port', default=8000, help="port")
@click.option('--reload', default=False, help="reload")
@click.option('--use-colors', default=False, help="colorized logging")
def serve(port: int, reload: bool, use_colors: bool):
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        lifespan='on',
        reload=reload,
        use_colors=use_colors,
    )

if __name__ == '__main__':
    cli()