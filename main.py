#!/usr/bin/env python3
"""Plan-carry entry: turn $100 into the most money in 30 days.

The program writes a short, concrete plan to /output/entry.txt.
The plan is an AI agent selling same-day AI-made video ads to local
service businesses that already spend on advertising.
"""

PLAN = (
    "Sell $49 same-day AI video ads to roofers, dentists, gyms that "
    "already buy ads. Find 200 on Google Maps, email each a 15-second "
    "sample made for them, close by phone. Spend $100 on a domain, an "
    "email tool, a month of an AI video generator. Day 1: list 200 leads, "
    "send 100 emails."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"Wrote /output/entry.txt ({len(PLAN)} characters)")


if __name__ == "__main__":
    main()
