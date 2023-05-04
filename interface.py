import tkinter as tk
import csv
import cv2
from pyzbar.pyzbar import decode
import time


HEIGHT = 50
WIDTH = 400
main_window_flag = True
recording_window_flag = True
scanning = True


# def stop_scanning():
#     global scanning
#     scanning = False


with open("names.txt", "r") as target:
    final = csv.reader(target)
    data = list(final)


def show_sign_up_menu():
    sign_up_menu = tk.Toplevel()
    canv = tk.Canvas(sign_up_menu, height=HEIGHT, width=WIDTH)
    canv.grid(column=1, row=1)
    sign_up_menu.resizable(False, False)


def show_upload_window():
    upload_window = tk.Toplevel()
    canv = tk.Canvas(upload_window, height=HEIGHT, width=WIDTH)
    canv.grid(column=1, row=1)
    upload_window.resizable(False, False)


def view_sheets():
    show_sheets_window = tk.Toplevel()
    canv = tk.Canvas(show_sheets_window, height=HEIGHT, width=WIDTH)
    canv.grid(column=1, row=1)
    show_sheets_window.resizable(False, False)


def start_scan():
    cap = cv2.VideoCapture(0)

    # address = 'https://192.168.198.105:8080/video'
    # cap.open(address)

    cap.set(3, 640)
    cap.set(4, 480)

    scanned = []

    current = time.time()

    while True:
        success, img = cap.read()
        for barcode in decode(img):
            scanned.append(barcode.data)
        cv2.imshow("result", img)
        cv2.waitKey(1)
        scanned = list(dict.fromkeys(scanned))
        print(scanned)


def show_recording_window():
    global recording_window_flag
    if recording_window_flag:
        record_user_window = tk.Toplevel()
        start_scan_button = tk.Button(record_user_window, text="Start scan", command=start_scan)
        start_scan_button.grid(column=1, row=1)

        # stop_scan_button = tk.Button(record_user_window, text="Stop scan", command=stop_scanning())
        # stop_scan_button.grid(column=2, row=4)

        add_checkbox = tk.Checkbutton(record_user_window, text="Add")
        add_checkbox.grid(column=2, row=1)

        column_label = tk.Label(record_user_window, text="Column")
        column_label.grid(column=0, row=3)
        column_entry = tk.Entry(record_user_window)
        column_entry.grid(column=1, row=3)

        text_label = tk.Label(record_user_window, text="Text")
        text_label.grid(column=2, row=3)
        text_entry = tk.Entry(record_user_window)
        text_entry.grid(column=3, row=3)

        canv = tk.Canvas(record_user_window, height=HEIGHT, width=WIDTH)
        canv.grid(column=1, row=2)
        canv = tk.Canvas(record_user_window, height=HEIGHT, width=WIDTH)
        canv.grid(column=1, row=4)
        record_user_window.resizable(False, False)
        recording_window_flag = False


def show_welcome_user_window():
    global main_window_flag

    if main_window_flag:

        if username_entry.get() == "Joe" and password_entry.get() == "908":

            welcome_user_window = tk.Toplevel()

            canv = tk.Canvas(welcome_user_window, height=HEIGHT, width=WIDTH)
            canv.grid(column=1, row=1)

            record_button = tk.Button(welcome_user_window, text="Record", command=show_recording_window)
            record_button.grid(column=0, row=0)

            view_button = tk.Button(welcome_user_window, text="View", width=5, command=view_sheets)
            view_button.grid(column=0, row=1)

            upload_button = tk.Button(welcome_user_window, text="Upload", command=show_upload_window)
            upload_button.grid(column=0, row=2)

            sign_up_button = tk.Button(welcome_user_window, text="Sign up a new member", command=show_sign_up_menu)
            sign_up_button.grid(column=1, row=1)
            welcome_user_window.resizable(False, False)
            main_window_flag = False
            # welcome_user_window.protocol("WM_DELETE_WINDOW", on_closing)

        else:
            not_member_menu = tk.Tk()
            not_member_menu.title("Attendance manager")
            canv = tk.Canvas(not_member_menu, height=10, width=300)
            canv.pack()
            text_label = tk.Label(not_member_menu, text="You're not a member")
            text_label.pack()
            canv = tk.Canvas(not_member_menu, height=10, width=300)
            canv.pack()


main_window = tk.Tk()

main_window.title("Attendance Management System")

canvas = tk.Canvas(main_window, height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=1)

main_window.resizable(False, False)

username_label = tk.Label(text="username")
username_label.grid(column=1, row=2)
username_entry = tk.Entry(width=30)
username_entry.grid(column=1, row=3)

password_label = tk.Label(text="password")
password_label.grid(column=1, row=4)
password_entry = tk.Entry(width=30, show="*")
password_entry.grid(column=1, row=5)

button = tk.Button(main_window, text="LOGIN", bg='White', fg='Black',
                   command=show_welcome_user_window)
button.grid(column=1, row=6)

canvas = tk.Canvas(main_window, height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=7)

main_window.mainloop()
