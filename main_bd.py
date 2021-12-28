import sys

print("""
-------- بسم الله الرحمن الرحيم --------
 -- ( Bismillahir Rahmanir Rahim ) --

1. See all Surah of Al-Quran
2. Exit
""")

while True:
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        import visual
        visual.Oneto28()
        visual.N28to58()
        visual.N59to80()
        visual.N81to114()
        import surah_bd
        surah_bd.select()

    elif user_input == 2:
        print("Exiting...")
        sys.exit()
