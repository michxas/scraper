import sys
import os
from colorama import Fore
import discum
import time

name = os.getlogin()
ez = f'SKID-HUB ID SCRAPER! Thanks for using {name}!'

from os import system
system("title " + ez)

green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
cyan = Fore.CYAN
logo = f'''\n                                           {Fore.GREEN}Simple Tutorial on how to use! \n{cyan}1.{white} Get your token. \n{cyan}2. {white}Go to setting>>advaced>>Turn Developer mode ON\n{cyan}3. {white}Go to scraper and paste ur token.\n{cyan}4.{white} Right click on server you want to scrape and click 'Copy ID' Then paste it into scraper.\n{cyan}5.{white} Right click on any channel then 'Copy ID' and paste it into a scraper.\n{cyan}6.{white} Press enter and wait.\n{cyan}7.{white} All ids are saved in 'ids'.txt file\nTy for using!'''
                            

               
print(logo)
print(' ')
print(' ')  
print(' ')  
print(' ')  
print(' ')                          


print(f'Hello, {name}!')     
token = input(f'[{cyan}?{white}] Token to scrape with >')    
guildid = input(f'[{cyan}?{white}] Server ID to scrape >')   
channelid = input(f'[{cyan}?{white}] Channel ID to scrape >')
input("Press 'Enter' to start scraping...")


bot = discum.Client(token=token)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members(guildid, channelid)
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)

f = open('ids.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()

os.system('cls')
input("ID's SCRAPED! Saved in 'ids.txt' Press enter to exit")