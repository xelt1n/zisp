#!/usr/bin/env python3
import speedtest
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run_test():
    try:
        st = speedtest.Speedtest()
        
        with console.status("[bold green]Finding best server...", spinner="dots"):
            st.get_best_server()
            server = st.results.server
        
        console.print(f"🌍 [bold cyan]Server:[/bold cyan] {server['sponsor']} ({server['name']})")

        with console.status("[bold blue]Testing Download...", spinner="growVertical"):
            dl = st.download() / 1_000_000

        with console.status("[bold magenta]Testing Upload...", spinner="growVertical"):
            ul = st.upload() / 1_000_000

        # Display results
        table = Table(show_header=True, header_style="bold white")
        table.add_column("Metric", style="dim")
        table.add_column("Result", justify="right")
        
        table.add_row("Download", f"[bold green]{dl:.2f} Mbps[/bold green]")
        table.add_row("Upload", f"[bold blue]{ul:.2f} Mbps[/bold blue]")
        table.add_row("Ping", f"{st.results.ping:.2f} ms")

        console.print(table)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    console.print(Panel.fit("⚡ [bold italic]ZISP[/bold italic] Speed Checker", border_style="magenta"))
    run_test()
