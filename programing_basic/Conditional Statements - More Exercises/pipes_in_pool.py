volume_of_pool = int(input())
flow_rate_of_first_pipe = int(input())
flow_rate_of_second_pipe = int(input())
time_of_pipe_working = float(input())

first_pipe_litres_water = flow_rate_of_first_pipe * time_of_pipe_working
second_pipe_litres_water = flow_rate_of_second_pipe * time_of_pipe_working
total_water = first_pipe_litres_water + second_pipe_litres_water

percent_pool_filed_from_first_pipe = (first_pipe_litres_water * 100 / total_water)
percent_pool_filed_from_second_pipe = (second_pipe_litres_water * 100 / total_water)
percent_pool_filed = total_water * 100 / volume_of_pool

if total_water <= volume_of_pool:
    print(f"The pool is {percent_pool_filed:.2f} % full. Pipe 1: {percent_pool_filed_from_first_pipe:.2f}%. Pipe 2: {percent_pool_filed_from_second_pipe:.2f}%.")
else:
    over_flow_water = total_water - volume_of_pool
    print(f"For {time_of_pipe_working} hours the pool overflows with {over_flow_water:.2f} liters.")

