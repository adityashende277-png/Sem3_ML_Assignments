def validate_sku(sku):
    sku = sku.strip().upper()
    if len(sku) != 8:
        return "Invalid SKU"
    if not (sku[0:3].isalpha()):
        return "Invalid SKU"
    if sku[3] != "-":
        return "Invalid SKU"
    if not sku[4:8].isdigit():
        return "Invalid SKU"

    return "Valid: " + sku


sku = " xYz-9876 "

print(validate_sku(sku))