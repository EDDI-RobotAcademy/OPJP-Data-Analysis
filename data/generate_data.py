import numpy as np
import pandas as pd
import random

from faker import Faker
fake = Faker('ko_KR')

# 가격(price) 데이터 생성
def generate_prices(num_prices=400):
    prices = []

    for _ in range(num_prices):
        price = random.randint(1000, 10000)
        prices.append(price)
    
    return pd.DataFrame(prices)

prices = generate_prices(400)

prices.to_csv("prices.csv", index=False)