n = int(input("Введите количество блоков N: "))
error_index = -1
prev_hash = 0

for i in range(n):
    m = int(input("Введите m: "))
    r = int(input("Введите r: "))
    h = int(input("Введите h: "))
    
    calculated_h = (37 * (m + r + prev_hash)) % 256
    
    if h != calculated_h or h >= 100:
        if error_index == -1:
            error_index = i
            
    prev_hash = h

print(error_index)