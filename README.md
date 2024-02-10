# Jellyfin Event Log

## Requirements:
- git clone https://github.com/Sean-Brooks/jellyfin_event_log.git
- cd jellyfin_event_log
- pip install -r requirements.txt

## API Token:
Login to Jellyfin > Dashboard > Advanced > Api Keys > create key > replace value of API_TOKEN

## Notes:
Replace JELLYFIN_HOST & API_TOKEN within jellyfin_event_log.py

## Running:
python jellyfin_event_log.py


```
                                                            Jellyfin Event Log
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Event                                                                                                      ┃ Date                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ sean is online from Safari                                                                                 │ 2024-02-10 @ 10:31:12 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────┤
│ kc has finished playing Jurassic Park - Jurassic.Park.1993.1080p.BluRay.mkv on Family Room TV              │ 2024-02-07 @ 14:13:41 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────┤
│ kc is playing Jurassic Park - Jurassic.Park.1993.1080p.BluRay.mkv on Family Room TV                        │ 2024-02-07 @ 12:49:37 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────┤
│ kc is online from Family Room TV                                                                           │ 2024-02-07 @ 12:48:15 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────┤
```
