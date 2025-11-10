"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("How old are you? "))
maximum_heart_beat = 220 - age
range = maximum_heart_beat * 0.65
range1 = maximum_heart_beat * 0.85
heart_rate_per_20_minute = maximum_heart_beat * 20.

print(f"Your maximum heart rate should be {int(range)} and {int(range1)} per minute.")
print(f"Your heart rate for at least 20 minutes should be around {heart_rate_per_20_minute}")