number = {"1":"January",
          "2":"February",
          "3":"March",
          "4":"April",
          "5":"May",
          "6":"June",
          "7":"July",
          "8":"August",
          "9":"Septeber",
          "10":"October",
          "11":"November",
          "12":"December"}

integer = input()
integer_str = str(integer)

if integer in number:
    print(number[integer])