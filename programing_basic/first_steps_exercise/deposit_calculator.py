deposit_sum = float(input())
time_for_deposit = int(input())
year_interest_rate = float(input())

total = deposit_sum + time_for_deposit * ((deposit_sum * year_interest_rate / 100) / 12)
print(total)
