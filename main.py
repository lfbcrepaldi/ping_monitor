from ping3 import ping
import time
from rich.live import Live
from rich.table import Table
from typing import NoReturn

def get_ping_time(host):
    return ping(host, timeout=2, unit='ms', size=64)


def gen_table() -> Table:
    hosts = ['8.8.8.8', '1.1.1.1', 'pudim.com', 'pudim.com.br']

    table = Table()
    table.add_column('Host')
    table.add_column('Latency')
    for host in hosts:
        latency = get_ping_time(host)
        latency_str = f'{latency:.2f} ms' if latency is not None else 'Timeout'

        row_style = 'green' if latency is not None and latency < 100 else 'yellow' if latency is not None else 'red'
        table.add_row(host, latency_str, style=row_style)
    
    return table


def show_live_table() -> NoReturn:
    with Live(gen_table(), refresh_per_second=4) as live:
        while True:
            live.update(gen_table())
            time.sleep(1)

def main():
    try:
        show_live_table()
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == '__main__':
    main()
