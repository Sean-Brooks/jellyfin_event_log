import requests
from rich.console import Console
from rich.table import Table

# Supress all SSL warnings
requests.packages.urllib3.disable_warnings()

JELLYFIN_HOST = '{URL_OF_JELLYFIN_HOST (i.e. https://example.jellyfin.con:9999)}'
API_TOKEN = '{CREATE_API_TOKEN_IN_JELLYFIN_DASHBOARD_THEN_INSERT_HERE}'


def get_auth():
    url = f"{JELLYFIN_HOST}/Auth/Keys"
    headers = {
        'Accept': 'application/json',
        'X-Emby-Token': API_TOKEN
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()


def get_activity(api_auth):
    url = f"{JELLYFIN_HOST}/System/ActivityLog/Entries"
    headers = {
        'Accept': 'application/json',
        'X-Emby-Token': api_auth['Items'][0]['AccessToken']
    }
    activity_response = requests.request("GET", url, headers=headers, verify=False)
    activity = activity_response.json()

    table = Table(title='Jellyfin Event Log', show_lines=True)
    table.add_column("Event", justify="left", style="cyan")
    table.add_column("Date", justify="left", style="green")

    for item in activity['Items']:
        table.add_row(f"{item['Name']}",
                      f"{item['Date'].replace('T', ' @ ').split('.')[0]}",
                      )
    console = Console()
    console.print(table)


def main():
    get_activity(get_auth())


if __name__ == '__main__':
    main()
