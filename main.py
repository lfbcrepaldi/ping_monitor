from ping3 import ping
import time
from rich.live import Live
from rich.table import Table


def get_ping_time(host):
    return ping(host, timeout=2)


def gen_table() -> Table:
    hosts = ['8.8.8.8', '8.8.4.4', '1.1.1.1', 'example.com']

    table = Table()
    table.add_column('Host')
    table.add_column('Latency')
    for host in hosts:
        latency = get_ping_time(host)
        latency_str = f'{latency*1_000:.2f} ms' if latency is not None else 'Timeout'
        
        row_style = 'green' if latency is not None and latency < 0.1 else 'yellow' if latency is not None else 'red'
        table.add_row(host, latency_str, style=row_style)
    
    return table


def main():
    with Live(gen_table(), refresh_per_second=4) as live:
        while True:
            live.update(gen_table())
            time.sleep(1)


if __name__ == '__main__':
    main()
