

def knapsack_packing_dp(W, items):
    n = len(items)
    
    A = [[0 for _ in range(W + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        name, wt, val = items[i-1]  
        for w in range(1, W + 1):
            if wt > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val + A[i-1][w - wt]  
                valWithout = A[i-1][w]         
                A[i][w] = max(valWith, valWithout)

    max_value = A[n][W]
    
    selected_items = []
    current_w = W
    
    for i in range(n, 0, -1):
        if A[i][current_w] != A[i-1][current_w]:
            name, wt, val = items[i-1]
            selected_items.append(name)
            current_w -= wt  

    selected_items.reverse()
    
    return max_value, selected_items

if __name__ == "__main__":
    print("=== 프로그램 시작 ===")
    items_data = [
        ('노트북', 3, 12),
        ('카메라', 1, 10),
        ('책', 2, 6),
        ('옷', 2, 7),
        ('휴대용 충전기', 1, 4)
    ]

    input_str = input("배낭 용량을 입력 하세요 : ")
    W_input = int(input_str)
    
    if W_input >= 0:
        max_val, selected = knapsack_packing_dp(W_input, items_data)
        
        print(f"최대 만족도: {max_val}")
        print(f"선택된 물건: {selected}")
    else:
        print("0 이상의 정수를 입력해주세요.")