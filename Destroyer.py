import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, ALIVE_NAME, USERNAME, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20  
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleventh = STRING11
twelvth = STRING12
thirtenth = STRING13
forteenth = STRING14
fifteenth = STRING15
sixteenth = STRING16
seventeenth = STRING17
eighteenth = STRING18
ninteenth = STRING19
twenty = STRING20


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_Destroyer():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await idk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await idk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await ydk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await wdk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await hdk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await sdk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await adk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await adk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await bdk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await cdk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await ddk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await edk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await edk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
          
          
          if eleventh:
        session_name = str(eleventh)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await vkk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelvth:
        session_name = str(twelvth)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await kkk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirtenth:
        session_name = str(thirtenth)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await lkk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forteenth :
        session_name = str(forteenth)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await mkk(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifteenth:
        session_name = str(fifteenth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await sid(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await sid(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sixteenth:
        session_name = str(sixteenth)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await shy(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await shy(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seventeenth:
        session_name = str(seventeenth)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await aan(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await aan(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eighteenth:
        session_name = str(eighteenth)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await ake(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await ake(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if ninteenth:
        session_name = str(ninteenth)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await eel(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await eel(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if twenty:
        session_name = str(twenty)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@YAMLOKOFFICIAL"))
            await khu(functions.channels.JoinChannelRequest(channel="@LONELY_MUSIC_N_STATUS"))
            await khu(functions.channels.JoinChannelRequest(channel="@TEAM_DESTROYER"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
