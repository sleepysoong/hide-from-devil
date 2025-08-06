import requests

def get_usd_to_krw() -> float:
    """USD → KRW 환율을 반환합니다."""
    url = "https://api.exchangerate.host/latest"
    params = {
        "base": "USD",
        "symbols": "KRW"
    }
    resp = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    return data["rates"]["KRW"]
  
if __name__ == "__main__":
    try:
        rate = get_usd_to_krw()
        print(f"오늘 환율은 {rate:,.2f}원이에요.")
    except Exception as e:
        print("환율을 가져오는 중 오류가 발생했습니다:", e)
