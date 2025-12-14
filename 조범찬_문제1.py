# 파일명: 이름_문제1.py
# 문제 1. 계단 오르는 방법의 수 계산 (Bottom-up DP)

def stair_climbing_dp(n):
    # 0 이하의 입력 처리
    if n < 1:
        return 0
    
    # [cite_start]DP 테이블 생성 (인덱스 1부터 n까지 사용) [cite: 19]
    dp = [0] * (n + 1)
    
    # 초기값 설정
    dp[1] = 1  # 1계단은 1가지
    if n >= 2:
        dp[2] = 2  # 2계단은 2가지 (1+1, 2)
    
    # [cite_start]Bottom-up 방식으로 테이블 채우기 [cite: 19]
    # 점화식: dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

# 메인 실행 블록
if __name__ == "__main__":
    try:
        # 사용자 입력
        n_input = int(input("계단의 개수를 입력하시오: "))
        
        if n_input > 0:
            result = stair_climbing_dp(n_input)
            print(f"{n_input}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
        else:
            print("자연수를 입력해주세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")