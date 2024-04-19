import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import re

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

logger = logging.getLogger()
# thumb = os.environ.get("THUMB")
# if thumb.startswith("http://") or thumb.startswith("https://"):
#     getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
#     thumb = "thumb.jpg"

@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **Careerwill Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/mendax** to continue..\n\n"
                                     "Bot made by **𝐌𝐞𝐧𝐝𝐚𝐱™❤️**" )

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = (
    f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
)
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

url="https://elearn.crwilladmin.com/api/v1/"

info= {
 "deviceType":"android",
    "password":"",
    "deviceModel":"Asus ASUS_X00TD",
    "deviceVersion":"Pie(Android 9.0)",
    "email":"",
}

@bot.on_message(filters.command(["mendax"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False

    url = "https://elearn.crwilladmin.com/api/v1/login-other"
    data = {
        "deviceType": "android",
        "password": "",
        "deviceIMEI": "08750aa91d7387ab",
        "deviceModel": "Realme RMX2001",
        "deviceVersion": "R(Android 11.0)",
        "email": "",
        "deviceToken": "fYdfgaUaQZmYP7vV4r2rjr:APA91bFPn3Z4m_YS8kYQSthrueUh-lyfxLghL9ka-MT0m_4TRtlUu7cy90L8H6VbtWorg95Car6aU9zjA-59bZypta9GNNuAdUxTnIiGFxMCr2G3P4Gf054Kdgwje44XWzS9ZGa4iPZh"
       }
    headers = {
        "Host": "elearn.crwilladmin.com",
        "Token": "",
        "Usertype": "",
        "Appver": "1.55",
        "Apptype": "android",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "313",
        "Accept-Encoding": "gzip, deflate",
        "user-agent": "okhttp/5.0.0-alpha.2",
        'Connection': 'Keep-Alive'
       }
    #proxy_host = ['47.254.153.200:80']
    #proxies = {
     #       'https': proxy_host,
     #       'http': proxy_host,
     #   }
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password** \n or \nSend **TOKEN** like This this:-  **TOKEN**" )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    s = requests.Session()
    if "*" in raw_text:
      data["email"] = raw_text.split("*")[0]
      data["password"] = raw_text.split("*")[1]
      await input1.delete(True)
      #s = requests.Session()
      response = s.post(url = url, headers=headers, json=data, timeout=10)
      if response.status_code == 200:
          data = response.json()
          token = data["data"]["token"]
          await m.reply_text(token)
      else:
           await m.reply_text("go back to response")
      #token = "4ffd1627981589c0a1261f7a114fbbf8bc87c6d9"
      await m.reply_text(f"```{token}```")
    else:
      token = raw_text
    html1 = s.get("https://elearn.crwilladmin.com/api/v1/comp/my-batch?&token=" + token).json()
    topicid = html1["data"]["batchData"]
    cool=""
    for data in topicid:
        instructorName=(data["instructorName"])
        FFF="**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa =f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
        #aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}')>4096:
            await m.reply_text(aa)
            cool =""
        cool+=aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    html2 = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-topic/"+raw_text2+"?type=class&token="+token).json()
    topicid = html2["data"]["batch_topic"]
    bn = html2["data"]["batch_detail"]["name"]
    vj=""
    for data in topicid:
        tids = (data["id"])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
    vp = ""
    for data in topicid:
        tn = (data["topicName"])
        tns=f"{tn}&"
        if len(f"{vp}{tn}")>4096:
            await m.reply_text(tns)
            vp=""
        vp+=tns
    cool1 = ""
    for data in topicid:
        t_name=(data["topicName"].replace(" ",""))
        tid = (data["id"])
        scraper = cloudscraper.create_scraper()
        ffx = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+tid+"&token="+token).json()
            #ffx = json.loads(html3)
        vcx =ffx["data"]["class_list"]["batchDescription"]
        vvx =ffx["data"]["class_list"]["classes"]
        vvx.reverse()
        zz= len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"

#         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

        if len(f'{cool1}{hh}')>4096:
            await m.reply_text(hh)
            cool1=""
        cool1+=hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
    editable2= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]

            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            #scraper = cloudscraper.create_scraper()
            html4 = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token).content
            ff = json.loads(html4)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff["data"]["class_list"]["batchName"].replace("/ "," ")
            vv =ff["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
                     #lessonName = re.sub('\|', '_', cf)

                    if bcvid.startswith("62"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html6 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html5 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url+"&bcov_auth="+stoken)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    elif bcvid.startswith("63"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html7 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html8 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url1+"&bcov_auth="+stoken1)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    else:
                        link=("https://www.youtube.com/embed/"+bcvid)
                    cc = (f"{lessonName}::{link}")
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{lessonName}:{link}\n")
                    #await m.reply_document(f"{mm }{t_name}.txt")
            except Exception as e:
                await m.reply_text(str(e))
        await m.reply_document(f"{mm }{t_name}.txt")
        #os.remove(f"{mm }{t_name}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            scraper = cloudscraper.create_scraper()
            html7 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token).content
            pdfD=json.loads(html7)
            k=pdfD["data"]["notesDetails"]
            bb = len(pdfD["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{name}:{s}\n")
                    continue
                await m.reply_document(f"{mm }{t_name}.txt")
                    
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]
        
        
            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            
            url3 = "https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token   
            ff = requests.get(url3)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff.json()["data"]["class_list"]["batchName"]
            
            vv =ff.json()["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
#                     lessonName = re.sub('\|', '_', cf)
                    
                
                
                    if bcvid.startswith("62"):
                        try:
                            video_response = requests.get(f"{bc_url}/{bcvid}", headers=bc_hdr)
                            video = video_response.json()
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)

                            surl=requests.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token)
                            stoken = surl.json()["data"]["token"]
                            #print(stoken)

                            link = video_url+"&bcov_auth="+stoken
                            #print(link)
                        except Exception as e:
                            print(str(e))
                        
                    else:
                        link="https://www.youtube.com/embed/"+bcvid
                    # await m.reply_text(link)

                    #editable3= await m.reply_text("**Now send the Resolution**")
                    #input4 = message = await bot.listen(editable.chat.id)
                    #raw_text4 = input4.text

                    cc = f"**{count}) Title :** {lessonName}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}\n\n**Upload By UnityBro✨**"
                    Show = f"**Downloading:-**\n**Title -** ```{lessonName}\n\nQuality - {raw_text4}```\n\n**Url :-** ```{link}```"
                    prog = await m.reply_text(Show)

                    if "youtu" in link:
                        if raw_text4 in ["144", "240", "480"]:
                            ytf = f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]'
                        elif raw_text4 == "360":
                            ytf = 18
                        elif raw_text4 == "720":
                            ytf = 22
                        else:
                            ytf = 18
                    else:
                        ytf=f"bestvideo[height<={raw_text4}]"
                        
                    if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}" "{link}"'
                    else:
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'


                    #cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
                    try:
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd)
                        

                        filename = f"{lessonName}.mp4"
#                         await prog.delete (True)
#                         reply = await m.reply_text("Uploading Video")
                        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:19 -vframes 1 "{filename}.jpg"', shell=True)
    
                        #thumbnail = f"{filename}.jpg"
                        await prog.delete (True)
                        reply = await m.reply_text("Uploading Video")
                        

                        try:
                            if thumb == "no":
                                thumbnail = f"{filename}.jpg"
                            else:
                                thumbnail = thumb
                        except Exception as e:
                            await m.reply_text(str(e))



                        dur = int(helper.duration(filename))
#                         await prog.delete (True)
                        start_time = time.time()
                        await m.reply_video(f"{lessonName}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{lessonName}.mp4")
                        
                        os.remove(f"{filename}.jpg")
                        await reply.delete (True)
                    except Exception as e:
                        await m.reply_text(f"**Video downloading failed ❌**\n{str(e)}")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")
    
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            url5=requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token)
            k=url5.json()["data"]["notesDetails"]
            bb = len(url5.json()["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                 
                    
                    ww = f"**{count1}) File Name :- **{name}\n**Date : **{xi}\n{bn}"
                    show2 = f'**Downloading :-**\n\n**Link :** ```{s}```'
                    prog2 = await m.reply_text(show2)
                    cmd2=f'yt-dlp -o "{name}.pdf" "{s}"'
                    try:
                        download_cmd2 = f"{cmd2} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd2)
                        await m.reply_document(f'{name}.pdf', caption=ww)

                        count1+=1
                        await prog2.delete (True)
                        os.remove(f'{name}.pdf')
                        time.sleep(2)
                        
                    except Exception as e:
                        await m.reply_text(f"**PDF downloading failed ❌**\n{str(e)}")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("✅Done Mendax Bro😂")
    
                    
                
                
        
        
        





        
                
        














bot.run()
