from typing import Optional

import typer
from rich import print
from rich.console import Console
from rich.table import Table
from stuart.core import add_event_source, get_event_source

main = typer.Typer(help="Stuart Couriers Application")
console = Console()

@main.command()
def add_parameters(
    max_capacity: int = typer.Option(...),
    capacity_required: int = typer.Option(...),

):
    """Adds new Couriers Parameters"""
    if add_event_source(max_capacity, capacity_required):
        print(":motorcycle: New Couriers Capacity Added :truck:")
    else:
        print(":no_entry: - Cannot add Event.")


@main.command("list")
def list_events(style: Optional[str] = None):
    """Lists Couriers Parameters from the database"""
    stuart = get_event_source(style)
    table = Table(
        title="Stuart Couriers informations (in liters)." if not style else f"Stuart {style}"
    )
    headers = [
        "id",
        "max_capacity",
        "capacity_required",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for stuart in stuart:
        stuart.date = stuart.date.strftime("%Y-%m-%d")
        values = [str(getattr(stuart, header)) for header in headers]
        table.add_row(*values)
    console.print(table)