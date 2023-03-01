import pyautogui #do a pip install
import ctypes
import time
import random
import pandas as pd
from DriveApi import *
from GmailApi import *

df = pd.read_excel('file.xlsx', sheet_name='ORGANIZED', header=None, skiprows=1)

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

class TeamMember:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.fileName = name + ".pdf"

# Define a function to create TeamMember instances from a row of data
def create_team_member(row, index):
    name_col = 3 + (index - 1) * 2
    email_col = name_col + 1
    return TeamMember(row[name_col], row[email_col], f"file{index}.txt")

# Define a function to create Team instances from a group of rows of data
def create_team(row):
    team_name = row.iloc[0, 1]
    members = []
    for i in range(4):
        name_col = 3 + i * 2
        email_col = name_col + 1
        if not pd.isna(row.iloc[0, name_col]):
            members.append(TeamMember(row.iloc[0, name_col], row.iloc[0, email_col]))
    return Team(team_name, members)

# Group the DataFrame by team name and apply the create_team function to each group



# omar = Person("Omar", "1bakromar@gmail.com", "The Rizzlers")
    
users = []

#a dictionary with each action and a tuple attached to it
actions = {
    1:None, #changeName
    2:None, #changeTeam
    3:None, #White Space
    4:None, #"Change File Name"
    5:None, #"Figma Button"
    6:None, #File
    7:None, #Export To PDF
}
teams = df.groupby(1).apply(create_team).tolist()

def readxlsx():
    
    for team in teams:
        print(f"Team Name: {team.name}")
        for member in team.members:
            print(f"  Member Name: {member.name}")
            print(f"  Member Email: {member.email}")


#gets the positoins of where to click
def getPositions():
    for i in range(1,8): #should be 5
        print("On", i)
        time.sleep(2)
        while(True):
            if ctypes.windll.user32.GetKeyState(0x01)!=0 and ctypes.windll.user32.GetKeyState(0x01)!=1:
                actions[i] = pyautogui.position()
                print(actions[i])
                break
        time.sleep(1)

    print(actions)

def generateCertificates():
    for team in teams:
        for member in team.members:
            pyautogui.moveTo(actions[1][0], actions[1][1])
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(member.name)

            pyautogui.moveTo(actions[2][0], actions[2][1])
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(team.name)
            
            pyautogui.moveTo(actions[3][0], actions[3][1])
            pyautogui.click(button='left')
            pyautogui.click(button='left')

            pyautogui.moveTo(actions[4][0], actions[4][1])
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(member.name)

            pyautogui.moveTo(actions[5][0], actions[5][1])
            pyautogui.click(button='left')

            pyautogui.moveTo(actions[6][0], actions[6][1])
            pyautogui.click(button='left')

            pyautogui.moveTo(actions[7][0], actions[7][1])
            pyautogui.click(button='left')


readxlsx()
# getPositions()
# generateCertificates()
# uploadFile(teams)
files = retrieveLink(teams)
sendEmail(teams, files)
