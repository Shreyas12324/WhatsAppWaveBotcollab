from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static



import csv
import re
import pywhatkit
import pyautogui
import time

def send_mess(mess,phone):
    pywhatkit.sendwhatmsg_instantly(phone, mess)
    pyautogui.press("enter")

def send_other_mess(mess):
    pyautogui.write(mess)
    pyautogui.press("enter")

def send_messages(L,phone):
   send_mess(L[0],phone)
   pyautogui.press("enter")
   time.sleep(2)
   pyautogui.press("enter")
   time.sleep(2)
   pyautogui.press("enter")

   for i in range(1,len(L)):
       send_other_mess(L[i])

   print("Messages sent successfully ! Script By Kushal Ajwani")

def extract_phone_numbers(csv_file_path):
    phone_numbers = []

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            phone_numbers.append(row[1])

    return phone_numbers


def index(request):
    return render(request,"index.html")

def send(request):
    text = request.GET.get("message")
    Messages = text.split(";")
    csv_file_path = 'staticfiles/file.csv'
    result = extract_phone_numbers(csv_file_path)
    for i in result:
        send_messages(Messages,i)
    return HttpResponse("Sending messages...")

