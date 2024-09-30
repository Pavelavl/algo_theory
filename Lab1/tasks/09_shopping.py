#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

def find_min_prices(shops):
    sweets = {}
    all_sweets = set(item['name'] for shop in shops.values() for item in shop)
    
    for sweet in all_sweets:
        prices = []
        for shop_name, items in shops.items():
            for item in items:
                if item['name'] == sweet:
                    prices.append({'shop': shop_name, 'price': item['price']})
        
        sorted_prices = sorted(prices, key=lambda x: x['price'])[:2]
        sweets[sweet] = sorted_prices
    
    return sweets


sweets = find_min_prices(shops)

for sweet, details in sweets.items():
    print(f"{sweet}:")
    for detail in details:
        print(f"  Магазин: {detail['shop']}, Цена: {detail['price']}")