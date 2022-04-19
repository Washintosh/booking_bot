from booking.booking import Booking

try:
  with Booking() as bot: #se realiza con el with para crear un context manager. Una vez que se sale del with, se ejecuta el método __exit__ presente en Booking. 
    currency = input("What currency do you want to use?: ")
    location = input("Where do you want to go?: ")
    check_in_date = input("What is your check-in date?: ")
    check_out_date = input("What is your check-out date?: ")
    number_adults = int(input("How many adults are?: "))
    bot.land_first_page()
    bot.change_currency(currency)
    bot.select_location(location)
    bot.select_dates(check_in_date, check_out_date)
    bot.select_adults(number_adults)
    bot.click_search()
    bot.apply_filtration()
    bot.refresh() #importante porque a veces hay que refrescar la página antes de ver los resultados
    bot.report_results()
except Exception as e:
  if "in PATH" in str(e):
    print("You are trying to run the bot from command line")
    print("Please add to PATH your Selenium Drivers")
    print("Windows:")
    print("   set PATH=%PATH%;C:path-to-your-folder")
    print()
    print("Linux:")
    print("   PATH=$PATH:/path-to-your-folder")
  else:
    raise