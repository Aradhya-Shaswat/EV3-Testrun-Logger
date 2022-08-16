import os
import time

try:
    import pyfiglet
    heading = pyfiglet.figlet_format(
        "EV3 Test Runs Record Logger", justify="center")

except ImportError:
    heading = "\033[1mEV3 Test Runs Record Logger\033[0m"


def main():
    os.system("clear || cls")
    print()
    print(heading)
    isPassed = False

    with open("./rn.txt", "r") as f:
        last_line = f.readlines()[-1]   

    time.sleep(1)
    print("Last Record: " + last_line)
    print()
    try:
        ts_no = int(input('Enter Test No: '))
    except ValueError:
        os.system("clear || cls")
        print("[!] Please Enter an Integer")
        time.sleep(2)
        main()
    print()
    to_check = input("Does the Robot Passed the Test? [Y/n]: ")
    print()

    if to_check == "Y":
        isPassed = True
    elif to_check == "n" or "N" or "No" or "no":
        isPassed = False
        ask = input("Reason for Failure? ")
    else:
        os.system("clear || cls")
        print("[!] Considering is as Failure")
        time.sleep(3)
        isPassed = False
        print()
        ask = input("Reason for Failure? ")

    if isPassed == True:
        with open("./Finale_Practise_1/rn.txt", "a") as file:
            file.write("\n")
            file.write(ts_no)

        with open("./records.txt", 'a') as file1:

            time_to_complete = float(
                input("Time for Completion of the Task: "))
            calculated_percent = (float(time_to_complete) - 35) / 35 * 100

            if float(round(calculated_percent)) > 0:
                file1.write("\n")
                file1.write("Test No: " + ts_no + " | " + "Test Passed" + " | " +
                            "Time Error Percentage: " + str(round(calculated_percent)) + "%")
                print()
                print("Record Saved")
                time.sleep(2)

            elif float(round(calculated_percent)) == 0:
                file1.write("\n")
                file1.write("Test No: " + ts_no + " | " +
                            "Test Passed" + " | " + "No Error Found!")
                print()
                print("Record Saved")
                time.sleep(2)

            else:
                file1.write("\n")
                file1.write("Test No: " + ts_no + " | " +
                            "Test Passed" + " | " + "Faster Than Average Time")
                print()
                print("Record Saved")
                time.sleep(2)

    elif isPassed == False:
        with open("./rn.txt", "a") as file:
            file.write("\n")
            file.write(ts_no)

        with open("./records.txt", 'a') as file1:
            file1.write("\n")
            file1.write("Test No: " + ts_no + " | " +
                        "Test Failed" + " | " + "Reason: " + ask)
            print()
            print("Record Saved")
            time.sleep(2)
    else:
        os.system("clear || cls")
        print("Achivement Unlocked: How Did You Get Here?")
        time.sleep(5)
        exit(0)

    print()
    continue_ = input("Enter More Records: [Y/n]: ")
    if continue_ == "Y":
        main()
    else:
        print()
        print("[!] Considering is as a No")
        time.sleep(3)
        exit(0)


class intialize:
    while True:
        os.system("clear || cls")
        print(heading)
        time.sleep(3)
        main()
