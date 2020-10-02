import time


a = True
while a == True:
    hello = "Hello You! \nik ben {owner}. hoe heet jij?"
    print(hello.format(owner = "Aki"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hallo " + username, "hier is je datum ")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("vandaag is het " + x.strftime("%d ") + x.strftime ("%B"))
    while True:
     time.sleep( 2 )

     antwoord1 = input("ik ga naar school met \n A de fiets \n B de auto \n C OV \n antwoord: ")
     if ( antwoord1 == "A"):
        print("leukk ik ga ook met de fiets")
     elif ( antwoord1 == "B"):
        print("heb je al een auto? niceee!!")
     elif ( antwoord1 == "C"):
        print("OV? waar kom je vandaan dan?")
        time.sleep( 2 )
        antwoord4 = input("Het OV heeft een storing wat doe je nu? \n A ik wacht hier, er is zo vast weer een werkende trein/tram/metro/bus \n B ik ga fietsen \n Cik laat mijn moeder me brengen \n antwoord:")
        if ( antwoord4 == "A"):
           print(" dat ging niet goed!!! je komt te laat op school")
           break 
        elif ( antwoord4 == "B"):
           print("fietsen lekker sportief!!")
           antwoord6 = input("je bent op school maar je weer niet waar je moet zijn, hoe ga je erachter komen? \n A magister \n B ik app een vriend \n C ik zoek wel \n antwoord:")
           if ( antwoord6 == "A"):
                 print("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
           elif ( antwoord6 == "B"):
                time.sleep( 2 )
                antwoord8 = input("jammer de vriend reageert niet, wat doe je nu?\n A magister \n B ik vraag t bij de receptie \n C ik zoek wel \n antwoord:")
                if ( antwoord8 == "A"):
                    print ("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
                elif ( antwoord8 == "B"):
                    print ("de receptie zget dat je geen les hebt, voor niks op  school gekomen?")
                elif ( antwoord8 == "C"):
                    print ("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
           elif ( antwoord6 == "C"):
                    print("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
                    time.sleep( 2 )
                    antwoord10 = input("je mag eindelijk naar huis, wat ga je doen \n A Huis \n B naar een vriend \n C naar een feestje \n antwoord:")
                    if ( antwoord10 == "A"):
                     print("nicee lekker uitrusten")
                    elif ( antwoord10 == "B"):
                     print("chill sesies met je vrienden yeet")
                    elif ( antwoord10 == "C"):
                     print("gekke fissa, je komt alleen niet op tijd thuis maarja ")
        elif (antwoord4 == "C"):
            print("moederskindje!!, achjaa je komt tenminste op tijd")
            antwoord7 = input("je bent op school maar je weer niet waar je moet zijn, hoe ga je erachter komen? \n A magister \n B ik app een vriend \n C ik zoek wel \n antwoord:")
            if ( antwoord7 == "A"):
                 print("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
            elif ( antwoord7 == "B"):
               time.sleep( 2 )
               antwoord9 = input("jammer de vriend reageert niet, wat doe je nu?\n A magister \n B ik vraag t bij de receptie \n C ik zoek wel \n antwoord:")
               if ( antwoord9 == "A"):
                        print ("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
                        antwoord12 = input("je mag eindelijk naar huis, wat ga je doen \n A Huis \n B naar een vriend \n C naar een feestje \n antwoord:")
                        if ( antwoord12 == "A"):
                         print("nicee lekker uitrusten")
                        elif ( antwoord12 == "B"):
                         print("chill sesies met je vrienden yeet")
                        elif ( antwoord12 == "C"):
                         print("gekke fissa, je komt alleen niet op tijd thuis maarja ")
                         time.sleep( 2 )
               elif ( antwoord9 == "B"):
                        print ("de receptie zget dat je geen les hebt, voor niks op  school gekomen?")
               elif ( antwoord9 == "C"):
                        print ("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
                        antwoord11 = input("je mag eindelijk naar huis, wat ga je doen \n A Huis \n B naar een vriend \n C naar een feestje \n antwoord:")
                        if ( antwoord13 == "A"):
                         print("nicee lekker uitrusten")
                        elif ( antwoord13 == "B"):
                         print("chill sesies met je vrienden yeet")
                        elif ( antwoord13 == "C"):
                         print("gekke fissa, je komt alleen niet op tijd thuis maarja ")
                         time.sleep( 2 )
            elif ( antwoord7 == "C"):
                    print("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
                    time.sleep( 2 )
                    antwoord11 = input("je mag eindelijk naar huis, wat ga je doen \n A Huis \n B naar een vriend \n C naar een feestje \n antwoord:")
                    if ( antwoord11 == "A"):
                         print("nicee lekker uitrusten")
                    elif ( antwoord11 == "B"):
                         print("chill sesies met je vrienden yeet")
                    elif ( antwoord11 == "C"):
                         print("gekke fissa, je komt alleen niet op tijd thuis maarja ")
                         time.sleep( 2 )
     
        
     antwoord2 = input("je bent op school maar je weer niet waar je moet zijn, hoe ga je erachter komen? \n A magister \n B ik app een vriend \n C ik zoek wel \n antwoord:")
     if ( antwoord2 == "A"):
         print("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
     elif ( antwoord2 == "B"):
        time.sleep( 2 )
        antwoord5 = input("jammer de vriend reageert niet, wat doe je nu?\n A magister \n B ik vraag t bij de receptie \n C ik zoek wel \n antwoord:")
        if ( antwoord5 == "A"):
            print ("nicee je komt er meteen achter waar je moet zijn, je gaat naar 1.08")
        elif ( antwoord5 == "B"):
            print ("de receptie zget dat je geen les hebt, voor niks op  school gekomen?")
        elif ( antwoord5 == "C"):
            print ("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
     elif ( antwoord2 == "C"):
        print("je komt erachter dat het lokaal 1.08 is maar je bent wel 10 min te laat")
     time.sleep( 2 )
     antwoord3 = input("je mag eindelijk naar huis, wat ga je doen \n A Huis \n B naar een vriend \n C naar een feestje \n antwoord:")
     if ( antwoord3 == "A"):
         print("nicee lekker uitrusten")
     elif ( antwoord3 == "B"):
        print("chill sesies met je vrienden yeet")
     elif ( antwoord3 == "C"):
        print("gekke fissa, je komt alleen niet op tijd thuis maarja ")
