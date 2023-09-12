weight = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = weight * width * height
volume_in_litres = volume / 1000
need_litres = volume_in_litres - (volume_in_litres * percent / 100)
print(need_litres)