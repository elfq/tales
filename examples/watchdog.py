from tales import watchdog, api

api.watchdog = "" # Your API Key

print(f"Minutes after last ban: {watchdog.last_minute()}\nDaily bans from staff: {watchdog.staff_bans_daily()}\nDaily bans from watchdog: {watchdog.watchdog_bans_daily()}\nStaff bans total: {watchdog.staff_total_bans()}\nWatchdog bans total: {watchdog.total_bans()} ")

