print("Welcome to the AK Flight Features and Demand Analysis Programme Platform")
GROUPID = input("Please enter your group code: ")
if GROUPID == ("AB319AK001"):
    USERID = input("Please enter your employee code: ")
    if USERID == ("AB319141225"):
        print("Welcome back CEO Ayan Kilje")
        print("Which files would you like to access")
        print("1. Airbus")
        print("2. Boeing")
        print("3. Cessna")
        print("4. Embrear")
        file_choice = input("Enter the number of the files that you would like to access. 1/2/3/4. : ")
        if file_choice == ("1"):
            print("What airbus plane's files would you like to access")
            print("A319")
            print("A320")
            print("A321")
            print("A330")
            print("A340")
            print("A350")
            print("A380")
            plane_choice = input("Enter the airbus plane files you would like to access by inputting the name of the plane: ")
            if plane_choice == ("A319"):
                print("Here is the link to the A319 Document: ")
    elif USERID == ("AB319310126"):
        print("Welcome back Arati Kilje, you will be working on AB319AK001")
        print("Here is the link: https://docs.google.com/document/d/1z4Izs2020Bh59xntLbGXc3bC-w7ioeLIokG6lxIKjyg/edit?tab=t.0")
        print("Here is the presentation link: https://docs.google.com/presentation/d/1jN8_vMv6L1y6N7dsTZ2osMB-mjCQoDMptGyaHpgLrfQ/edit?slide=id.p#slide=id.p")
        print("Here is the link to the guideline document: https://docs.google.com/document/d1C_trkGIpV_lQQF8rvWgryZevVnSKvOPRaqcChCCJdu8/edit?tab=t.0")
