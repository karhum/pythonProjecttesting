# COPY THIS INTO THE BEGINNING OF YOUR EXERCISE

# this product identifier list could originate from a database system
# or something like that. there could also be hundreds of these codes
# instead of just these ones here.

# in this exercise, these identifiers are in this list.
# later in the course, we also practice downloading this kind of
# data from the internet!

# product identifiers list
products = ["K1565_2017_ST7745", "T2432_2019_FE84",
            "T8551_2018_XA413", "T3345_2019_JK142",
            "Y51372_2019_HJ2", "Y76715_2017_AB3",
            "E98144_2018_21T", "T7733_2020_CE55",
            "E7614_2021_XZA784", "E9722_2017_MHE67",
            "Y82018_2020_FI95", "T61287_2021_IA293",
            "E9152_2019_TY5", "T774_2021_OB672"]

year = input("Search code for which year?\n")

for product in products:
    product_info = product.split("_")
    if year == product_info[1]:
        print(product_info[0])
