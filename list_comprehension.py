incoming_requests = [
    {
        "request_id": "REQ001",
        "status": "completed",
        "items": [{"name": "Monitor", "price": 200}, {"name": "Cable", "price": 15}]
    },
    {
        "request_id": "REQ002",
        "status": "completed",
        "items": [{"name": "Laptop", "price": 1500}, {"name": "Gift", "price": 0}] # Invalid (price is 0)
    },
    {
        "request_id": "REQ003",
        "status": "pending",
        "items": [{"name": "Tablet", "price": 300}] # Invalid (status is pending)
    },
    {
        "request_id": "REQ004",
        "status": "completed",
        "items": [{"name": "Keyboard", "price": 50}]
    }
]

total_revenue = sum(
    sum(item["price"] for item in request["items"])
    for request in incoming_requests
    if request["status"] == "completed"
    and all(item["price"] > 0 for item in request["items"])
)

print(f"Total Revenue from valid completed requests: ${total_revenue:.2f}") # Output: Total Revenue from valid completed requests: $265.00

#user_payload = {
#    "user_id": 101,
#    "orders": [
#        {"order_id": 1, "status": "shipped"},
#        {"order_id": 2, "status": "pending"},
#        {"order_id": 3, "status": "shipped"}
#    ]
#}

#shipped_orders = [
#    order["order_id"] 
#    for order in user_payload["orders"] 
#    if order["status"] == "shipped"
#]

#print(shipped_orders) # Output: [1, 3]

#############################################

#def validate_product_price(product):
#    try:
#        price = float(product.get("price"))
#        if price <= 0:
#            return False
#        return True
#    except (ValueError, TypeError):
#        return False

#item_a = {"name": "Laptop", "price": "1200.50"}
#item_b = {"name": "Mouse", "price": "-10"}
#item_c = {"name": "Keyboard", "price": None}

#print(validate_product_price(item_a)) # Output: True
#print(validate_product_price(item_b)) # Output: False
#print(validate_product_price(item_c)) # Output: False