n = int(input())
fixed_dates = set()
companies = set()
ans = 0

for company in range(n):
    c = int(input())
    for i in range(c):
        start_date, period = list(map(int, input().split()))

        interns = [i for i in range(start_date, start_date + period)]
        posibility = True
        for day in interns:
            if day in fixed_dates:
                posibility = False
                break

        # all days are available
        if posibility:
            companies.add(company)
            for day in interns:
                fixed_dates.add(day)

print(len(companies))
