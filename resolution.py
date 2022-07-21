#lists of products
products = ['computer', 'book', 'tablet', 'cellphone', 'tv', 'air conditioning', 'alexa', 'coffee machine', 'kindle']

#each item in the list of products corresponds to the amount of sales in the month and price, in that order
products_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

def tax_correction():
    print(products)
    #Input tax change: product name (all lowcase)
    product_name = input("1. Enter the name of the product that had the tax changed: ").lower()
    #Imput the signal of the tax, increase or decrease:
    signal_tax = input("2. Did the rate increase or decrease? (Insert: increase or decrease) ").lower()
    #Input tax change: percent of tax
    new_tax = float(input("3. Enter the number, just the number, of the new tax: "))

    #If product name in products
    if product_name in products:
        #Index of product in products list
        product_index = products.index(product_name)

        #Catch the index 1 (price) of products_ecommerce related to the product index mapped
        products_ecommerce_index = products_ecommerce[product_index]
        products_ecommerce_index_sales = products_ecommerce_index[0]
        products_ecommerce_index_price = products_ecommerce_index[1]

        #Values Before
        products_ecommerce_price_before = products_ecommerce_index[1]
        total_month_cost_before = products_ecommerce_index_sales * products_ecommerce_price_before

        #put the new tax in the product
        if signal_tax == "increase":
            tax_multiply = 1 + (new_tax/100)
        elif signal_tax == "decrease":
            tax_multiply = 1 - (new_tax/100)
        else:
            print ("We did not identify the second value passed, please try again.")
            tax_correction()

        products_ecommerce_price_after = products_ecommerce_index_price * tax_multiply
        
        #Impact of the tax chang on the business: increase in monthly spending on the product
        total_month_cost_after = products_ecommerce_price_after * products_ecommerce_index_sales

        #Result
        if signal_tax == "increase":
            print(f"With the increase of {new_tax}% on {product_name} price, we have: Price increase from {products_ecommerce_price_before} to {products_ecommerce_price_after}. Total month cost increase from {total_month_cost_before} to {total_month_cost_after}.")
        else:
            print(f"With the decrease of {new_tax}% on {product_name} price, we have: Price increase from {products_ecommerce_price_before} to {products_ecommerce_price_after}. Total month cost increase from {total_month_cost_before} to {total_month_cost_after}.")

    else:
        print("We did not identify the values passed, please try again.")
        print(f"Here is the list of products: {products}")
        tax_correction()

tax_correction()

