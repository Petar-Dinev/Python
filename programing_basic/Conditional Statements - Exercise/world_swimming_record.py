world_record_in_seconds = float(input())
metres_for_swimming = float(input())
time_in_seconds_for_one_meter_swimming = float(input())

delay = (metres_for_swimming // 15) * 12.5
ivan_time = metres_for_swimming * time_in_seconds_for_one_meter_swimming + delay
difference = abs(ivan_time - world_record_in_seconds)

if ivan_time >= world_record_in_seconds:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")

