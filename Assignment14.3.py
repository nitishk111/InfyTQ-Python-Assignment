child_discount = 1 / 3
fest_discount = 0.10
service_tax: float = 0.07
ticket_price = int(input("Enter price for a ticket: "))
ticket_adult = int(input("Enter total no of ticket bought for adult: "))
ticket_child = int(input("Enter total no of ticket bought for child: "))

price_adult = ticket_adult * ticket_price
price_child = ticket_child * (ticket_price * child_discount)

total_price = price_adult + price_child
total_price = total_price + total_price * service_tax
discounted_price = total_price - (total_price * fest_discount)

print("Total price to be paid by customer is "+str(discounted_price))

