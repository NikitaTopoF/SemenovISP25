n_roads = int(input("Дороги:"))
best_road_num = 1
max_height = 0
for i in range(1, n_roads + 1):
    n_tunnels = int(input("Туннели:"))
    min_tunnel_height = float('inf')
    j = 0
    while j < n_tunnels:
        height = int(input("Высота:"))
        if height < min_tunnel_height:
            min_tunnel_height = height
        j += 1  
    if min_tunnel_height > max_height:
        max_height = min_tunnel_height
        best_road_num = i
print(best_road_num, max_height)

