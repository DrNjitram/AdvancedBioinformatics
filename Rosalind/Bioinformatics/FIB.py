months = [1, 1]
current_month = 2

target_month = 28
increase = 3

while current_month < target_month:
    months.append(months[current_month - 2] * increase + months[current_month - 1])
    current_month += 1
    print(months)
