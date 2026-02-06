import csv
from datetime import datetime, timedelta

def create_ics():
    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Horse Racing Sales//Entry Tracker//EN",
        "X-WR-CALNAME:Auction Entry Deadlines",
        "REFRESH-INTERVAL;VALUE=DURATION:PT1H"
    ]

    with open('sales_entries.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['sale_name']
            date_str = row['close_date'].replace("-", "")
            
            ics_content.append("BEGIN:VEVENT")
            ics_content.append(f"SUMMARY:ENTRY CLOSE: {name}")
            ics_content.append(f"DTSTART;VALUE=DATE:{date_str}")
            ics_content.append(f"DESCRIPTION:Entry deadline for {name} ({row['organizer']})")
            
            # 7-Day Reminder
            ics_content.append("BEGIN:VALARM")
            ics_content.append("TRIGGER:-P7D")
            ics_content.append("ACTION:DISPLAY")
            ics_content.append(f"DESCRIPTION:7-day reminder: {name} entries closing")
            ics_content.append("END:VALARM")
            
            # 1-Day Reminder
            ics_content.append("BEGIN:VALARM")
            ics_content.append("TRIGGER:-P1D")
            ics_content.append("ACTION:DISPLAY")
            ics_content.append(f"DESCRIPTION:URGENT: {name} entries close tomorrow")
            ics_content.append("END:VALARM")
            
            ics_content.append("END:VEVENT")

    ics_content.append("END:VCALENDAR")
    
    with open('deadlines.ics', 'w') as f:
        f.write("\n".join(ics_content))

if __name__ == "__main__":
    create_ics()
