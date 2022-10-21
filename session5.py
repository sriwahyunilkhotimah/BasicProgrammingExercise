from operator import itemgetter



#input product name to variablebnj
#product_name = input(" input the product name : ")
#input product price to variable
#product_price = int(input(" input price of product: "))
#set 10% variable
#persen= 10
#input amount of items
#amount_items = int(input(" how many items do you buy : " ))
#harga product * jumlah yang di beli
#print ( " money spent " ,product_price*amount_items)
#calculate the 10% from the produk price
#profit= product_price*persen/100
#profit_items= profit* amount_items
#print ("profit 10% : " + str(profit))
#print("total profit : " + str(profit_items))
#print the final product price
#print(product_name,"sale price is : " , product_price + profit)
#price sale
#price_sale = product_price+profit
#total_selling = price_sale*amount_items
#print(" total sale price" ,total_selling)
#item sold
#item_sold = int (input("how many product have been sold : "))
#profit_sold = profit * item_sold
#print("profit from items sold : " + str(profit_sold))

products = []

while(True):
    product = {}
    product ["name"] = input("input product_name : ")
    product ["price"] = int (input("input product price : "))
    product ["stock"] = int(input("input product stock : "))
        
    #add product to products variable
    products.append(product)

    isBreak = input("stop the application? y for yes n for no : ")
    if(isBreak == "y" ) :
        break

pieces=[]

print(products[0])
for i in products :
    pieces.append(i["price"])

print(pieces[0])

