from abc import (
    ABC, abstractmethod
)
from rich.table import Table
from rich.console import Console


class BaseTable(ABC):
    def __init__(self):
        self.console = Console()
        self.table = Table(show_header=True, header_style="bold magenta")

    @abstractmethod
    def populate_cols(self): pass

    @abstractmethod
    def populate_rows(self): pass

    @abstractmethod
    def print(self): pass
