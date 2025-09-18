user_input = input("What's the weather like today? (sunny/rainy/cold):.").strip().lower()
#Selection 1 response
if user_input == "sunny":
    print("Wear a t-shirt and sunglasses.")

#Selection 2 response
elif user_input == "rainy":
    print("Don't forget your umbrella and a raincoat")

#Selection 3 response
elif user_input == "cold":
    print(" Make sure to wear a warm coat and a scarf.")     

else:
    print("Sorry, I don't have recommendations for this weather.")       