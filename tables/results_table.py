from tables.base_table import BaseTable


class ResultsTable(BaseTable):
    def __init__(self):
        super().__init__()

    def populate_cols(self):
        self.table.add_column("Score", width=12)
        self.table.add_column("id", style="dim")
        self.table.add_column("name", style="dim")
        self.table.add_column("brand", style="dim")

        return self

    def populate_rows(self, rows):
        rows.sort(key=lambda r: r['score'], reverse=True)

        for r in rows:
            self.table.add_row(
                str(r['score']),
                str(r['item']['id']),
                r['item']['name'],
                r['item']['brand']
            )
        
        return self

    def print(self):
        self.console.log(self.table)
