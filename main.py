import pyautogui
import keyboard

msg = "woyyyyy"
name = "Broo"

# posisi dari file check posisi
pyautogui.moveTo(1180,733)

pyautogui.click()
pyautogui.write(message=f"Hi.. {name} {msg}")
keyboard.press("enter")
