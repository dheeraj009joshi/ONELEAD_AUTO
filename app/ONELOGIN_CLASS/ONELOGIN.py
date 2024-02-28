import csv
import datetime
import os
import re
import time 
import datetime
import threading
# from onelogin_class import onLogin
#from multiprocessing impoCrt Process, Manager
from functools import partial
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from app.ONELOGIN_CLASS import config
import pandas as pd 
from selenium.webdriver.edge.service import Service


from app.ONELOGIN_CLASS.function import calculate_days_difference, time_difference_in_minutes
class onLogin:

    def __init__(self):
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument("headless")
        options.add_argument("disable-gpu")
       
        self.driver=webdriver.Edge(options=options)
        # self.driver=webdriver.Edge()
        print(self.driver.capabilities)
    def login_to_oneLogin(self,username=config.ONELOGIN_USERNAME,password=config.ONELOGIN_PASSWORD):
        self.driver.get("https://group1auto.onelogin.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[2]/form/div/div[3]/div/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[2]/form/div/div[3]/div/button').click()
        verify=0
        print("waiting for otp verification")
        while verify==0:
            try:
                self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/button').click()
                verify=1
            except:
                pass
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/p[2]/button').click()
        time.sleep(10)
        print("login done")
        


    def open_eleads_oneLogin(self):
        all_oprions_after_login=self.driver.find_elements(By.XPATH,'//*[@id="apps-view-container"]/div[2]/div/div/div/div/a/div/div[1]/div')
        for opt in all_oprions_after_login:
            if opt.text=='ELEAD SSO SAML':
                opt.click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # driver.close()
        try:
            # driver.switch_to.window(driver.window_handles[2])
            # driver.close()
            self.driver.switch_to.window(self.driver.window_handles[2])
        except:
            pass 
    

    def open_outlook_oneLogin(self):
        print("Opening outlook")
        all_oprions_after_login=self.driver.find_elements(By.XPATH,'//*[@id="apps-view-container"]/div[2]/div/div/div/div/a/div/div[1]/div')
        for opt in all_oprions_after_login:
            if opt.text=='OWA Outlook Web Mail' or opt.text =='Outlook for Office 365 OWA Link':
                opt.click()
        time.sleep(10)  
        self.driver.switch_to.window(self.driver.window_handles[1])
        # driver.close()
        try:
            # driver.switch_to.window(driver.window_handles[2])
            # driver.close()
            self.driver.switch_to.window(self.driver.window_handles[2])
        except:
            pass 


    def get_otp_from_outlook_for_automotivemastermind(self):
        print("looking for otp")
        List_emails=self.driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/span')
        for email in List_emails:
            print(email.text)
            if email.text=="Login Authorization":
                email.click()
                time.sleep(5)
                otp_pattern = r'\b\d{6}\b'
                otp_match = re.search(otp_pattern, self.driver.find_element(By.XPATH,'/html').text)
                # otp_match =  self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr/td/h1').text
                print(otp_match)
                if otp_match:
                    otp = otp_match.group()
                    print("Found OTP:", otp)
                # otp=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div[3]/div/div[1]/div[2]/div[7]/div/div/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div[1]/div[3]/div[3]/div[1]/div/div/table[2]/tbody/tr/td[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr/td/h1').text
                    print("otp :- ",otp)
                    return otp

    def get_otp(self):
        self.login_to_oneLogin()
        self.open_outlook_oneLogin()
        otp=self.get_otp_from_outlook_for_automotivemastermind()
        return otp
    

    def search_lead(self,search_keyword):
        self.driver.switch_to.window(self.driver.window_handles[1])
        # driver.close()
        try:
            # driver.switch_to.window(driver.window_handles[2])
            # driver.close()
            self.driver.switch_to.window(self.driver.window_handles[2])
        except:
            pass 
        search_field=self.driver.find_element(By.XPATH,'//*[@id="txtQuickSearch"]')
        search_field.clear()
        search_field.send_keys(search_keyword)
        time.sleep(0.5)
        sear_button_click=self.driver.find_element(By.XPATH,'//*[@id="tdSearchImage"]').click()
        time.sleep(0.3)
        # frame=driver.find_element(By.XPATH,'//*[@id="searchResultsFrame"]')
        self.driver.switch_to.frame('Main')
        time.sleep(0.3)
        frame=self.driver.find_element(By.XPATH,'//*[@id="searchResultsFrame"]')
        self.driver.switch_to.frame(frame)
        time.sleep(0.3)
        row1=self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]')
        match_percent=row1.find_element(By.XPATH,'td[2]').text.replace("%","")
        # print(match_percent)
        if float(match_percent)==100:
            name_lead=row1.find_element(By.XPATH,'td[3]/a').text
            lead_data_url=row1.find_element(By.XPATH,'td[3]/a').get_attribute("onclick")
            lead_ids=lead_data_url.replace('$.popupOppty','').replace(";","").replace("(","").replace(")","").replace("'","").split(",")
            lead_urll=f'https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID={lead_ids[0]}&lDID={lead_ids[1]}'
            return {"Match":True,"name":name_lead,"Url":lead_urll}
        else:
            {"Match":False}
                 

    def send_email_via_html(self,url,email_subject,email_body):
            self.driver.get(url)
            time.sleep(5)
            main_window = self.driver.current_window_handle
            try:
                all_lebal_url=self.driver.find_element(By.XPATH,'//html/body/form/div[3]/table[1]/tbody/tr[1]/td[2]/a').click()
                # all_lebal_urls[email_index].click()
                time.sleep(5)
                # main_window = driver.current_window_handle
                popup_window = None

                # Iterate through all available windows and find the popup window
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        popup_window = handle

                # Switch the focus to the popup window
                pop=self.driver.switch_to.window(popup_window)
                email_available_or_not=self.driver.find_element(By.XPATH,'//*[@id="szTo"]').get_attribute("value")
                print(email_available_or_not)
                print("")
                print("")
                print("")
                if email_available_or_not :
                    name=self.driver.find_element(By.XPATH,"/html/body/form[2]/table[1]/tbody/tr[2]/td[1]")
                    print(f"name= {name.text}")
                    # emailed_user.write(name.text+"\n")
                    Name=name.text.split(":")[-1]
                    subject_text=email_subject
                    body_text=f"{email_body}"
                    subject=self.driver.find_element(By.XPATH,'//*[@id="szSubject"]')
                    subject.click()
                    subject.send_keys(subject_text)
                    subject.click()
                    source=self.driver.find_element(By.XPATH,'//*[@id="cke_18_label"]')
                    source.click()
                    time.sleep(2)
                    body=self.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/textarea')
                    # textarea = driver.find_element("xpath", "//textarea[@id='your_textarea_id']")

                    # Use JavaScript to set the value of the textarea
                    new_text = "Your new text goes here."
                    self.driver.execute_script("arguments[0].value = arguments[1]", body, body_text)
                    # body.click()
                    # time.sleep(0.5)
                    # body.clear()
                    # time.sleep(0.5)
                    # body.send_keys(body_text)
                    # print("body text is written down")
                    # body.click()
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,'//*[@id="btnSend"]').click()
                    print("Email sent button clicked")
                    time.sleep(2) 
            except Exception as Error_in_sending_mail:
                print(f"got error in mail send :- {Error_in_sending_mail}")
        
            self.driver.switch_to.window(main_window)
  


    def send_email_via_text(self,url,email_subject,email_body):
            self.driver.get(url)
            time.sleep(5)
            main_window = self.driver.current_window_handle
            try:
                all_lebal_url=self.driver.find_element(By.XPATH,'//html/body/form/div[3]/table[1]/tbody/tr[1]/td[2]/a').click()
                # all_lebal_urls[email_index].click()
                time.sleep(5)
                # main_window = driver.current_window_handle
                popup_window = None

                # Iterate through all available windows and find the popup window
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        popup_window = handle

                # Switch the focus to the popup window
                pop=self.driver.switch_to.window(popup_window)
                email_available_or_not=self.driver.find_element(By.XPATH,'//*[@id="szTo"]').get_attribute("value")
                print(email_available_or_not)
                print("")
                print("")
                print("")
                if email_available_or_not :
                    name=self.driver.find_element(By.XPATH,"/html/body/form[2]/table[1]/tbody/tr[2]/td[1]")
                    print(f"name= {name.text}")
                    # emailed_user.write(name.text+"\n")
                    Name=name.text.split(":")[-1]
                    subject_text=email_subject
                    body_text=f"{email_body}"
                    subject=self.driver.find_element(By.XPATH,'//*[@id="szSubject"]')
                    subject.click()
                    subject.send_keys(subject_text)
                    subject.click()
                    frame_for_body=self.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
                    self.driver.switch_to.frame(frame_for_body)
                    time.sleep(2)
                    body=self.driver.find_element(By.XPATH,'/html/body')
                    body.click()
                    body.send_keys(body_text)
                    body.click()
                    self.driver.switch_to.default_content()
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,'//*[@id="btnSend"]').click()
                    time.sleep(4)
                    print("Email sent button clicked")
                    time.sleep(2) 
            except Exception as Error_in_sending_mail:
                print(f"got error in mail send :- {Error_in_sending_mail}")
        
            self.driver.switch_to.window(main_window)
  





    def send_message(self,url,message_text):
            self.driver.get(url)
            time.sleep(5)
            main_window = self.driver.current_window_handle
            try:
                text_OPTIO= self.driver.find_element(By.XPATH,'//*[@id="textSingleCustomerChat"]').click()
            
                time.sleep(5)
                popup_window = None

                # Iterate through all available windows and find the popup window
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        popup_window = handle

                name=self.driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[2]/td[3]').text
                print(name)
                pop=self.driver.switch_to.window(popup_window)
                
                
                # # all_color urls 
                # yellow :- https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=5754493&lDID=19517661&loc=ADVN
                # green :- https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=20750979&lDID=19664718&loc=ADVN
                # grey:- https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=5748052&lDID=19423018&loc=ADVN
                Text_message=message_text
                try:
                    try:
                        
                        # For green color 

                        
                        text_area=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[4]/textarea[1]')
                        text_area.click()
                        text_area.send_keys(Text_message)
                        text_area.click()
                        time.sleep(2)
                        send_btn=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[5]/div')
                        send_btn.click() 
                    
                    except:
                        # For yellow color   
                        type_messagr=self.driver.find_element(By.XPATH,'//*[@id="react-app"]/div/div[2]/div[2]/div/div[2]/div[2]/div').click()
                        time.sleep(5)                               
                        # select_custom=driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[2]').click()
                        select_default=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[3]').click()
                        time.sleep(2)
                        # text_area=driver.find_element(By.XPATH,'//*[@id="optin-preview-container"]/textarea')
                        # text_area.click()
                        # text_area.send_keys(Text_message)
                        # text_area.click()
                        send_button=self.driver.find_element(By.XPATH,'//*[@id="react-app"]/div/div[2]/div[2]/div/div[2]/div[4]/button[2]')
                        send_button.click()
                                
                except Exception as e :
                    print(e)
                
            except Exception as Error_in_sending_mail:
                print(f"got error in mail send :- {Error_in_sending_mail}")
            
            self.driver.switch_to.window(main_window)





    def close_all_extra_tabe_and_windows(self):
        main_window_handle = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        for window_handle in all_window_handles:
        # Switch to the window
            self.driver.switch_to.window(window_handle)

            # Close the window if it is not the main window
            if window_handle != main_window_handle:
                self.driver.close()

        # Switch back to the main window
        self.driver.switch_to.window(main_window_handle)
        pass

    def get_lead_details( lead_urls, output_file):

        
        a=onLogin() 
        
        a.login_to_oneLogin() 
        driver=a.driver
        
        all_oprions_after_login=driver.find_elements(By.XPATH,'//*[@id="apps-view-container"]/div[2]/div/div/div/div/a/div/div[1]/div')
        for opt in all_oprions_after_login:
            if opt.text=='ELEAD SSO SAML':
                opt.click()
        time.sleep(10)   
        driver.switch_to.window(driver.window_handles[1])
        main_window_handle = driver.current_window_handle
        all_window_handles = driver.window_handles
        for window_handle in all_window_handles:
        # Switch to the window
            driver.switch_to.window(window_handle)

            # Close the window if it is not the main window
            if window_handle != main_window_handle:
                driver.close()

        # Switch back to the main window
        driver.switch_to.window(main_window_handle)
        try:
    # driver.switch_to.window(driver.window_handles[2])
            # driver.close()
            driver.switch_to.window(driver.window_handles[2])
        except:
            pass
        details_leads=open(f"{output_file}","a")
        details_leads.write("Name,cell,email,Created_date,Created_time,vehicle,PrimarySalesPerson,LastDateOf_contact,LastDateOf_contact_time,Number_of_times_SalesPerson_contacted,Number_of_times_customer_contacted,Pending_Replies,Pending_Replies_Text,avg_daily_contacted,sales_status,up_type,source,sub_source,Lead_url\n")
        # f=open(f'all_leade_all_in_one_{datetime.date.today()}.csv','r')
        # import json
        all_urls=lead_urls
      
        batch_size = 100  # You can adjust this value based on your needs

        # all_urls=['https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22831066&lDID=21993180','https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22726119&lDID=21869119']
        # all_urls=['https://group1.eleadcrm.com/evo2/fresh/elead-v45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22895748&lDID=22055520','https://group1.eleadcrm.com/evo2/fresh/eLead-V45/elead_track/NewProspects/OpptyDetails.aspx?lPID=10901982&lDID=22075070','https://group1.eleadcrm.com/evo2/fresh/elead-v45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22841517&lDID=22018748','https://group1.eleadcrm.com/evo2/fresh/elead-v45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22775406&lDID=21927585']
        # all_urls=['https://group1.eleadcrm.com/evo2/fresh/elead-v45/elead_track/NewProspects/OpptyDetails.aspx?lPID=22998940&lDID=22169272']
        count_leads_processed=0
        count_leads_written_in_csv=0

        
        batch_no=1
        url_batches = [all_urls[i:i + batch_size] for i in range(0, len(all_urls), batch_size)]
        try:
            # Process each batch
            for batch in url_batches:
                print("batch no = "+str(batch_no))
                try:
                    for url in batch:
                        try:
                            Lead_url=url
                            # driver.set_page_load_timeout(10)
                            driver.get(url)
                            count_leads_processed+=1
                            print(f"Leads processes :- {count_leads_processed}")
                            # time.sleep(5)
                            vehicle=''
                            PrimarySalesPerson=''
                            try:
                                view_previous_data=driver.find_element(By.XPATH,'//*[@id="OpportunityPanel_ViewPrevOpptyLink"]/span').click()
                                # print("got it ")
                                time.sleep(1)
                                all_oprions_for_sales_statue=driver.find_elements(By.XPATH,'//*[@id="OpportunityPanel_StatusDropdown"]/option')
                                for option in all_oprions_for_sales_statue:
                                        
                                    if option.is_selected():
                                        sales_status=option.text
                                        # print(sales_status)
                                
                                    
                            except:
                            

                                all_oprions_for_sales_statue=driver.find_elements(By.XPATH,'//*[@id="OpportunityPanel_StatusDropdown"]/option')
                                for option in all_oprions_for_sales_statue:
                                    
                                    if option.is_selected():
                                        sales_status=option.text
                                        # print(sales_status)
                                    
                                    
                            opportunity_section_text=driver.find_element(By.XPATH,'//*[@id="OpportunityPanel_ActiveOpptyPanel"]').text
                            try:
                                up_type=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
                            except:
                                up_type=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[2]').text

                            # print("Up_type=  "+up_type)             # /html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[2]
                            try:
                                if "Source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[7]').text:
                                    source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[7]/td[2]').text
                                elif "Source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]').text:
                                    source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
                                else:
                                    source=""
                            except:
                                if "Source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[7]').text:
                                    source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[2]').text
                                elif "Source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[8]').text:
                                    source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[2]').text
                                else:
                                    source=""
                            # print("source=  "+source)
                            try:                   
                                if "Sub-source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]').text:
                                    sub_source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
                                elif "Sub-source" in driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]').text:
                                    sub_source=driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[4]/div[1]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
                                else:
                                    sub_source=""
                            except Exception as e :
                                print(e)
                                pass
                              
                            


                            
                # # # # # # Getting General Details   
                            # print("getting details")
                            try:
                                vehicle=driver.find_element(By.XPATH,'//*[@id="OpportunityPanel_ActiveOpptyPanel"]/table/tbody/tr[2]/td[3]').text.replace("Add Opportunity",'')
                            except:
                                pass
                            try:
                                PrimarySalesPerson=driver.find_element(By.XPATH,'//*[@id="OpportunityPanel_ActiveOpptyPanel"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[1]').text
                            except:
                                pass 
                            name=driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[2]/td[3]').text
                            try:
                                cell=driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[6]/td[2]/div[1]/table/tbody/tr/td[1]').text
                            except:
                                cell=''
                            email=driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[8]/td[2]').text 
                            driver.switch_to.frame("tabsTargetFrame")
                            try:
                                Created=driver.find_element(By.XPATH,'//*[@id="gvOpptyHistory"]/tbody/tr[1]/td[2]').text
                            except:
                                Created=''




                # # # # # # contacted details   
                            Number_of_times_SalesPerson_contacted=0
                            Number_of_times_customer_contacted=0
                            Pending_Reply=False
                            Pending_Reply_text=''
                            all_contacts=driver.find_elements(By.XPATH,'/html/body/form/table/tbody/tr[4]/td/div/div/table/tbody/tr[2]/td/div/table/tbody/tr')
                            # print(len(all_contacts))  #################/html/body/form/table/tbody/tr/td/div/div/table/tbody/tr/td/div/table/tbody/tr/td[5]/div
                            date_of_contacts=[]

                            for i in all_contacts:

                                # print(" i am in the loop ")
                                # Times lead responded
                                try:
                                    
                                    contect_type=i.text.split("\n")[1]
                                    contect_outcome=i.text.split("\n")[2]
                                    # print("typr_contacted ="+contect_type)
                                    if 'Read Email' in contect_type or (contect_type=='Text Message' and contect_outcome == "Received"):
                                        Number_of_times_customer_contacted+=1
                                except:
                                    pass


                                # Times SalesPErson contacted
                                try:
                                    # print(i.find_element(By.XPATH,"td[6]").text)
                                # print("sales person contact ="+ i.text.split('\n')[3])
                                    aa=i.find_element(By.XPATH,"td[6]").text.split(",")[0]
                                    # print(aa)
                                    if aa==PrimarySalesPerson.split(",")[0]:
                                        date_of_contacts.append((i.text).split("\n")[0])
                                        Number_of_times_SalesPerson_contacted+=1
                                except:
                                    pass
                            



                            try:
                                # print(" i am inside the true false section ")
                                contect_type=all_contacts[1].text.split("\n")[1]
                                contect_outcome=all_contacts[1].text.split("\n")[2]
                                # print("typr_contacted ="+contect_type)
                                if 'Read Email' in contect_type or (contect_type=='Text Message' and contect_outcome == "Received"):
                                        Pending_Reply=True
                                        if 'Email' in  contect_type:
                                            # pass
                                            all_contacts[1].find_element(By.XPATH,"td[7]/div/a").click()
                                            time.sleep(2)
                                            main_window = driver.current_window_handle
                                            # print(main_window)
                                            popup_window = None
                                            for handle in driver.window_handles:
                                                if handle != main_window:
                                                    popup_window = handle
                                            pop=driver.switch_to.window(popup_window)
                                            # print("pop up window + "+popup_window)
                                            text=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[1]').text
                                            Pending_Reply_text=text.replace(",",' ').replace('\n',' ')
                                            driver.close()
                                            # print(text)
                                            driver.switch_to.window(main_window)
                                            # print("main window  +"+main_window)
                                            # print("switching to main window")
                                        else:       
                                            Pending_Reply_text=all_contacts[1].find_element(By.XPATH,"td[5]/div").text
                            except:
                                pass

                            
                            


                # # # # # # Last Date of contacted
                            try:
                                LastDateOf_contact=date_of_contacts[0]
                            except:
                                LastDateOf_contact=''


                # # # # # #  Average contacted to a person( Lead)
                            try:
                                total_days_after_creation=calculate_days_difference(Created.split(" ")[0])
                                avg_daily_contacted=len(all_contacts)/total_days_after_creation
                            except:
                                avg_daily_contacted=0






                # # # # # # validating the data and adding it to file
                            if vehicle !='' or PrimarySalesPerson !='':
                                # print("OPPORTUNITY available")
                                # print(name)
                                # print(cell)
                                # print(email)
                                # print(vehicle)
                                # print(PrimarySalesPerson)
                                # print(LastDateOf_contact)
                                # print(Number_of_times_SalesPerson_contacted)
                                # print(Number_of_times_customer_contacted)
                                # print(Pending_Reply)
                                # print(Pending_Reply_text)
                                vehicle=vehicle.replace("\n"," ")
                                PrimarySalesPerson=PrimarySalesPerson.replace(","," ")
                                formatted_avg_daily_contacted = "{:.2f}".format(avg_daily_contacted)
                                # print(formatted_avg_daily_contacted)
                                # print( "testing the data ")
                                # print(Created.split(" ")[0])
                                # print(Created.split(" ")[1]+" "+Created.split(" ")[2])
                                try:
                                    Lase_date_contact_date=LastDateOf_contact.replace("keyboard_arrow_down ",'').split(" ")[0]
                                    Lase_date_contact_date_time=LastDateOf_contact.replace("keyboard_arrow_down ",'').split(" ")[1]+" "+LastDateOf_contact.replace("keyboard_arrow_down ",'').split(" ")[2]
                                except:
                                    Lase_date_contact_date=''
                                    Lase_date_contact_date_time=''

                                
                                details_leads.write(f'{name.replace(","," ")},{cell},{email},{Created.split(" ")[0]},{Created.split(" ")[1]+" "+Created.split(" ")[2]},{vehicle},{PrimarySalesPerson},{Lase_date_contact_date},{Lase_date_contact_date_time},{Number_of_times_SalesPerson_contacted},{Number_of_times_customer_contacted},{Pending_Reply},{Pending_Reply_text},{formatted_avg_daily_contacted},{sales_status},{up_type},{source},{sub_source},{Lead_url}'+'\n')
                                count_leads_written_in_csv+=1
                                print(f"Leads written in csv :- {count_leads_written_in_csv}")
                            # time.sleep(5)    
                        except Exception as e :
                            driver.back()
                            print(e)
                            pass
                    # Execute JavaScript to clear local storage
                    driver.execute_script("window.localStorage.clear();")
                    driver.execute_script("window.sessionStorage.clear();")
                    print("local storage cleared")
                    batch_no+=1


                except TimeoutException:
                        print("Timed out waiting for element to be present. Switching to new tab.")
                        time.sleep(10)
                        driver.execute_script("window.localStorage.clear();")
                        driver.execute_script("window.sessionStorage.clear();")
                        print("local storage cleared")

                        driver.execute_script("window.open();")
                        driver.switch_to.window(driver.window_handles[-1])
                        
                        print("new tab opened")
                        time.sleep(5)
                        # Switch to the new tab
                        driver.switch_to.window(driver.window_handles[-2])
                        driver.close()
                        # Switch back to the new tab
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(3)
                        driver.get(url)
                except Exception as err:
                        print(err)
                        pass
                    
        except Exception as err:
            print(err)   
            pass    

    def multiprocess_leads_data(self, all_urls):
        url_groups = [all_urls[i:i + 1000] for i in range(0, len(all_urls), 1000)]
        threads = []

        for i, url_group in enumerate(url_groups):
            output_file_path = f"output_files/leads_data/output{i}.csv"
            thread = threading.Thread(target=onLogin.get_lead_details, args=(url_group, output_file_path))
            threads.append(thread)

        for thread in threads:
            thread.start()
            time.sleep(30)  # Adjust the sleep duration as needed

        for thread in threads:
            thread.join()

        # Access results from the dictionary
        print("Leads task completed")



    def  get_tracking_info( Tracking_Name, lead_urls, output_file):
        a=onLogin() 
        a.login_to_oneLogin()
        a.open_eleads_oneLogin() 
        driver=a.driver

        f=open(output_file,'a',encoding='utf-8')
        f.write("Lead_Url,Created_Date,Created_Time,Time_Assigned,Delay_Assigned,Person_Assigned,Num_Actions,Is_Assigned,Is_Texted,Is_Appointment,Is_Sold\n")
        for lead_url in lead_urls:
            driver.get(lead_url)
            time.sleep(2)
            try:
                PrimarySalesPerson=driver.find_element(By.XPATH,'//*[@id="OpportunityPanel_ActiveOpptyPanel"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[1]').text
            except:
                pass 
            name=driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[2]/td[3]').text
            try:
                cell=driver.find_element(By.XPATH,'//*[@id="CustomerAjaxPanel"]/table/tbody/tr[6]/td[2]/div[1]/table/tbody/tr/td[1]').text
            except:
                cell=''

            driver.switch_to.frame("tabsTargetFrame")
            createdDate=''
            createdTime=''
            try:
                Created=driver.find_element(By.XPATH,'//*[@id="gvOpptyHistory"]/tbody/tr[1]/td[2]').text.split(" ")
                createdDate=Created[0]
                createdTime=" ".join(Created) 
            except:
                Created=''

            all_contacts=driver.find_elements(By.XPATH,'/html/body/form/table/tbody/tr[4]/td/div/div/table/tbody/tr[2]/td/div/table/tbody/tr')
            date_of_contacts=[]
            Number_of_times_SalesPerson_contacted=0
            isTexted=False
            for i in all_contacts:
                try:
                    if cell !='':
                        contactType=i.text.split("\n")[1]
                        contactedBy=i.find_element(By.XPATH,"td[6]").text.split(",")[0]
                        if contactType=='Text Message' and contactedBy==Tracking_Name.split(" ")[-1]:
                            isTexted=True
                except:
                    pass
                try:
                    aa=i.find_element(By.XPATH,"td[6]").text.split(",")[0]
                    if aa==Tracking_Name.split(" ")[-1]:
                        date_of_contacts.append((i.text).split("\n")[0])
                        Number_of_times_SalesPerson_contacted+=1
                except:
                    pass

            # go to audit tabc
            driver.switch_to.default_content()
            time.sleep(2)
            audit_tab_link=driver.find_element(By.XPATH,'//*[@id="liAuditTrail"]').click()
            time.sleep(3)
            driver.switch_to.frame("tabsTargetFrame")
            all_audits_logs=driver.find_elements(By.XPATH,'//*[@id="GridViewAuditTrail"]/tbody/tr')
            print(all_audits_logs)
            isProcessable=False
            isAassigned=False
            timeAssigned=''
            isSold=False
            isAppointmentSet=False
            for log in all_audits_logs:
                try:
            # print(log.find_element(By.XPATH,'td[4]').text)
                    if  log.find_element(By.XPATH,'td[3]').text==Tracking_Name and log.find_element(By.XPATH,'td[4]').text=='Add to Sales Team':
                        isAassigned=True
                        timeAssigned=" ".join(log.find_element(By.XPATH,'td[1]').text.split(" "))
                        isProcessable=True
                        print(" add sales team found",isProcessable)
                        
                    if log.find_element(By.XPATH,'td[3]').text==Tracking_Name and log.find_element(By.XPATH,'td[4]').text=='Change Opportunity Status' and log.find_element(By.XPATH,'td[5]').text=='Set Opportunity from Active/New to Active/Appointment Set':
                        isAppointmentSet=True
                        # timeAssigned=" ".join(log.find_element(By.XPATH,'td[1]').text.split(" "))
                        isProcessable=True
                        print(" Active/Appointment Set",isProcessable)
                    if log.find_element(By.XPATH,'td[3]').text==Tracking_Name and log.find_element(By.XPATH,'td[4]').text=='Change Opportunity Status' and log.find_element(By.XPATH,'td[5]').text=='Set Opportunity from Active/New to Sold/CRM Sold':
                        isAppointmentSet=True
                        # timeAssigned=" ".join(log.find_element(By.XPATH,'td[1]').text.split(" "))
                        isProcessable=True
                        print("  Sold/CRM Sold",isProcessable)
                except Exception as err:
                    # print(err)
                    pass
            DelayAssigned=None
            if isProcessable:
                if  isAassigned:
                    DelayAssigned=time_difference_in_minutes(createdTime,timeAssigned) 
                    if DelayAssigned==False:
                        isAassigned=False
                print(PrimarySalesPerson)
                print(createdDate)
                print(createdTime)
                print(timeAssigned)
                print(DelayAssigned)
                print(date_of_contacts)
                print(Number_of_times_SalesPerson_contacted)
                print(isAppointmentSet)

                f.write(f'{lead_url},{createdDate},{" ".join(createdTime.split(" ")[1:])},{timeAssigned},{DelayAssigned},{PrimarySalesPerson.replace(","," ")},{Number_of_times_SalesPerson_contacted},{isAassigned},{isTexted},{isAppointmentSet},{isSold}\n')

    def multiprocess_tracking_data(self, Tracking_Name,all_urls):
        url_groups = [all_urls[i:i + 1000] for i in range(0, len(all_urls), 1000)]
        threads = []

        for i, url_group in enumerate(url_groups):
            output_file_path = f"output_files/tracking_data/output{i}.csv"
            thread = threading.Thread(target=onLogin.get_tracking_info, args=(Tracking_Name,url_group, output_file_path))
            threads.append(thread)

        for thread in threads:
            thread.start()
            time.sleep(30)  # Adjust the sleep duration as needed

        for thread in threads:
            thread.join()

        # Access results from the dictionary
        print("Tracking task completed")


    

    def combine_csv_files(folder_path, output_filename):
   
        
        f=open(output_filename,'a',encoding="utf-8")
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                f2=open(file_path,'r',encoding="utf-8")
                for i in f2.readlines():
                    f.write(i)


               

        print(f"Combination complete. Output saved as '{output_filename}'")






    def end_session(self):
        self.driver.quit()


