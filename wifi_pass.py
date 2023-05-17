# -*- coding: utf-8 -*-
"""
Created on Mon May  15 11:27:18 2023
@author: Muhammad Ahmed Ansari
"""

# code for getting wifi password from windows
import subprocess

def get_wifi_pass():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in output if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    return 'Current connected wifi password -> '+results[0]

p = get_wifi_pass()
print(p)

