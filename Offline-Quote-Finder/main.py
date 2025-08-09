from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import json
import random
import os

console = Console()
QUOTES_FILE = "quotes.json"


if not os.path.exists(QUOTES_FILE):
    sample_quotes = [
        {"text": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
        {"text": "Don’t let yesterday take up too much of today.", "author": "Will Rogers"}
    ]
    with open(QUOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(sample_quotes, f, indent=4)

def load_quotes():
    with open(QUOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_quotes(keyword):
    quotes = load_quotes()
    return [q for q in quotes if keyword.lower() in q["text"].lower()]

def random_quote():
    quotes = load_quotes()
    return random.choice(quotes)

def display_quotes(quotes):
    table = Table(title="Quotes", box=box.ROUNDED, style="cyan")
    table.add_column("Quote", style="yellow", no_wrap=False)
    table.add_column("Author", style="green", no_wrap=True)

    for q in quotes:
        table.add_row(q["text"], q["author"])
    console.print(table)

def main():
    while True:
        console.print("\n[bold cyan]=== Offline Quote Finder ===[/bold cyan]")
        console.print("[yellow]1.[/yellow] Search for a quote")
        console.print("[yellow]2.[/yellow] Get a random quote")
        console.print("[yellow]3.[/yellow] Exit")

        choice = Prompt.ask("Enter choice", choices=["1", "2", "3"])

        if choice == "1":
            keyword = Prompt.ask("Enter keyword")
            results = search_quotes(keyword)
            if results:
                display_quotes(results)
            else:
                console.print("[red]No quotes found.[/red]")
        
        elif choice == "2":
            q = random_quote()
            display_quotes([q])
        
        elif choice == "3":
            console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
