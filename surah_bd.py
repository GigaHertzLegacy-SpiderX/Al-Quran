# audio selection

def audio(url):
    import time
    import pafy
    import vlc

    audio = pafy.new(url)
    best = audio.getbestaudio()
    playurl = best.url
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    secs = int(audio.length)
    secs = secs + 5
    print("[+] Seaching for the audio...")
    print("[+] Playing the audio...")
    print("[*] It will take some time if your Internet Connection is slow...")
    time.sleep(10)
    print("[+] Press Ctrl+C to stop the audio")
    time.sleep(secs)
    print("")
    select()



def select():
    import sys
    user_input1 = int(input("Select which one you want to hear: "))
    if user_input1 == 1:
        print("[+] Playing Surah Al-Fatiha ( the opening )")
        url = "https://www.youtube.com/watch?v=zE_WFiHnSlY"
        audio(url)
    elif user_input1 == 2:
        print("[+] Playing Surah Al-Baqara (the Cow)")
        url = "https://www.youtube.com/watch?v=uRxyu_IoXJk&t=8s"
        audio(url)

    elif user_input1 == 3:
        print("[+] Playing Surah Aali Imran (the Family of Imran) ")
        url = "https://www.youtube.com/watch?v=HUt0yOQ1G7I&t=5s"
        audio(url)

    elif user_input1 == 4:
        print("[+] Playing Surah An-Nisa’ (the Women)")
        url = "https://www.youtube.com/watch?v=LinJ2c2p10w&t=4s"
        audio(url)

    elif user_input1 == 5:
        print("[+] Playing Surah Al-Ma’idah (the Table) ")
        url = "https://www.youtube.com/watch?v=9Z2cbMsDnig&t=4s"
        audio(url)

    elif user_input1 == 6:
        print("[+] Playing Surah Al-An’am (the Cattle)")
        url = "https://www.youtube.com/watch?v=26OuAh4F4JM&t=3s"
        audio(url)

    elif user_input1 == 7:
        print("[+] Playing Surah Al-A’raf (the Heights)")
        url = "https://www.youtube.com/watch?v=kANt948lz-U&t=4s"
        audio(url)

    elif user_input1 == 8:
        print("[+] Playing Surah Al-Anfal (the Spoils of War)")
        url = "https://youtu.be/yiScdzKEE5U&t=4s"
        audio(url)

    elif user_input1 == 9:
        print("[+] Playing Surah At-Tawba (the Repentance)")
        url = "https://youtu.be/lPlbDdDMFRQ&t=4s"
        audio(url)

    elif user_input1 == 10:
        print("[+] Playing Surah Yunus (the Prophet)")
        url = "https://youtu.be/DwpNZqwyFYY&t=4s"
        audio(url)

    elif user_input1 == 11:
        print("[+] Playing Surah Hud (the Witness)")
        url = "https://youtu.be/jhokAKQBo00?t=4"
        audio(url)

    elif user_input1 == 12:
        print("[+] Playing Surah Yusuf (the Light)")
        url = "https://youtu.be/lG8ugu2fRJE?t=4"
        audio(url)

    elif user_input1 == 13:
        print("[+] Playing Surah Ar-Ra’d (the Thunder)")
        url = "https://youtu.be/fW4zWnKhxRo?t=3"
        audio(url)

    elif user_input1 == 14:
        print("[+] Playing Surah Ibrahim (the Merciful)")
        url = "https://youtu.be/qG6xcFp8syM?t=4"
        audio(url)

    elif user_input1 == 15:
        print("[+] Playing Surah Al-Hijr (the Rocky Tract)")
        url = "https://youtu.be/PeASD3ZvPPo?t=4"
        audio(url)

    elif user_input1 == 16:
        print("[+] Playing Surah An-Nahl (the Bee)")
        url = "https://youtu.be/TSYT0dwn7ps?t=4"
        audio(url)

    elif user_input1 == 17:
        print("[+] Playing Surah Al-Isra’ (the Night Journey)")
        url = "https://youtu.be/xpFz6JUFIY4?t=4"
        audio(url)

    elif user_input1 == 18:
        print("[+] Playing Surah Al-Kahf (the Cave)")
        url = "https://youtu.be/Io0WdUNVZPc?t=4"
        audio(url)

    elif user_input1 == 19:
        print("[+] Playing Surah Maryam (Maryam)")
        url = "https://youtu.be/FBeoVl1B3EI?t=3"
        audio(url)

    elif user_input1 == 20:
        print("[+] Playing Surah Ta-Ha (Ta-Ha)")
        url = "https://youtu.be/9t41Kbz0BNk?t=4"
        audio(url)

    elif user_input1 == 21:
        print("[+] Playing Surah Al-Anbiya’ (the Prophets)")
        url = "https://youtu.be/lWf9U5Aibao?t=3"
        audio(url)

    elif user_input1 == 22:
        print("[+] Playing Surah Al-Hajj (the Pilgrimage)")
        url = "https://youtu.be/kYgorM75UQc?t=4"
        audio(url)

    elif user_input1 == 23:
        print("[+] Playing Surah Al-Muminoon (the Believers)")
        url = "https://youtu.be/QAz8eEVQtvs?t=4"
        audio(url)

    elif user_input1 == 24:
        print("[+] Playing Surah An-Nur (the Light)")
        url = "https://youtu.be/vEL9MlABLw4?t=4"
        audio(url)

    elif user_input1 == 25:
        print("[+] Playing Surah Al-Furqan (the Criterion)")
        url = "https://youtu.be/mYYjW2VDCNU?t=4"
        audio(url)

    elif user_input1 == 26:
        print("[+] Playing Surah Ash-Shu’ara’ (the Poets)")
        url = "https://youtu.be/Ovc9Ho4kwpk?t=4"
        audio(url)

    elif user_input1 == 27:
        print("[+] Playing Surah An-Naml (the lights)")
        url = "https://youtu.be/cAs74fcqIvk?t=4"
        audio(url)

    elif user_input1 == 28:
        print("[+] Playing Surah Al-Qasas (the Stories)")
        url = "https://youtu.be/tEtA41qV3gY?t=4"
        audio(url)

    elif user_input1 == 29:
        print("[+] Playing Surah Al-Ankabut (the Spider)")
        url = "https://youtu.be/vUz3k6GHaOw?t=4"
        audio(url)

    elif user_input1 == 30:
        print("[+] Playing Surah Ar-Rum (the Romans)")
        url = "https://youtu.be/Z5pr6S_dl30?t=4"
        audio(url)

    elif user_input1 == 31:
        print("[+] Playing Surah Luqman (Luqman)")
        url = "https://youtu.be/b0S-7pHxzy0?t=4"
        audio(url)

    elif user_input1 == 32:
        print("[+] Playing Surah As-Sajdah (the Prostration)")
        url = "https://youtu.be/t7OYOcKOZMU?t=4"
        audio(url)

    elif user_input1 == 33:
        print("[+] Playing Surah Al-Ahzab (the Combined Forces)")
        url = "https://youtu.be/dNMlWIHE6VE?t=4"
        audio(url)

    elif user_input1 == 34:
        print("[+] Playing Surah Saba’ (the Sabeans)")
        url = "https://youtu.be/R3vQwpmJTYA?t=4"
        audio(url)

    elif user_input1 == 35:
        print("[+] Playing Surah Fatir (the Originator)")
        url = "https://youtu.be/6Us3Fyjvj88?t=4"
        audio(url)

    elif user_input1 == 36:
        print("[+] Playing Surah Ya-Sin (the Impotence)")
        url = "https://youtu.be/DPttIrzp3rA?t=4"
        audio(url)

    elif user_input1 == 37:
        print("[+] Playing Surah As-Saffat (the Disbelievers)")
        url = "https://youtu.be/FZ8F_dmEN6E?t=4"
        audio(url)

    elif user_input1 == 38:
        print("[+] Playing Surah Sad (the Glorious)")
        url = "https://youtu.be/9eufPvum8k8?t=4"
        audio(url)

    elif user_input1 == 39:
        print("[+] Playing Surah Az-Zumar (the Groups)")
        url = "https://youtu.be/8UmdUUdoqYU?t=4"
        audio(url)

    elif user_input1 == 40:
        print("[+]Playing Surah Ghafir (the Forgiver)")
        url = "https://youtu.be/8JChVV2bq6Q?t=4"
        audio(url)

    elif user_input1 == 41:
        print("[+] Playing Surah Fussilat (the Clans)")
        url = "https://youtu.be/d7aeC5kNzLA?t=4"
        audio(url)

    elif user_input1 == 42:
        print("[+] Playing Surah Ash-Shura (the Consultation)")
        url = "https://youtu.be/W-6k79HAPa0?t=4"
        audio(url)

    elif user_input1 == 43:
        print("[+] Playing Surah Az-Zukhruf (the Ornaments)")
        url = "https://youtu.be/WRRAAonklRk?t=4"
        audio(url)

    elif user_input1 == 44:
        print("[+] Playing Surah Ad-Dukhan (the Smoke)")
        url = "https://youtu.be/CydFdttjlkQ?t=4"
        audio(url)

    elif user_input1 == 45:
        print("[+] Playing Surah Al-Jathiyah (the Crouching)")
        url = "https://youtu.be/lS1dhsoSS_Y?t=4"
        audio(url)

    elif user_input1 == 46:
        print("[+] Playing Surah Al-Ahqaf (the Valley)")
        url = "https://youtu.be/xIaJ8rHSDL8?t=4"
        audio(url)

    elif user_input1 == 47:
        print("[+] Playing Surah Muhammad (Muhammad)")
        url = "https://youtu.be/C8OdGS8JtLM?t=4"
        audio(url)

    elif user_input1 == 48:
        print("[+] Playing Surah Al-Fath (the Victory)")
        url = "https://youtu.be/QST0Eszp6uM?t=4"
        audio(url)

    elif user_input1 == 49:
        print("[+] Playing Surah Al-Hujurat (the Help)")
        url = "https://youtu.be/KteQMTDZxtI?t=4"
        audio(url)

    elif user_input1 == 50:
        print("[+] Playing Surah Qaf (Qaf)")
        url = "https://youtu.be/Qoy6dD8Iohk?t=4"
        audio(url)

    elif user_input1 == 51:
        print("[+] Playing Surah Adh-Dhariyat (the Scaterers)")
        url = "https://youtu.be/1cXyWIUMZDs?t=4"
        audio(url)

    elif user_input1 == 52:
        print("[+] Playing Surah At-Tur (the Mount)")
        url = "https://youtu.be/16EWlSm4FNw?t=4"
        audio(url)

    elif user_input1 == 53:
        print("[+] Playing Surah An-Najm (the Star)")
        url = "https://youtu.be/tU2UUTFyAGU?t=4"
        audio(url)

    elif user_input1 == 54:
        print("[+] playing Surah Al-Qamar (the Moon)")
        url = "https://youtu.be/ZYlJnZ9hYiE?t=4"
        audio(url)

    elif user_input1 == 55:
        print("[+] Playing Surah Ar-Rahman (the Most Gracious)")
        url = "https://youtu.be/OOVDppL7wQs?t=4"
        audio(url)

    elif user_input1 == 56:
        print("[+] Playing Surah Al-Waqi’ah (the Event)")
        url = "https://youtu.be/YLkXsn98tLE?t=4"
        audio(url)

    elif user_input1 == 57:
        print("[+] Playing Surah Al-Hadid (the Iron)")
        url = "https://youtu.be/YyIZtpG6XqM?t=4"
        audio(url)

    elif user_input1 == 58:
        print("[+] Playing Surah Al-Mujadilah (the Reasoning)")
        url = "https://youtu.be/Swf7lcyeNi0?t=4"
        audio(url)

    elif user_input1 == 59:
        print("[+] Playing Surah Al-Hashr (the Gathering)")
        url = "https://youtu.be/WwHik6yvnIA?t=4"
        audio(url)

    elif user_input1 == 60:
        print("[+] Playing Surah Al-Mumtahanah (the Transformation)")
        url = "https://youtu.be/KexIXbF09WU?t=4"
        audio(url)

    elif user_input1 == 61:
        print("[+] Playing Surah As-Saff (the Ranks)")
        url = "https://youtu.be/vppEUNsG150?t=4"
        audio(url)

    elif user_input1 == 62:
        print("[+] Playing Surah Al-Jumu’ah (the Congregation)")
        url = "https://youtu.be/Oi6IzlrD9bk?t=4"
        audio(url)

    elif user_input1 == 63:
        print("[+] Playing Surah Al-Munafiqun (the Hypocrites)")
        url = "https://youtu.be/UZKsoddxd7I?t=4"
        audio(url)

    elif user_input1 == 64:
        print("[+] Playing Surah At-Taghabun (the Evidence)")
        url = "https://youtu.be/SPKG6zifhOs?t=4"
        audio(url)

    elif user_input1 == 65:
        print("[+] Playing Surah At-Talaq (the Divorce)")
        url = "https://youtu.be/5B1oiQ-yy6c?t=4"
        audio(url)

    elif user_input1 == 66:
        print("[+] playing Surah At-Tahrim (the Prohibition)")
        url = "https://youtu.be/WSIUgcs3xjo?t=4"
        audio(url)

    elif user_input1 == 67:
        print("[+] Playing Surah Al-Mulk (the Kingdom)")
        url = "https://youtu.be/4JxAn7d37PE?t=4"
        audio(url)

    elif user_input1 == 68:
        print("[+] Playing Surah Al-Qalam (the Pen)")
        url = "https://youtu.be/6URt9CLENyU?t=4"
        audio(url)

    elif user_input1 == 69:
        print("[+] Playing Surah Al-Haqqah (the Ways of Help)")
        url = "https://youtu.be/UfmIZSt83rs?t=4"
        audio(url)

    elif user_input1 == 70:
        print("[+] Playing Surah Al-Ma’arij (the Ways of Suffering)")
        url = "https://youtu.be/D8OyiS6z8e8?t=3"
        audio(url)

    elif user_input1 == 71:
        print("[+] Playing Surah Nuh (Noah)")
        url = "https://youtu.be/x-Fi1AzumXg?t=4"
        audio(url)

    elif user_input1 == 72:
        print("[+] Playing Surah Al-Jinn (the Jinn)")
        url = "https://youtu.be/ruvNPsgjADQ?t=4"
        audio(url)

    elif user_input1 == 73:
        print("[+] Playing Surah Al-Muzzammil (Th False Prophet)")
        url = "https://youtu.be/IttWi-inJ_4?t=4"
        audio(url)

    elif user_input1 == 74:
        print("[+] Playing Surah Al-Muddaththir (The One who is Subdued)")
        url = "https://youtu.be/bJw-u6m5hII?t=4"
        audio(url)

    elif user_input1 == 75:
        print("[+] Playing Surah Al-Qiyamah (The Resurrection)")
        url = "https://youtu.be/LRQcawa4u_I?t=4"
        audio(url)

    elif user_input1 == 76:
        print("[+] Playing Surah Al-Insan (The Human)")
        url = "https://youtu.be/tWu3G26B1WA?t=4"
        audio(url)

    elif user_input1 == 77:
        print("[+] Playing Surah Al-Mursalat (The Names)")
        url = "https://youtu.be/hve0b58Ap6s?t=3"
        audio(url)

    elif user_input1 == 78:
        print("[+] Playing Surah An-Naba (The Announcement)")
        url = "https://youtu.be/NOQw3wqovE8?t=4"
        audio(url)

    elif user_input1 == 79:
        print("[+] Playing Surah An-Naziat (The Repentance)")
        url = "https://youtu.be/awloGGBgYu0?t=3"
        audio(url)

    elif user_input1 == 80:
        print("[+] Playing Surah ‘Abasa (He Frowned)")
        url = "https://youtu.be/ZwEmi43WpxE?t=4"
        audio(url)

    elif user_input1 == 81:
        print("[+] Playing Surah At-Takwir (The Overthrowing)")
        url = "https://youtu.be/hiOzmuPiiHw?t=4"
        audio(url)

    elif user_input1 == 82:
        print("[+] Playing Surah Al-Infitar (The Cleaving)")
        url = "https://youtu.be/hFK1E69gFYk?t=4"
        audio(url)

    elif user_input1 == 83:
        print("[+] Playing Surah Al-Mutaffifin (Those Who Deal in Fraud)")
        url = "https://youtu.be/Ac1QU83oMh4?t=4"
        audio(url)

    elif user_input1 == 84:
        print("[+] Playing Surah Al-Inshiqaq (The Splitting Asunder)")
        url = "https://youtu.be/ssoRzBaCm3A?t=4"
        audio(url)

    elif user_input1 == 85:
        print("[+] Playing Surah Al-Buruj (the Stars)")
        url = "https://youtu.be/-H5l3-mJ8H4?t=3"
        audio(url)

    elif user_input1 == 86:
        print("[+] Playing Surah At-Tariq (The Night comer)")
        url = "https://youtu.be/oGznT84kVmQ?t=4"
        audio(url)

    elif user_input1 == 87:
        print("[+] Playing Surah Al-A’la (The Most High)")
        url = "https://youtu.be/xnAaSKABpV4?t=4"
        audio(url)

    elif user_input1 == 88:
        print("[+] Playing Surah Al-Ghashiyah (The Overwhelming)")
        url = "https://youtu.be/8693yJ2bpss?t=4"
        audio(url)

    elif user_input1 == 89:
        print("[+] Playing Surah Al-Fajr (The Dawn)")
        url = "https://youtu.be/CgxILOWq6nI?t=3"
        audio(url)

    elif user_input1 == 90:
        print("[+] Playing Surah Al-Balad (The City)")
        url = "https://youtu.be/ZlYJIhjAIUM?t=4"
        audio(url)

    elif user_input1 == 91:
        print("[+] Playing Surah Al-Shams (The Sun)")
        url = "https://youtu.be/lp8QALOP5Jw?t=3"
        audio(url)

    elif user_input1 == 92:
        print("[+] Playing Surah Al-Layl (The Night)")
        url = "https://youtu.be/rDP0Tt7Mptg?t=3"
        audio(url)

    elif user_input1 == 93:
        print("[+] Playing Surah Ad-Duha (The Forenoon)")
        url = "https://youtu.be/AnO-X6tgiRs?t=4"
        audio(url)

    elif user_input1 == 94:
        print("[+] Playing Surah Al-Inshirah (The Opening Forth)")
        url = "https://youtu.be/H2hhGSEknkE?t=4"
        audio(url)

    elif user_input1 == 95:
        print("[+] Playing Surah Al-Tin (The Fig)")
        url = "https://youtu.be/XR3yuhq8-vI?t=4"
        audio(url)

    elif user_input1 == 96:
        print("[+] Playing Surah Al-Alaq (The Clot)")
        url = "https://youtu.be/jyvxnLmGG6U?t=4"
        audio(url)

    elif user_input1 == 97:
        print("[+] Playing Surah Al-Qadr (Tthe Night of Decree)")
        url = "https://youtu.be/p6EtgQZfwsQ?t=3"
        audio(url)

    elif user_input1 == 98:
        print("[+] Playing Surah Al-Bayyinah (The Clear Evidence)")
        url = "https://youtu.be/wlsgQ3UaiHk?t=4"
        audio(url)

    elif user_input1 == 99:
        print("[+] Playing Surah Az-Zalzalah (The Earthquake)")
        url = "https://youtu.be/Mda-1DO7XUM?t=4"
        audio(url)

    elif user_input1 == 100:
        print("[+] Playing Surah Al-Adiyat (The Runners)")
        url = "https://youtu.be/Me94_pWewsg?t=3"
        audio(url)

    elif user_input1 == 101:
        print("[+] Playing Surah Al-Qari’ah (The Striking Hour)")
        url = "https://youtu.be/KQbN6CE62sE?t=3"
        audio(url)

    elif user_input1 == 102:
        print("[+] Playing Surah At-Takathur (The Pilling Up)")
        url = "https://youtu.be/PwBsIsvZo78?t=4"
        audio(url)

    elif user_input1 == 103:
        print("[+] Playing Surah Al-‘Asr (The Time)")
        url = "https://youtu.be/PwBsIsvZo78?t=3"
        audio(url)

    elif user_input1 == 104:
        print("[+] Playing Surah Al-Humazah (The Wind)")
        url = "https://youtu.be/AD2FTfde3gs?t=4"
        audio(url)

    elif user_input1 == 105:
        print("[+] Playing Surah Al-Fil (The Elephant)")
        url = "https://youtu.be/OscMyxCioZ8?t=3"
        audio(url)

    elif user_input1 == 106:
        print("[+] Playing Surah Al-Quraish (The Quraish)")
        url = "https://youtu.be/EMKO5k_xiRE?t=3"
        audio(url)

    elif user_input1 == 107:
        print("[+] Playing Surah Al-Ma’un (the Assistance)")
        url = "https://youtu.be/rB1TOVHZ4CM?t=3"
        audio(url)

    elif user_input1 == 108:
        print("[+] Playing Surah Al-Kautsar (the River of Abundance)")
        url = "https://youtu.be/ifq6UO66g78?t=3"
        audio(url)

    elif user_input1 == 109:
        print("[+] Playing Surah Al-Kafirun (The Disbelievers)")
        url = "https://youtu.be/ZaHspJ0gRK8?t=4"
        audio(url)

    elif user_input1 == 110:
        print("[+] Playing Surah An-Nasr (The Help)")
        url = "https://youtu.be/GnOmpk-XFww?t=4"
        audio(url)

    elif user_input1 == 111:
        print("[+] Playing Surah Al-Masad/Lahab (the Palm Fiber)")
        url = "https://youtu.be/robx49fFmbk?t=3"
        audio(url)

    elif user_input1 == 112:
        print("[+] Playing Surah Al-Ikhlas (the Sincerity)")
        url = "https://youtu.be/UcxK4qDRMxk?t=3"
        audio(url)

    elif user_input1 == 113:
        print("[+] Playing Surah Al-Falaq (The Daybreak)")
        url = "https://youtu.be/oUb2UluKw7Q?t=3"
        audio(url)

    elif user_input1 == 114:
        print("[+] Playing Surah An-Nas (Mankind)")
        url = "https://youtu.be/EnRhAvlb9a4?t=3"
        audio(url)

    else:
        print("[-] Invalid Input")
        print("[-] Existing...")
        sys.exit()
