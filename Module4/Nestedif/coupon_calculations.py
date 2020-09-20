def calculate_price(price, cash_coupon, percent_coupon):
    TAX = 1.06
    percent_coupon_convert = 1.00 - (percent_coupon/100.00)
    total = ((price - cash_coupon)*percent_coupon_convert)
    if total <= 10.00:
        total_f = total + 5.95
    if total <=30.00 and total > 10.00:
        total_f = total + 7.69
    elif total < 50.00 and total > 30.00:
        total_f = total + 11.95
    elif total > 50.00:
        total_f = total
    total_final = total*1.06
    total_final = round(total_final,2)
    print(total_final)
    return total_final
if __name__ == '__main__':
    calculate_price(100.00, 5.00, 10.00)
