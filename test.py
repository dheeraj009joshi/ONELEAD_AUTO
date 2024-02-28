import time
from functools import wraps
from flask import session,redirect,url_for,request, render_template
from bson.objectid import ObjectId
from selenium import webdriver

driver=webdriver.Edge(executable_path="dslkndf")
from selenium.webdriver.common import driver_finder
from app.DB.Db_config import collection
from app.ONELOGIN_CLASS.ONELOGIN import onLogin

message='''<table bgcolor="#E4E4E4" border="0" cellpadding="0" cellspacing="0" style="background-color:#E4E4E4;" width="100%">
	<tbody>
		<tr>
			<td>
			<table align="center" bgcolor="#E4E4E4" border="0" cellpadding="0" cellspacing="0" class="full-width" style="background-color:#E4E4E4; width:600px;" width="600">
				<tbody>
					<tr>
						<td align="center" class="web" style="color:#666666; font-family: Roboto, Arial, Helvetica, sans-serif; font-size:11px; line-height:13px; padding-top:12px; padding-bottom:9px;">Trouble viewing this email?<a href="http://www.auto1mail.com/templates/2024-02/08-Presidents/GA251.html" style="color:#eb091e;" target="_blank">&nbsp;Read&nbsp;online</a></td>
					</tr>
				</tbody>
			</table>
			</td>
		</tr>
		<tr>
			<td>
			<table align="center" border="0" cellpadding="0" cellspacing="0" class="full-width" style="width:600px;" width="600">
				<tbody>
					<tr>
						<td><!-- Email Content Begin --><!-- Header Begin -->
						<table align="center" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" class="full-width" style="background-color:#ffffff; width:600px;" width="600">
							<tbody>
								<tr>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
									<td class="stack-column-center" style="color:#ffffff; font-family:Roboto, Arial, Helvetica, sans-serif; font-size: 12px; line-height:14px; padding-top:15px; padding-bottom:15px; background-color: #ffffff;"><img alt="Logo" border="0" height="auto" hspace="0" src="http://www.auto1mail.com/templates/Test_JS/images/brand/logo-toyota.png" style="display:inline-block; vertical-align:bottom; max-width: 200px;" vspace="0" width="200"></td>
									<!-- <td width="50" style="width:50px;"> </td> -->
									<td align="right" class="stack-column-center" style="color:#333; font-family: Open Sans, Arial, Helvetica, sans-serif; font-size: 11px; line-height:16px; padding-top:15px; padding-bottom:15px; text-align:right; white-space:normal;" valign="bottom"><strong style="font-size: 16px;">World Toyota</strong><br>
									<span style="color: #333;"><a href="https://www.worldtoyota.com/new-vehicles/" style="color: #eb091e; text-decoration: none;" target="_blank">New Inventory</a>&nbsp;|&nbsp;<a href="https://www.worldtoyota.com/used-vehicles/" style="color: #eb091e; text-decoration: none;" target="_blank">Pre-Owned Inventory</a>&nbsp;|&nbsp;<a href="https://www.worldtoyota.com/service/schedule-service/" style="color: #eb091e; text-decoration: none;" target="_blank">Service</a></span></td>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
								</tr>
							</tbody>
						</table>
						<!-- Header End --><!-- Hero Image Begin -->

						<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" class="full-width" style="background-color:#ffffff; width:600px;" width="600">
							<tbody>
								<tr>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
									<td style="color:#141414; font-family:Open Sans, Arial, Helvetica, sans-serif; font-size:20px; line-height:24px;"><a href="https://www.worldtoyota.com/used-vehicles/" style="color:#1473E6;" target="_blank"><img alt="Hero Image Alt Text" border="0" class="mobile-image" height="auto" hspace="0" src="http://www.auto1mail.com/templates/2024-02/08-Presidents/images/top.png" style="color:#141414; font-family:Open Sans, Arial, Helvetica, sans-serif; font-size:20px; line-height:24px; display:block; vertical-align:top; max-width: 570px; padding-bottom:15px;" vspace="0" width="570"> </a></td>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
								</tr>
							</tbody>
						</table>
						<!-- Hero Image End --><!-- Footer Begin -->

						<table align="center" bgcolor="#eb091e" border="0" cellpadding="0" cellspacing="0" class="full-width" style="background-color:#eb091e; width:600px;" width="600">
							<tbody>
								<tr>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
									<td align="center" style="color:#ffffff; font-family: Open Sans, Arial, Helvetica, sans-serif; font-size: 11px; line-height:16px; padding-top:15px; padding-bottom:15px; text-align:center; white-space:normal;" valign="bottom"><strong style="font-size: 16px;">World Toyota</strong><br>
									5800 Peachtree Bvld, Atlanta, GA 30341<br>
									<a href="https://www.worldtoyota.com/" style="color: #ffffff; text-decoration: none;" target="_blank">www.‌worldtoyota‌.com</a> | (678) 547-9130
									<table align="center" cellpadding="5px;">
										<tbody>
											<tr>
												<td style="padding-top: 10px;"><a href="https://www.facebook.com/WorldToyotaAtlanta"><img alt="Facebook" height="30" src="http://www.auto1mail.com/templates/Test_JS/images/iconmonstr-facebook-4-240.png" style="max-width: 30px;" width="30"></a></td>
												<td style="padding-top: 10px;"><a href="https://twitter.com/worldtoyotaatl?lang=en"><img alt="Twitter" height="30" src="http://www.auto1mail.com/templates/Test_JS/images/iconmonstr-twitter-4-240.png" style="max-width: 30px;" width="30"></a></td>
												<td style="padding-top: 10px;"><a href="https://www.youtube.com/channel/UCZR_Lf0faM-7tJ0ymBxNn6Q"><img alt="YouTube" height="30" src="http://www.auto1mail.com/templates/Test_JS/images/iconmonstr-youtube-4-240.png" style="max-width: 30px;" width="30"></a></td>
											</tr>
										</tbody>
									</table>
									© Copyright 2024, Group 1 Automotive</td>
									<td class="mobile-spacer" style="width:15px;" width="15">&nbsp;</td>
								</tr>
							</tbody>
						</table>
						<!-- Footer End --><!-- Email Content End --></td>
					</tr>
				</tbody>
			</table>
			</td>
		</tr>
	</tbody>
</table>'''


all_urls=['https://group1.eleadcrm.com/evo2/fresh/elead-v45/elead_track/NewProspects/OpptyDetails.aspx?lPID=24499393&lDID=23724428']
    
def auto_email(user_id,all_urls,email_subject,email_body):
    user_id = ObjectId(str(user_id))
    user = collection.find_one({"_id": user_id})
    object=onLogin()
    object.login_to_oneLogin()
    time.sleep(10)
    object.open_eleads_oneLogin()
    for url in all_urls:
        try:
            object.send_message(url,email_body)
            user["todays_emails"] = user.get("todays_emails", 0) + 1
            result = collection.update_one({"_id": user_id}, {"$set": user})
        except Exception as err:
            pass
        
auto_email("65d4885c537bae39a494c49a",all_urls,"Are you still in market",message)