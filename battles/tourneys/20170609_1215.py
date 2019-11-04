def getMonthName(mo):
    mos = ["invalid month", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    try:
        return mos[mo]
    except:
        return "invalid month"

