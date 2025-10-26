# pc_quote_generator.py
# Custom Computer Quote Generator - Resume Ready (Indian Market)
# Author: Happy

import os

print("🇮🇳 Welcome to the Custom Computer Quote Generator!\n")

while True:
    # --- Option to Quit ---
    print("Type 'q' at any point to quit the program.\n")

    # --- Screen Size ---
    print("Please select your screen size:")
    print("a. 13\" (₹4,000)")
    print("b. 15\" (₹6,000)")
    print("c. 17\" (₹8,000)")
    screen_choice = input("> ").lower()
    if screen_choice in ["q", "quit"]:
        print("👋 Exiting program. Thank you!")
        break

    if screen_choice == "a" or screen_choice == "1":
        screen = '13"'
        screen_price = 4000
    elif screen_choice == "b" or screen_choice == "2":
        screen = '15"'
        screen_price = 6000
    else:
        screen = '17"'
        screen_price = 8000

    # --- RAM ---
    print("\nPlease select your RAM:")
    print("a. 8GB (₹3,500)")
    print("b. 16GB (₹6,500)")
    print("c. 32GB (₹12,000)")
    ram_choice = input("> ").lower()
    if ram_choice in ["q", "quit"]:
        print("👋 Exiting program. Thank you!")
        break

    if ram_choice == "a" or ram_choice == '1':
        ram = "8GB"
        ram_price = 3500
    elif ram_choice == "b" or ram_choice == "2":
        ram = "16GB"
        ram_price = 6500
    else:
        ram = "32GB"
        ram_price = 12000

    # --- CPU ---
    print("\nPlease select your CPU clock speed:")
    print("a. 2.5GHz (₹7,000)")
    print("b. 3.2GHz (₹12,000)")
    print("c. 4.0GHz (₹20,000)")
    cpu_choice = input("> ").lower()
    if cpu_choice in ["q", "quit"]:
        print("👋 Exiting program. Thank you!")
        break

    if cpu_choice == "a" or cpu_choice == "1":
        cpu = "2.5GHz"
        cpu_price = 7000
    elif cpu_choice == "b" or cpu_choice == "2":
        cpu = "3.2GHz"
        cpu_price = 12000
    else:
        cpu = "4.0GHz"
        cpu_price = 20000

    # --- Storage ---
    print("\nPlease select your storage:")
    print("a. 512GB HDD (₹2,000)")
    print("b. 512GB SSD (₹4,000)")
    print("c. 1TB SSD (₹7,000)")
    storage_choice = input("> ").lower()
    if storage_choice in ["q", "quit"]:
        print("👋 Exiting program. Thank you!")
        break

    if storage_choice == "a" or storage_choice == "1":
        storage = "512GB HDD"
        storage_price = 2000
    elif storage_choice == "b" or storage_choice == "2":
        storage = "512GB SSD"
        storage_price = 4000
    else:
        storage = "1TB SSD"
        storage_price = 7000

    # --- Graphics Card ---
    print("\nPlease select your Graphics Card:")
    print("a. Integrated (₹0)")
    print("b. Dedicated (₹10,000)")
    print("c. High-End (₹25,000)")
    gpu_choice = input("> ").lower()
    if gpu_choice in ["q", "quit"]:
        print("👋 Exiting program. Thank you!")
        break

    if gpu_choice == "a" or gpu_choice == "1":
        gpu = "Integrated"
        gpu_price = 0
    elif gpu_choice == "b" or gpu_choice == '2':
        gpu = "Dedicated"
        gpu_price = 10000
    else:
        gpu = "High-End"
        gpu_price = 25000

    # --- Total Cost ---
    total = screen_price + ram_price + cpu_price + storage_price + gpu_price

    # --- Discount Code ---
    print("\nDo you have a discount code? (PROMO-10 / PROMO-20 / PROMO-30)")
    code = input("> ").upper()
    if code in ["Q", "QUIT"]:
        print("👋 Exiting program. Thank you!")
        break

    discount = 0
    if code == "PROMO-10" or code == "1":
        discount = 0.10
    elif code == "PROMO-20" or code == '2':
        discount = 0.20
    elif code == "PROMO-30" or code == "3" and total >= 60000:
        discount = 0.30

    final_price = total - (total * discount)

    # --- Output Summary ---
    summary = f"""
----------------------------------------
🧾 Your Custom Computer Quote:
 - Screen Size: {screen} (₹{screen_price:,})
 - RAM: {ram} (₹{ram_price:,})
 - CPU: {cpu} (₹{cpu_price:,})
 - Storage: {storage} (₹{storage_price:,})
 - Graphics Card: {gpu} (₹{gpu_price:,})
----------------------------------------
💰 TOTAL PRICE: ₹{total:,}
"""

    if discount > 0:
        summary += f"🎟️ Discount applied: {int(discount*100)}%\n"
        summary += f"✅ FINAL PRICE after discount: ₹{final_price:,.2f}\n"
    else:
        summary += "❌ No discount applied.\n"

    summary += "----------------------------------------\nThank you for choosing Kaali Computers 💻🇮🇳\n"

    # --- Print & Save ---
    print(summary)
    with open("quote.txt", "w", encoding="utf-8") as file:
        file.write(summary)
    print("✅ Your quote has been saved to 'quote.txt'")

    # --- Option to Delete ---
    print("\nDo you want to delete the saved quote? (yes/no)")
    delete_choice = input("> ").lower()
    if delete_choice == "yes":
        if os.path.exists("quote.txt"):
            os.remove("quote.txt")
            print("🗑️ Saved quote deleted successfully!")
        else:
            print("❌ No saved quote found to delete.")
    else:
        print("💾 Your quote is safely saved!")

    # --- Ask to Continue ---
    print("\nDo you want to create another quote? (yes/no)")
    cont = input("> ").lower()
    if cont != "yes":
        print("👋 Exiting program. Thank you for using Kaali Computers!")
        break
