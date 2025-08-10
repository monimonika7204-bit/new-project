def print_line():
    print("-" * 70)

def print_header():
    print_line()
    print("{:^70}".format("XYZ Grocery Store - Final Bill"))
    print_line()
    print("{:<10} {:<25} {:<10} {:<10} {:<10}".format("ID", "Item Name", "Qty", "Price", "Total"))
    print_line()

def print_footer(total, gst, net_total):
    print_line()
    print("{:<50} {:>10}".format("Total", f"{total:.2f}"))
    print("{:<50} {:>10}".format("GST (5%)", f"{gst:.2f}"))
    print("{:<50} {:>10}".format("Net Total", f"{net_total:.2f}"))
    print_line()

# Predefined items with ID as key: ID: (Name, Price per unit, Default Qty)
item_catalog = {
    101: ("Rice", 40, 2),
    102: ("Sugar", 45, 1),
    103: ("Wheat Flour", 30, 5),
    104: ("Oil", 150, 1),
    105: ("Tea", 100, 1),
    106: ("Salt", 20, 1),
    107: ("Toothpaste", 55, 1),
    108: ("Soap", 25, 3),
    109: ("Shampoo", 90, 1),
    110: ("Detergent", 60, 2),
    # Add up to 50 items
}

def generate_bill():
    num_items = int(input("Enter number of items (max 50): "))
    if num_items > 50:
        print("❌ Maximum 50 items allowed.")
        return

    total = 0
    bill_items = []

    for i in range(num_items):
        item_id = int(input(f"Enter item ID {i+1}: "))
        if item_id in item_catalog:
            name, price, qty = item_catalog[item_id]
            item_total = qty * price
            bill_items.append((item_id, name, qty, price, item_total))
            total += item_total
        else:
            print(f"❌ Item ID {item_id} not found in catalog.")

    gst = total * 0.05
    net_total = total + gst

    # Print Bill
    print("\n" + "=" * 70)
    print_header()
    for item_id, name, qty, price, item_total in bill_items:
        print("{:<10} {:<25} {:<10} {:<10} {:<10.2f}".format(item_id, name, qty, price, item_total))
    print_footer(total, gst, net_total)

# Run the program
generate_bill()
