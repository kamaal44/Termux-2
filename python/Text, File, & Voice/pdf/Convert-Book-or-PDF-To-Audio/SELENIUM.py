#!/usr/bin/python
import os
import glob
import urllib

import threading
import datetime
from time import strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = os.getcwd()

#Read the comment on line 63 it's important
def convert_to_audio(file_,voice_name):
    driver = webdriver.PhantomJS()
    driver.get('http://www.fromtexttospeech.com/')
    #wait for it to open
    driver.implicitly_wait(10)
    print(voice_name+" textfile file open")
    f=open(file_)
    #format 
    driver.execute_script('document.getElementById("input_text").value="%s"' %f.read().replace("\n"," ").replace("\""," "))
   
    f.close()
    voice= {"Alice":0,
            "Daisy":1,
            "George":2,
            "Jenna":3,
            "John":4}
    #select the voice chosen when this was called
    driver.execute_script('document.getElementById("voice").selectedIndex=%d;' %voice[voice_name])    
    driver.find_element_by_id("create_audio_file").click();
    print("trying to join file")
    try:
        #wait until it crates an mp3
        element = WebDriverWait(driver, 1e10).until(
            EC.presence_of_element_located((By.ID, "single1"))
        )
    finally:
    	print("file made")
        #get href so that selenium can read it
        driver.execute_script('''
            if(document.getElementsByClassName("input_text")[0].innerHTML.indexOf("Download audio file")>-1)
            {
                for(i=0; i<document.getElementsByTagName("a").length;i++)
                {
                    if(document.getElementsByTagName("a")[i].innerHTML.indexOf("Download audio file")>-1)//if it is finnihed
                     //."link" is a made up attribute that so i can store the href for later extraction
                        document.getElementById("single1").link=document.getElementsByTagName("a")[i].href;
                    
                }
 
            }
        ''')
        print("trying to download")
        #get value of link from attribute i made up
        el=driver.find_element_by_id("single1")
        link=el.get_attribute("link")
        print("downloading %s from %s" %(file_.split("/")[-1], link))
        print(strftime("%Y-%m-%d %H:%M:%S"))
        #download it! : D
        urllib.urlretrieve(link, filename=file_.replace(".txt","")+"."+voice_name+".mp3")
        driver.close()
          

#The methods below will convert the text file into multiple voices: the result is more versitle but is Significantly longer 
#I would recommend finding one voice you prefer and only converting the text into that voice
for text_file in glob.glob(os.path.join(path, '*.txt')):
    convert_to_audio(text_file,"Alice")
    convert_to_audio(text_file,"Daisy")
    convert_to_audio(text_file,"George")
    convert_to_audio(text_file,"Jenna")
    convert_to_audio(text_file,"John")
 


