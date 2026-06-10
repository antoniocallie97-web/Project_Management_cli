from tabulate import tabulate


def print_table(data, headers):
    """
    Display data in a formatted table.
    
    Args:
        data (list): List of rows.
        headers (list): Column headers.
    """
    print(tabulate(data, headers=headers, tablefmt="grid"))