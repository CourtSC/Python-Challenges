# A program to determine how much PTO will be accrued by a certain date.
import datetime
from math import floor

# currAmt is the current amount of PTO available, targetDate is the date you want to check (year, month, day),  lastDate is the date of the last PTO accrual (year, month, day), and accrual rate is how much you accrue per period in weeks.
def ptoCalc(currAmt, accrualRate, period):
    # Convert Args to datetime objects.
    targetDate, lastDate, period = datetime.date.fromisoformat(input("Enter the Date you would like to check (YYYY-MM-DD): ")), datetime.date.fromisoformat(input("Enter the date of the last PTO accrual: ")), datetime.timedelta(weeks=period)
    # Find number of weeks between lastDate and targetDate.
    timeDelta = targetDate - lastDate
    # Find how many accrual periods are in the timeDelta variable.
    iters = floor(timeDelta / period)
    # Return the amount of PTO for the given date.
    return round(currAmt + (accrualRate * iters), 4)

print(ptoCalc(-24.73, 5.54, 2))