import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say
from flask import Flask, jsonify, request
import asyncio
import signal
import sys
# Add these imports if not already present
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  



# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
# Add with other global variables
reject_spam_running = False
insquad = None 
joining_team = False 
reject_spam_task = None
lag_running = False
lag_task = None
# Add these with your other global variables at the top
reject_spam_running = False
reject_spam_task = None
evo_cycle_running = False
evo_cycle_task = None
# Add with other global variables at the top
auto_start_running = False
auto_start_teamcode = None
stop_auto = False
auto_start_task = None
start_spam_duration = 18  # seconds to spam start
wait_after_match = 20  # seconds to wait after match
start_spam_delay = 0.2  # delay between start packets

# RARE LOOK CHANGER BUNDLE ID
BUNDLE = {
    "rampage": 914000002,
    "cannibal": 914000003,
    "devil": 914038001,
    "scorpio": 914039001,
    "frostfire": 914042001,
    "paradox": 914044001,
    "naruto": 914047001,
    "aurora": 914047002,
    "midnight": 914048001,
    "itachi": 914050001,
    "dreamspace": 914051001
}
# Emote mapping for all emote commands


# Badge values for s1 to s5 commands - using your exact values
BADGE_VALUES = {
    "s1": 1048576,    # Your first badge
    "s2": 32768,      # Your second badge  
    "s3": 2048,       # Your third badge
    "s4": 64,         # Your fourth badge
    "s5": 262144     # Your seventh badge
}







evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003"   # m60
}






EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909051015,
    12: 909041002,
    13: 909039004,
    14: 909042008,
    15: 909051014,
    16: 909039012,
    17: 909040010,
    18: 909035010,
    19: 909041005,
    20: 909051003,
    21: 909034001
}






ALL_EMOTES = {
    1: 909000001, #hello
    2: 909000002, #lol
    3: 909000003, #provoke
    4: 909000004, #applause
    5: 909000005, #dab
    6: 909000006, #chicken
    7: 909000007, #armwave
    8: 909000008, #dance
    9: 909000009, #babyshark
    10: 909000010, #rose
    11: 909000011, #mummydance
    12: 909000012, #pushup
    13: 909000013, #shuffling
    14: 909000014, #throne
    15: 909000015, #dragon
    16: 909000016, #dangerousgame
    17: 909000017, #jaguardance
    18: 909000018, #threaten
    19: 909000019, #shakewithme
    20: 909000020, #devilsmove
    21: 909000021, #furiousslam
    22: 909000022, #moonflip
    23: 909000023, #wigglewalk
    24: 909000024, #battledance
    25: 909000025, #highfive
    26: 909000026, #shakeitup
    27: 909000027, #gloriousspin
    28: 909000028, #cranekick
    29: 909000029, #partydance
    30: 909000031, #jigdance
    31: 909000032, #selfie
    32: 909000033, #soulshaking
    33: 909000034, #pirate
    34: 909000035, #healingdance
    35: 909000036, #topdj
    36: 909000037, #deathglare
    37: 909000038, #powerofmoney
    38: 909000039, #car
    39: 909000040, #breakdance
    40: 909000041, #kungfu
    41: 909000042, #bonappetit
    42: 909000043, #aimfire
    43: 909000044, #swan
    44: 909000045, #heart
    45: 909000046, #teatime
    46: 909000047, #bringiton
    47: 909000048, #whyohwhy
    48: 909000049, #fancyhands
    49: 909000051, #shimmy
    50: 909000052, #doggie
    51: 909000053, #challengeon
    52: 909000054, #lasso
    53: 909000055, #money
    54: 909000056, #unknown
    55: 909000057, #unknown
    56: 909000058, #unknown
    57: 909000059, #unknown
    58: 909000060, #unknown
    59: 909000061, #unknown
    60: 909000062, #unknown
    61: 909000063, #ak
    62: 909000064, #unknown
    63: 909000065, #unknown
    64: 909000066, #unknown
    65: 909000067, #unknown
    66: 909000068, #scar
    67: 909000069, #unknown
    68: 909000070, #unknown
    69: 909000071, #unknown
    70: 909000072, #cobra
    71: 909000073, #unknown
    72: 909000074, #unknown
    73: 909000075, #mp40
    74: 909000076, #unknown
    75: 909000077, #unknown
    76: 909000078, #unknown
    77: 909000079, #morepractice
    78: 909000080, #ffws2021
    79: 909000081, #m10_green
    80: 909000082, #goodgame
    81: 909000083, #greetings
    82: 909000084, #walker
    83: 909000085, #xm8
    84: 909000086, #mythosfour
    85: 909000087, #championgrab
    86: 909000088, #winandchill
    87: 909000089, #hadouken
    88: 909000090, #famas
    89: 909000091, #bigsmash
    90: 909000092, #fancysteps
    91: 909000093, #allincontrol
    92: 909000094, #debugging
    93: 909000095, #waggorwave
    94: 909000096, #crazyguitar
    95: 909000097, #poof
    100: 909042007, #lvl100
    106: 909000108, #unknown
    119: 909000121, #dribbleking
    120: 909000122, #ffwsguitar
    121: 909000123, #mindit
    122: 909000124, #goldencombo
    123: 909000125, #sickmoves
    124: 909000126, #rapswag
    125: 909000127, #battleinstyle
    126: 909000128, #rulersflag
    127: 909000129, #moneythrow
    128: 909000130, #endlessbullets
    129: 909000131, #smoothsway
    130: 909000132, #number1
    131: 909000133, #fireslam
    132: 909000134, #heartbroken
    133: 909000135, #rockpaperscissors
    134: 909000136, #shatteredreality
    135: 909000137, #haloofmusic
    136: 909000138, #burntbbq
    137: 909000139, #switchingsteps
    138: 909000140, #creedslay
    139: 909000141, #leapoffail
    140: 909000142, #rhythmgirl
    142: 909000144, #kungfutigers
    143: 909000145, #possessedwarrior
    144: 909000150, #raiseyourthumb
    145: 909033001, #m4a1
    146: 909033002, #mp5
    147: 909033003, #comeanddance
    148: 909033004, #dropkick
    149: 909033005, #sitdown
    150: 909033006, #booyahsparks
    151: 909033007, #ffwsdance
    152: 909033008, #easypeasy
    153: 909033009, #winnerthrow
    154: 909033010, #weightofvictory
    155: 909034001, #rampagebook
    156: 909034002, #collapse
    157: 909034003, #flaminggroove
    158: 909034004, #energetic
    159: 909034005, #ridicule
    160: 909034006, #teasewaggor
    161: 909034007, #greatconductor
    162: 909034008, #fakedeath
    163: 909034009, #twerk
    164: 909034010, #brheroic
    165: 909034011, #brmaster
    166: 909034012, #csheroic
    167: 909034013, #csmaster
    168: 909034014, #yesido
    169: 909035001, #freemoney
    173: 909035005, #victoriouseagle
    174: 909035006, #flyingsaucer
    175: 909035007, #m18
    176: 909035008, #bobbledance
    177: 909035009, #weighttraining
    178: 909035010, #beautifullove
    179: 909035011, #groovemoves
    180: 909035012, #an94
    181: 909035013, #louderplease
    182: 909035014, #ninjastand
    183: 909035015, #creatorinaction
    184: 909036001, #ghost
    185: 909036002, #shibasurf
    186: 909036003, #waiterwalk
    187: 909036004, #grafficameraman
    188: 909036005, #agileboxer
    189: 909036006, #sunbathing
    190: 909036008, #skateboardswag
    191: 909036009, #phantomtamer
    192: 909036010, #signal
    193: 909036011, #eternaldescent
    194: 909036012, #swaggydance
    195: 909036014, #admire
    196: 909037001, #reindeerfloat
    197: 909037002, #bamboodance
    198: 909037003, #constellationdance
    199: 909037004, #trophygrab
    200: 909037005, #starryhands
    201: 909037006, #yum
    202: 909037007, #happydancing
    203: 909037008, #juggle
    204: 909037009, #neonsign
    205: 909037010, #beasttease
    206: 909037011, #fist
    207: 909037012, #clapdance
    208: 909038001, #influencer
    210: 909038003, #technoblast
    211: 909038004, #valentineheart
    212: 909038005, #angrywalk
    213: 909038006, #makesomenoise
    214: 909038008, #crocohooray
    215: 909038009, #scorpionspin
    216: 909038010, #thompson_evo
    217: 909038011, #shallwedance
    218: 909038012, #g18
    219: 909038013, #spinmaster
    220: 909039001, #festival
    221: 909039002, #artisticdance
    222: 909039003, #forwardbackward
    223: 909039004, #scorpionfriend
    224: 909039005, #achingpower
    225: 909039006, #earthlyforce
    226: 909039007, #grenademagic
    227: 909039008, #ohyeah
    228: 909039009, #graceonwheels
    229: 909039010, #flex
    230: 909039011, #m10_red
    231: 909039012, #firebeasttamer
    232: 909039013, #crimsontunes
    233: 909039014, #swaggyvsteps
    234: 909040001, #chromaticfinish
    235: 909040002, #smashthefeather
    236: 909040003, #sonoroussteps
    237: 909040004, #fish
    238: 909040005, #chromaticpop
    239: 909040006, #chromatwist
    240: 909040008, #birthofjustice
    241: 909040009, #spidersense
    242: 909040010, #mp40_blue
    243: 909040011, #playwiththunderbolt
    244: 909040012, #anniversary
    245: 909040013, #wisdomswing
    247: 909041001, #thunderflash
    248: 909041002, #whirlpool
    249: 909041003, #inosuke
    250: 909041004, #flyinginksword
    251: 909041005, #groza
    252: 909041006, #dancepuppet
    253: 909041007, #highknees
    254: 909041008, #flar
    255: 909041009, #feeltheelectricity
    256: 909041010, #whacacotton
    257: 909041011, #honorablemention
    258: 909041012, #brgrandmaster
    259: 909041013, #csgm
    260: 909041014, #monsterclubbing
    261: 909041015, #basudaradance
    262: 909042001, #stirfryfrostfire
    263: 909042002, #moneyrain
    264: 909042003, #frostfirecalling
    265: 909042004, #stompingfoot
    266: 909042005, #thisway
    267: 909042006, #excellentservice
    269: 909042008, #woodpecker
    270: 909042009, #celebrationschuss
    271: 909042011, #dawnvoyage
    272: 909042012, #lamborghiniride
    274: 909042016, #handgrooves
    275: 909042017, #unknown
    276: 909042018, #kemusan
    277: 909043001, #ribbitrider
    278: 909043002, #innerself
    279: 909043003, #emperortreasure
    280: 909043004, #whysochaos
    281: 909043005, #hugefeast
    282: 909043006, #colorburst
    283: 909043007, #dragonswipe
    284: 909043008, #samba
    285: 909043009, #speedsummon
    288: 909044001, #bytemounting
    289: 909044002, #unicyclist
    290: 909044003, #basketrafting
    291: 909044004, #happylamb
    292: 909044005, #paradox
    294: 909044007, #raiseyourthumb2
    295: 909044008, #claphands
    296: 909044009, #donedeal
    297: 909044010, #starcatcher
    298: 909044011, #paradoxwings
    299: 909044012, #zombified
    300: 909044015, #unknown
    301: 909044016, #honkup
    302: 909045001, #cyclone
    303: 909045002, #springrocker
    304: 909045003, #giddyup
    305: 909045004, #goosydance
    306: 909045005, #captainvictor
    307: 909045006, #youknowimgood
    308: 909045007, #stepstep
    309: 909045008, #superyay
    310: 909045009, #moonwalk
    311: 909045010, #flowersalute
    312: 909045011, #foxyrun
    314: 909045015, #floatingmeditation
    315: 909045016, #naatunaatu
    316: 909045017, #championswalk
    317: 909046001, #auraboarder
    318: 909046002, #booyahchamp
    319: 909046003, #controlledcombustion
    322: 909046006, #gunspinning
    323: 909046007, #crowdpleaser
    324: 909046008, #nosweat
    325: 909046009, #magmaquake
    326: 909046010, #maxfirepower
    327: 909046011, #canttouchthis
    328: 909046012, #firestarter
    329: 909046013, #ffwsflag
    330: 909046014, #beatdrop
    331: 909046015, #spatialawareness
    332: 909046016, #trapping
    333: 909046017, #soaringup
    334: 909047001, #wontbowdown
    337: 909047004, #flutterdash
    338: 909047005, #slipperythrone
    339: 909047006, #acceptancespeech
    340: 909047007, #lovemelovemenot
    341: 909047008, #scissorsavvy
    342: 909047009, #thinker
    343: 909047010, #matchcountdown
    344: 909047011, #hiptwists
    345: 909047012, #jkt48
    346: 909047013, #stormyascent
    347: 909047015, #rasengan
    348: 909047016, #thousandyears
    349: 909047017, #ninjasign
    350: 909047018, #ninja
    351: 909047019, #clone
    353: 909048002, #midnightperuse
    354: 909048003, #guitargroove
    355: 909048004, #keyboardplayer
    356: 909048005, #ondrums
    357: 909048006, #chacchac
    358: 909048007, #pillowfight
    359: 909048008, #targetpractice
    361: 909048010, #hitasix
    362: 909048011, #flagsummon
    363: 909048012, #swiftsteps
    364: 909048013, #carnivalfunk
    365: 909048014, #slurp
    366: 909048015, #paint
    367: 909048016, #halftime
    368: 909048017, #throwin
    369: 909048018, #bailalorocky
    370: 909049001, #bigdill
    371: 909049002, #handraise
    372: 909049003, #owl
    373: 909049004, #slapandtwist
    374: 909049005, #sidewiggle
    375: 909049006, #creationdays
    376: 909049007, #rainingcoins
    378: 909049009, #infiniteloops
    379: 909049010, #p90
    380: 909049011, #boxingmachine
    381: 909049012, #flyingguns
    382: 909049013, #comicbarf
    383: 909049014, #driveby
    384: 909049015, #pedalmetal
    385: 909049016, #spearspin
    386: 909049017, #guildflag
    387: 909049018, #discodazzle
    388: 909049019, #squatchallenge
    389: 909049020, #winninggoal
    390: 909049021, #headhigh
    391: 909050002, #ninjasummon
    393: 909050004, #foreheadpoke
    394: 909050005, #fireball
    395: 909050006, #flyingraijin
    396: 909050008, #thor
    398: 909050010, #drumtwirl
    399: 909050011, #bunnyaction
    400: 909050012, #broomswoosh
    401: 909050013, #blade
    402: 909050014, #mapread
    403: 909050015, #tomato
    404: 909050016, #tacticalmoveout
    405: 909050017, #bunnywiggle
    406: 909050018, #flamingheart
    407: 909050019, #rainorshine
    408: 909050020, #sholay
    409: 909050021, #peakpoints
    410: 909046004, #cheerstovictory
    411: 909046005, #shoeshining
    412: 909047002, #aurora
    413: 909047003, #couchfortwo
    414: 909048001, #rescue
    415: 909048009, #goofycamel
    416: 909049008, #clapclaphooray
    417: 909050003, #finalbattle
    418: 909052010, #unknown
}


def resolve_emote_id(raw_id: int) -> int:
    """
    Converts shortcut numbers like 1/2/3 into real emote IDs if mapped.
    If raw_id is already a real emote id, it returns it unchanged.
    """
    return ALL_EMOTES.get(raw_id, raw_id)
    
    
# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()

async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    



def get_idroom_by_idplayer(packet_hex):
    """Extract room ID from packet - converted from your other TCP"""
    try:
        json_result = get_available_room(packet_hex)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"Error extracting room ID: {e}")
        return None

async def check_player_in_room(target_uid, key, iv):
    """Check if player is in a room by sending status request"""
    try:
        # Send status request packet
        status_packet = await GeT_Status(int(target_uid), key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        
        # You'll need to capture the response packet and parse it
        # For now, return True and we'll handle room detection in the main loop
        return True
    except Exception as e:
        print(f"Error checking player room status: {e}")
        return False
        
            


    

def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000002", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000004", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        

async def SEnd_InV_with_Cosmetics(Nu, Uid, K, V, region):
    """Simple version - just add field 5 with basic cosmetics"""
    region = "ind"
    fields = {
        1: 2, 
        2: {
            1: int(Uid), 
            2: region, 
            4: int(Nu),
            # Simply add field 5 with basic cosmetics
            5: {
                1: "BOT",                    # Name
                2: int(await get_random_avatar()),     # Avatar
                5: random.choice([1048576, 32768, 2048]),  # Random badge
            }
        }
    }

    if region.lower() == "ind":
        packet = '0514'
    elif region.lower() == "bd":
        packet = "0519"
    else:
        packet = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, K, V)   
            
async def join_custom_room(room_id, room_password, key, iv, region):
    """Join custom room with proper Free Fire packet structure"""
    fields = {
        1: 61,  # Room join packet type (verified for Free Fire)
        2: {
            1: int(room_id),
            2: {
                1: int(room_id),  # Room ID
                2: int(time.time()),  # Timestamp
                3: "BOT",  # Player name
                5: 12,  # Unknown
                6: 9999999,  # Unknown
                7: 1,  # Unknown
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,  # Room type
            },
            3: str(room_password),  # Room password
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 33, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.120.1", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"❌ Error in RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    """Send join request with specific badge - converted from your old TCP"""
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[C][B][FF0000] FF_TCP_BOT",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(await get_random_avatar()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: badge_value  # Dynamic badge value
            },
            32: badge_value,    # Dynamic badge value
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    """Leave squad packet"""
    fields = {
        1: 7,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def join_teamcode_packet(team_code, key, iv, region):
    """Join team using code"""
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {
                2: 800,
                6: 11,
                8: "1.111.1",
                9: 5,
                10: 1
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region):
    """Auto start loop that joins, starts match, waits, leaves, repeats"""
    global auto_start_running, stop_auto
    
    print(f"[AUTO] Auto start loop started for team {team_code}")
    
    while not stop_auto:
        try:
            # Send status message
            status_msg = f"[B][C][FFA500]🤖 Auto Start Bot\n🎯 Team: {team_code}\n⚡ Joining team..."
            await safe_send_message(chat_type, status_msg, uid, chat_id, key, iv)
            
            # Join team
            join_packet = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(2)
            
            # Send start spam status
            start_msg = f"[B][C][00FF00]✅ Joined team {team_code}\n🎯 Starting match for {start_spam_duration} seconds..."
            await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
            
            # Start spam
            start_packet = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            spam_count = 0
            
            while time.time() < end_time and not stop_auto:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                spam_count += 1
                await asyncio.sleep(start_spam_delay)
            
            if stop_auto:
                break
            
            # Wait after match
            wait_msg = f"[B][C][FFFF00]⏳ Match started! Bot in lobby waiting {wait_after_match} seconds..."
            await safe_send_message(chat_type, wait_msg, uid, chat_id, key, iv)
            
            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            
            if stop_auto:
                break
            
            # Leave squad
            leave_msg = f"[B][C][FF0000]🔄 Leaving team {team_code} to rejoin and start again..."
            await safe_send_message(chat_type, leave_msg, uid, chat_id, key, iv)
            
            leave_packet = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"[AUTO] Error in auto_start_loop: {e}")
            error_msg = f"[B][C][FF0000]❌ Auto start error: {str(e)}\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            break
    
    auto_start_running = False
    stop_auto = False
    print(f"[AUTO] Auto start loop stopped for team {team_code}")
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"❌ Error resetting bot: {e}")
        return False    
    
async def create_custom_room(room_name, room_password, max_players, key, iv, region):
    """Create a custom room"""
    fields = {
        1: 3,  # Create room packet type
        2: {
            1: room_name,
            2: room_password,
            3: max_players,  # 2, 4, 8, 16, etc.
            4: 1,  # Room mode
            5: 1,  # Map
            6: "en",  # Language
            7: {   # Player info
                1: "BotHost",
                2: int(await get_random_avatar()),
                3: 330,
                4: 1048576,
                5: "BOTCLAN"
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)              
            


async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][1E90FF]🌀 Request received! Preparing to spam {target_uid}...\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Reset bot state
        await reset_bot_state(key, iv, region)
        
        # Create and send join packets
        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        spam_count = 3
        
        for i in range(spam_count):
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Sent /{cmd} request #{i+1} with badge {badge_value}")
            await asyncio.sleep(0.1)
        
        success_msg = f"[B][C][00FF00]✅ Successfully Sent {spam_count} Join Requests!\n🎯 Target: {target_uid}\n🏷️ Badge: {badge_value}\n"
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup
        await asyncio.sleep(1)
        await reset_bot_state(key, iv, region)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error in /{cmd}: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)





    
    
    
async def auto_rings_emote_dual(sender_uid, bot_uid, key, iv, region):
    """Send The Rings emote to both sender and bot for dual emote effect"""
    try:
        # The Rings emote ID
        
        rings_emote_id = 909050009
        
         # Send emote to SENDER (person who invited)
        emote_to_sender = await Emote_k(int(sender_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
        # Small delay between emotes
        await asyncio.sleep(0.5)
        
        # Send emote to BOT (bot performs emote on itself)
        emote_to_bot = await Emote_k(int(bot_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
        
        print(f"🤖 Bot performed dual Rings emote with sender {sender_uid} and bot {bot_uid}!")
        
    except Exception as e:
        print(f"Error sending dual rings emote: {e}")    
        
        
async def Room_Spam(Uid, Rm, Nm, K, V):
   
    same_value = random.choice([32768])  #you can add any badge value 
    
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000] FF_TCP_BOT",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await get_random_avatar()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: same_value  
            },
            16: same_value,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: same_value  
            },
            32: same_value,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    
async def evo_cycle_spam(uids, key, iv, region):
    """Cycle through all evolution emotes one by one with 5-second delay"""
    global evo_cycle_running
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        for emote_number, emote_id in evo_emotes.items():
            if not evo_cycle_running:
                break
                
            print(f"Sending evolution emote {emote_number} (ID: {emote_id})")
            
            for uid in uids:
                try:
                    uid_int = int(uid)
                    H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                    print(f"Sent emote {emote_number} to UID: {uid}")
                except Exception as e:
                    print(f"Error sending evo emote {emote_number} to {uid}: {e}")
            
            # Wait 5 seconds before moving to next emote (as requested)
            if evo_cycle_running:
                print(f"Waiting 5 seconds before next emote...")
                for i in range(5):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
        
        # Small delay before restarting the cycle
        if evo_cycle_running:
            print("Completed one full cycle of all evolution emotes. Restarting...")
            await asyncio.sleep(2)
    
    print("Evolution emote cycle stopped")
    
async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"Sent reject spam #{count} to {target_uid}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"Error in reject spam: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"[B][C][00FF00]✅ Reject Spam Completed Successfully for ID {target_uid}\n✅ Total packets sent: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ Reject Spam Partially Completed for ID {target_uid}\n⚠️ Total packets sent: {spam_count * 2}\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("Reject spam was cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in reject spam: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)    
    
async def banecipher(client_id, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[0. 00000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[0000=00]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 
####################################
def bundle_packet(self, bundle_id, target_uid):
        fields = {
            1: 88,
            2: {
                1: {
                    1: bundle_id,
                    2: 1
                },
                2: 2
            }
        }
        packet = create_protobuf_packet(fields).hex()
        encrypted = encrypt_packet(packet, self.key, self.iv)
        header_length = len(encrypted) // 2
        header_length_hex = dec_to_hex(header_length)

        if len(header_length_hex) == 2:
            final_header = "0515000000"
        elif len(header_length_hex) == 3:
            final_header = "051500000"
        elif len(header_length_hex) == 4:
            final_header = "05150000"
        elif len(header_length_hex) == 5:
            final_header = "0515000"
        else:
            final_header = "0515000000"

        final_packet = final_header + header_length_hex + encrypted
        return bytes.fromhex(final_packet)

async def bundle_packet_async(bundle_id, key, iv, region="ind"):
    """Create bundle packet"""
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: 1
            },
            2: 2
        }
    }
    
    # Use your CrEaTe_ProTo function
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use your encrypt_packet function
    encrypted = await encrypt_packet(packet_hex, key, iv)
    
    # Use your DecodE_HeX function
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    
    # Build final packet based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    
    # Determine header based on length
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)



Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

print(get_random_color())
    
# ---- Random Avatar ----
async def get_random_avatar():
    await asyncio.sleep(0)  # makes it async but instant
    avatar_list = [
        '902050001', '902050002', '902050003', '902039016', '902050004',
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
    return random.choice(avatar_list)
    
async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Joined team: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"🎭 Performed emote {emote_id} to UID {target_uid}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"🚪 Left team: {team_code}")
        
        return True, f"Quick emote attack completed! Sent emote to UID {target_uid}"
        
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "User-Agent": "GarenaMSDK/5.5.2P3(ASUS_Z01QD;Android 9;en-IN;IND;)",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip" 
        }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status != 200:
                print(f"⚠ Guest login HTTP status: {response.status}")
                return None, None
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)
            
async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.120.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PKQ1.190522.001)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "loginbp.ggpolarbear.com",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB52"
    }
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    headers = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PKQ1.190522.001)",
    'Authorization': f"Bearer {token}",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"}
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    """Safely send message with retry mechanism"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            print(f"Message sent successfully on attempt {attempt + 1}")
            return True
        except Exception as e:
            print(f"Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)  # Wait before retry
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.1)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"Error in custom_emote_spam for uid {uid}: {e}")
            break

# NEW FUNCTION: Faster spam request loop - Sends exactly 30 requests quickly
async def spam_request_loop_with_cosmetics(target_uid, key, iv, region):
    """Spam request function with cosmetics - using your same structure"""
    global spam_request_running
    
    count = 0
    max_requests = 30
    
    # Different badge values to rotate through
    badge_rotation = [1048576, 32768, 2048, 64, 4094, 11233, 262144]
    
    while spam_request_running and count < max_requests:
        try:
            # Rotate through different badges
            current_badge = badge_rotation[count % len(badge_rotation)]
            
            # Create squad (same as before)
            PAc = await OpEnSq(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
            await asyncio.sleep(0.2)
            
            # Change squad size (same as before)
            C = await cHSq(5, int(target_uid), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
            await asyncio.sleep(0.2)
            
            # Send invite WITH COSMETICS (enhanced version)
            V = await SEnd_InV_With_Cosmetics(5, int(target_uid), key, iv, region, current_badge)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            # Leave squad (same as before)
            E = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
            
            count += 1
            print(f"✅ Sent cosmetic invite #{count} to {target_uid} with badge {current_badge}")
            
            # Short delay
            await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"Error in cosmetic spam: {e}")
            await asyncio.sleep(0.5)
    
    return count
            


# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"

# NEW FUNCTION: all emote spam with mapping
async def play_emote_spam(uids, number, key, iv, region):
    """Send all emotes based on number mapping"""
    try:
        emote_id = ALL_EMOTES.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-410 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending play emote to {uid}: {e}")
        
        return True, f"Sent playlution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in play_emote_spam: {str(e)}"

# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_custom_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed custom evolution emote spam {count} times"
    

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)
    
    
async def AcceptJoinRequest(bot_uid, requester_uid, K, V):
    fields = {
        1: 38,
        2: {
            1: int(bot_uid),
            2: int(requester_uid),
            8: 1
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0514', K, V)
    
    
async def TcPOnLine(ip, port, key, iv, AutHToKen, region, reconnect_delay=0.5):
    global online_writer, last_status_packet, status_response_cache, insquad, joining_team, whisper_writer
    
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    whisper_writer = None
    
    while True:
        try:
            print(f"Attempting to connect to {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("Authentication token sent. Entering read loop...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("Connection closed by the server.")
                    break
                    
                data_hex = data2.hex()
                
                # =================== EMOTE HIJACK ====================
                if data_hex.startswith('0514'):
                    try:
                        # Try to extract emote info from encrypted packet
                        decrypted = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(decrypted)
                        
                        # Check for Type 21 (emote packet)
                        if packet_json.get('1') == 21:
                            if '2' in packet_json and 'data' in packet_json['2']:
                                emote_data = packet_json['2']['data']
                                
                                if ('1' in emote_data and '2' in emote_data and 
                                    '5' in emote_data and 'data' in emote_data['5']):
                                    
                                    nested = emote_data['5']['data']
                                    
                                    if '1' in nested and '3' in nested:
                                        sender_uid = nested.get('1', {}).get('data')
                                        emote_id = nested.get('3', {}).get('data')
                                        
                                        print(f"🎯 EMOTE HIJACK DETECTED!")
                                        print(f"👤 Sender: {sender_uid}")
                                        print(f"🎭 Original emote: {emote_id}")
                                        
                                        # Send special emote back
                                        special_emote = await Emote_k(int(sender_uid), 909038002, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', special_emote)
                                        print(f"🎁 Sent special emote 909038002 to {sender_uid}")
                                        
                                        # Mirror user's emote back
                                        await asyncio.sleep(0.3)
                                        try:
                                            mirror_emote_id = int(emote_id)
                                            mirror_packet = await Emote_k(int(sender_uid), mirror_emote_id, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', mirror_packet)
                                            print(f"🔄 Mirroring user's emote {emote_id} back")
                                        except ValueError:
                                            print(f"❌ Could not convert emote ID: {emote_id}")
                                        
                                        # Bot also does the emote to itself
                                        await asyncio.sleep(0.2)
                                        try:
                                            bot_uid = 13777711848
                                            bot_self_emote = await Emote_k(bot_uid, int(emote_id), key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                                            print(f"🤖 Bot also doing emote {emote_id}")
                                        except Exception as e:
                                            print(f"❌ Bot self-emote failed: {e}")
                                        
                                        continue  # Skip other processing for this packet
                                        
                    except Exception as e:
                        print(f"❌ Emote hijack error: {e}")
                        pass

                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        pkt_type = packet_json.get('4', {})
                        if isinstance(pkt_type, dict):
                            pkt_type = pkt_type.get('data')
                        if pkt_type == 3:
                            pass
                        elif pkt_type in [7, 8, 9, 10, 11, 56]:
                            insquad = None
                            joining_team = False
                            print(f"Squad exited or dissolved (type {pkt_type}), insquad reset.")
                            continue
                    except Exception as e:
                        print(f"Error in auto-accept case 1: {e}")
                        pass
                
                # Case 2: Receiving an invitation while not in a squad (Auto-Join/Accept)
                if data_hex.startswith("0500") and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)

                        pkt_type = packet_json.get('4', {})
                        if isinstance(pkt_type, dict):
                            pkt_type = pkt_type.get('data')

                        def D(x):
                            if isinstance(x, dict) and 'data' in x:
                                return x['data']
                            return x

                        if pkt_type == 3:
                            bot_uid = D(packet_json.get('1'))
                            p5 = D(packet_json.get('5'))
                            if isinstance(p5, dict):
                                sender_uid = D(p5.get('1'))
                                team_code = D(p5.get('8'))
                                p2 = D(p5.get('2'))
                                invite_uid = D(p2.get('1')) if isinstance(p2, dict) else sender_uid
                                if sender_uid and team_code:
                                    uid = sender_uid
                                    squad_owner = sender_uid
                                    code = team_code
                                    emote_id = 909050009
                                    SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                                    inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
                                    print(f"Received squad invite from {squad_owner}, accepting...")
                                    Join = await ArohiAccepted(squad_owner, code, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)
                                    await asyncio.sleep(2)
                                    emote_to_sender = await Emote_k(int(uid), emote_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
                                    bot_emote = await Emote_k(int(bot_uid), emote_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)
                                    insquad = True

                        elif pkt_type == 34:
                            bot_uid = D(packet_json.get('1'))
                            p5 = D(packet_json.get('5'))
                            requester_uid = D(p5.get('1')) if isinstance(p5, dict) else None
                            if requester_uid:
                                print(f"Join request from {requester_uid}, approving...")
                                approve = await AcceptJoinRequest(bot_uid, requester_uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', approve)
                                print(f"Approval sent to {requester_uid}")

                    except Exception as e:
                        print(f"Auto-accept error: {e}")
                        insquad = None
                        joining_team = False

                # Case 3: Joining Team/Chat handling (long packet)
                if data_hex.startswith('0500') and len(data_hex) > 1000 and joining_team:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                
                        OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)

                        if CHaT_CoDe is None or SQuAD_CoDe is None:
                            print("Incomplete squad data, skipping auth")
                            continue  # or return

                        print(f"Received squad data for joining team, attempting chat auth for {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                        joining_team = False
                            
                    except Exception as e:
                        print(f"Error in joining_team chat auth: {e}")
                        pass

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 Received status response packet")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ Status packet structure missing '08' marker.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"✅ Parsed status for {player_id}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 SPECIAL CONDITION MET: Player {player_id} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ Error checking special condition: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "IN ROOM" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"Failed to extract room ID: {room_error}")
                
                                # If in squad, extract leader
                                elif "INSQUAD" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"Failed to extract leader: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"✅ Saved to cache: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================               
                # Case 4: General Chat Auth (long packet, not actively joining)
                if data_hex.startswith('0500') and len(data_hex) > 1000 and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        pkt_type_field = packet_json.get('4', {})
                        if isinstance(pkt_type_field, dict):
                            pkt_type = pkt_type_field.get('data')
                        else:
                            pkt_type = pkt_type_field
                            
                        if pkt_type != 6:
                            pass
                            
                        else:

                            OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)
                            
                            print(f"Received long packet, attempting general chat auth for {OwNer_UiD}...")
                            JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)

                    except Exception as e:
                        print(f"Error in general chat auth: {e}")
                        pass

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 Received status response packet")
    
                    try:
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ Status packet structure missing '08' marker.")
                            continue
        
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                                player_status = get_player_status(proto_part) 
                                print(f"✅ Parsed status for {player_id}: {player_status}")
                
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 SPECIAL CONDITION MET: Player {player_id} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ Error checking special condition: {cond_error}")
                                
                                # Extract room ID if in room
                                if "IN ROOM" in player_status:
                                    try:
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"Failed to extract room ID: {room_error}")
                
                                # Extract leader if in squad
                                elif "INSQUAD" in player_status:
                                    try:
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"Failed to extract leader: {leader_error}")
                
                                # Save to cache
                                # Assuming save_to_cache function exists
                                # save_to_cache(player_id, cache_entry)
                                print(f"✅ Status cache updated: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                

            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
            print(f"Connection closed. Reconnecting in {reconnect_delay} seconds...")

        except ConnectionRefusedError:
            print(f"Connection refused to {ip}:{port}. Retrying...")
            await asyncio.sleep(reconnect_delay)
        except asyncio.TimeoutError:
            print(f"Connection timeout to {ip}:{port}. Retrying...")
            await asyncio.sleep(reconnect_delay)
        except Exception as e:
            print(f"Unexpected error in TcPOnLine: {e}")
            await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, reject_spam_running, reject_spam_task
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - Bot Connected With Clan Chat Successfully ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        
                        # Debug print to see what we're receiving
                        print(f"Received message: {inPuTMsG} from UID: {uid} in chat type: {XX}")
                        
                    except:
                        response = None


                    if response:



                                #GET PLAYER ADD FRIEND
                        if inPuTMsG.strip().startswith('/add '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /add <uid>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 Sending Friend Requests..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:

                                    final_result = await loop.run_in_executor(executor, get_player_add, target_uid)

                                await safe_send_message(response.Data.chat_type, f"\n[B][C][00FF00]✅ {final_result}\n", uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/spam_req '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /spam_req <uid>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 Sending 100 Friend Requests to: {target_uid}..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                try:
                                    
                                    final_result = await send_all_friend_requests_async(target_uid)
                                    
                                    success_msg = f"\n[B][C][00FF00]✅ {final_result}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ Error: {str(e)}", uid, chat_id, key, iv)


                        if inPuTMsG.strip().startswith('/quick'):
                            print('Processing quick emote attack command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /quick (team_code) [emote_id] [target_uid]\n\n[FFFFFF]Examples:\n[00FF00]/quick ABC123[FFFFFF] - Join, send Rings emote, leave\n[00FF00]/ghostquick ABC123[FFFFFF] - Ghost join, send emote, leave\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
        
                                initial_message = f"[B][C][FFFF00]⚡ QUICK EMOTE ATTACK!\n\n[FFFFFF]🎯 Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n[FFFFFF]⏱️ Estimated: [00FF00]2 seconds\n\n[FFFF00]Executing sequence...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"[B][C][00FF00]✅ QUICK ATTACK SUCCESS!\n\n[FFFFFF]🏷️ Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n\n[00FF00]Bot joined → emoted → left! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF0000]❌ Regular attack failed: {result}\n"
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print("failed")
            
                        



                        if inPuTMsG.strip().startswith('/bundle'):
                            print('Processing bundle command')
    
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                                # Show available bundles
                                bundle_list = """[B][C][00FF00]🎁 AVAILABLE BUNDLES 🎁
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FFFFFF]• midnight
[FFFFFF]• aurora
[FFFFFF]• naruto  
[FFFFFF]• paradox
[FFFFFF]• frostfire
[FFFFFF]• rampage
[FFFFFF]• cannibal
[FFFFFF]• devil
[FFFFFF]• scorpio
[FFFFFF]• dreamspace
[FFFFFF]• itachi

[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[00FF00]Usage: /bundle [name]
[FFFFFF]Example: /bundle midnight"""
                                await safe_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                            else:
                                bundle_name = parts[1].lower()
        
                                # All bundles use the same ID: 914000002
                                bundle_id = BUNDLE.get(bundle_name)
        
                                initial_msg = f"[B][C][00FF00]🎁 Sending {bundle_name}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Create bundle packet
                                    bundle_packet = await bundle_packet_async(bundle_id, key, iv, region)
            
                                    if bundle_packet and online_writer:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                                        success_msg = f"[B][C][00FF00]✅ Done: {bundle_name}"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to create bundle packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error sending bundle: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # ===============================================================

                        # Invite Command - /inv (creates 5-player group and sends request)
                        if inPuTMsG.strip().startswith('/inv '):
                            print('Processing invite command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nCreating 5-Player Group and sending request to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:

                                    V = await SEnd_InV(4, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)

                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Player Group invitation sent successfully to {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 6-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/roommsg'):
                            print('Processing room message command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /roommsg (room_id) (message)\nExample: /roommsg 489775386 Hello room!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                message = " ".join(parts[2:])
        
                                initial_msg = f"[B][C][00FF00]📢 Sending to room {room_id}: {message}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Get bot UID
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else 13699776666
            
                                    # Send room chat using leaked packet structure
                                    room_chat_packet = await send_room_chat_enhanced(message, room_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', room_chat_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ Message sent to room {room_id}!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"✅ Room message sent to {room_id}: {message}")
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nSending Group Invitation...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        
           
           
                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('Processing reject spam command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /reject (target_uid)\nExample: /reject 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"[B][C][1E90FF]🌀 Started Reject Spam on: {target_uid}\n🌀 Packets: 150 each type\n🌀 Interval: 0.2 seconds\n"
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][00FF00]✅ Reject spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active reject spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                                              
                                    
                                    
                        # Individual command handlers for /s1 to /s5
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                            #ALL BADGE SPAM REQUEST 
                        if inPuTMsG.strip().startswith('/spam'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ Usage: /spam <uid>\nExample: /spam 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                total_requests = 10  # total join requests
                                sequence = ['s1', 's2', 's3', 's4', 's5']  # all badge commands

                                # Send initial consolidated message
                                initial_msg = f"[B][C][1E90FF]🌀 Request received! Preparing to spam {target_uid} with all badges...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)

                                count = 0
                                while count < total_requests:
                                    for cmd in sequence:
                                        if count >= total_requests:
                                            break
                                        # Build a fake command string like "/s1 123456789"
                                        fake_command = f"/{cmd} {target_uid}"
                                        await handle_badge_command(cmd, fake_command, uid, chat_id, key, iv, region, response.Data.chat_type)
                                        count += 1

                                # Success message after all 30 requests
                                success_msg = f"[B][C][00FF00]✅ Successfully sent {total_requests} Join Requests!\n🎯 Target: {target_uid}\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                      
                                                
                                              
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('/join'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                sender_uid = response.Data.uid  # Get the UID of person who sent the command            
                                bot_uid = LoGinDaTaUncRypTinG.AccountUID
        
                                initial_message = f"[B][C]{get_random_color()}\nJoining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(sender_uid, bot_uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"Dual emote failed but join succeeded: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Joined squad: {CodE}!\n💍 Dual Rings emote activated!\n🤖 Bot + You = 💕\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"Regular join failed: {e}")
                                    
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ghost (team_code)\nExample: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGhost joining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][00FF00]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Ghost join failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW LAG COMMAND
                        if inPuTMsG.strip().startswith('/lag '):
                            print('Processing lag command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Stop any existing lag task
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                
                                # Start new lag task
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nAction: Rapid join/leave\nSpeed: Ultra fast (milliseconds)\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # STOP LAG COMMAND
                        if inPuTMsG.strip() == '/stop lag':
                            if lag_task and not lag_task.done():
                                lag_running = False
                                lag_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Lag attack stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active lag attack to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nLeaving current squad...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Left the squad successfully!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/start'):
                            # Process /start command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Match starting command sent!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                            

                        # Emote command - works in all chat types
                        if inPuTMsG.strip().startswith('/e'):
                            print(f'Processing emote command in chat type: {response.Data.chat_type}')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /e (uid) (emote_id)\nExample: /e 123456789 909000001\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                                
                            initial_message = f'[B][C]{get_random_color()}\nSending emote to target...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                            uid2 = uid3 = uid4 = uid5 = None
                            s = False
                            target_uids = []

                            try:
                                target_uid = int(parts[1])
                                target_uids.append(target_uid)
                                uid2 = int(parts[2]) if len(parts) > 2 else None
                                if uid2: target_uids.append(uid2)
                                uid3 = int(parts[3]) if len(parts) > 3 else None
                                if uid3: target_uids.append(uid3)
                                uid4 = int(parts[4]) if len(parts) > 4 else None
                                if uid4: target_uids.append(uid4)
                                uid5 = int(parts[5]) if len(parts) > 5 else None
                                if uid5: target_uids.append(uid5)
                                idT = int(parts[-1])  # Last part is emote ID
                                
                                raw_idT = idT
                                idT = resolve_emote_id(idT)
                                

                            except ValueError as ve:
                                print("ValueError:", ve)
                                s = True
                            except Exception as e:
                                print(f"Error parsing emote command: {e}")
                                s = True

                            if not s:
                                try:
                                    for target in target_uids:
                                        H = await Emote_k(target, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Emote {idT} sent to {len(target_uids)} player(s)!\nTargets: {', '.join(map(str, target_uids))}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending emote: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Invalid UID format. Usage: /e (uid) (emote_id)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                                # /lvup command - Auto Start Bot
                        if inPuTMsG.strip().startswith('/lw'):
                            print('Processing /lvup auto-start command')
                            global auto_start_running, auto_start_teamcode, stop_auto, auto_start_task
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lw (team_code)\nExample: /lw 123456\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Check if numeric
                                if not team_code.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Team code must be numbers only!\nExample: /lw 123456\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                
                                # Check if already running
                                if auto_start_running:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Auto start already running for team {auto_start_teamcode}!\nUse /stop to stop first.\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                
                                # Start auto start
                                global auto_start_task, stop_auto
                                stop_auto = False
                                auto_start_running = True
                                auto_start_teamcode = team_code
                                
                                # Send initial message
                                initial_msg = f"""
[B][C][00FFFF]🤖 AUTO START BOT ACTIVATED!

🎯 Team Code: {team_code}
⚡ Action: Join → Start → Wait → Leave → Repeat
⏰ Start Spam: {start_spam_duration} seconds
⏳ Wait Time: {wait_after_match} seconds
🔄 Loop: Continuous 24x7

💡 To stop: /stop
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                
                                # Start auto loop in background
                                auto_start_task = asyncio.create_task(
                                    auto_start_loop(team_code, uid, chat_id, response.Data.chat_type, key, iv, region)
                                )
                        

                        if inPuTMsG.strip().startswith('/stop'):
                            print('Processing /stop auto-stop command')
                            
                                # Start auto start
                            stop_auto = True
                            auto_start_running = False
                            auto_start_teamcode = None
                                
                                # Send initial message
                            initial_msg = f"""
[B][C][00FFFF]🤖 AUTO START BOT STOPED !

🎯 Team Code: {team_code}
⚡ Action: Join → Start → Wait → Leave → Repeat
⏰ Start Spam: {start_spam_duration} seconds
⏳ Wait Time: {wait_after_match} seconds
🔄 Loop: Continuous 24x7

💡 To on: /lw [team_code]
"""
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                

                        # EVO CYCLE START COMMAND - @evos
                        if inPuTMsG.strip().startswith('@evos'):
                            print('Processing evo cycle start command in any chat type')
                            # Declare global variables

                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed @evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "@evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(evo_cycle_spam(uids, key, iv, region))
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Target: Yourself\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Targets: Yourself + {len(uids)-1} other players\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - @sevos
                        if inPuTMsG.strip() == '@sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('Processing fast emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /fast uid1 [uid2] [uid3] [uid4] [1-410]\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and [1-410]
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = ALL_EMOTES.get(int(part))
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /fast uid1 [uid2] [uid3] [uid4] [1-410]\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast emote spam started!\nTargets: {len(uids)} players\nEmote: {emote_id}\nSpam count: 25 times\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('Processing custom emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /p (uid) [1-410] (times)\nExample: /p 123456789 [1-410] 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = ALL_EMOTES.get(int(parts[2]))
                                    times = int(parts[3])
                                    
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 100:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom emote spam started!\nTarget: {target_uid}\nEmote: {emote_id}\nTimes: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Usage: /p (uid) [1-410] (times)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        
                        # NEW PLAY COMMANDS
                        if inPuTMsG.strip().startswith('/play '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /play uid1 [uid2] [uid3] [uid4] number(1-410)\nExample: /play 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-410 (1,2 or 3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /play uid1 [uid2] [uid3] [uid4] number(1-410)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in ALL_EMOTES:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-410 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await play_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use (1-410) only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        

                        # NEW EVO COMMANDS
                        if inPuTMsG.strip().startswith('/evo '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-100)\nExample: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending evolution emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('Processing evo_fast command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-100)\nExample: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/evo_c '):
                            print('Processing evo_c command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-100) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-100) time(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Time must be between 1-100 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution fast spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution custom spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip().lower() in ("help", "/help", "menu", "/menu", "commands"):
                            print(f"Help command detected from UID: {uid} in chat type: {response.Data.chat_type}")

                            # Header
                            header = f"[b][c]{get_random_color()}Hey User Welcome To FF TCP BOT"
                            await safe_send_message(response.Data.chat_type, header, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Group Commands ─────
                            group_commands = """[C][B][FFD700]═══⚡ ADVANCED COMMANDS ⚡═══[00FF00][B]
├─ [00FF00]Create 3-Player Group
│  └─ [00AAFF]/3
├─ [00FF00]Create 5-Player Group
│  └─ [00AAFF]/5
├─ [00FF00]Create 6-Player Group
│  └─ [00AAFF]/6
├─ [00FF00]Invite Player in Team
│  └─ [00AAFF]/inv [uid]
├─ [00FF00]Join Bot in Team
│  └─ [00AAFF]/join [team_code]
└─ [00FF00]Leave Bot Team
   └─ [00AAFF]/exit
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, group_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Advanced Commands ─────
                            advanced_commands = """[C][B][800080]═══⚡ ADVANCED COMMANDS ⚡═══[00FF00][B]
├─ [00FF00]Start Level up bot
│  └─ [00AAFF]/lw [team code]
├─ [00FF00]Stop level up bot
│  └─ [00AAFF]/stop
├─ [00FF00]Equip Rare Bundle
│  └─ [00AAFF]/bundle [code]
├─ [00FF00]Lag Attack Team
│  └─ [00AAFF]/lag [code]
├─ [00FF00]Stop Lag Attack
│  └─ [00AAFF]/stop lag
└─ [00FF00]Reject Spam
   └─ [00AAFF]/reject [uid]
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, advanced_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Emote Commands ─────
                            emote_commands = """[C][B][32CD32]═══⚡ EMOTE COMMANDS ⚡═══[7CFC00][B]
├─ [7CFC00]Send Single Emote
│  └─ [32CD32]/play [uid] [1-410]
├─ [7CFC00]Fast Emote (25x)
│  └─ [32CD32]/fast [uid] [1-410]
├─ [7CFC00]Custom Emote (X Times)
│  └─ [32CD32]/p [uid] [1-410] [X]
├─ [7CFC00]Emote Menu
│  └─ [32CD32]/emote
└─ [7CFC00]Custom Emote (Using Id)
   └─ [32CD32]/e [uid] [id]
[7CFC00]━━━━━━━━━━━━[32CD32]"""
                            await safe_send_message(response.Data.chat_type, emote_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Evolution Emote Commands ─────
                            evo_commands = """[C][B][00AAFF]═══⚡ EVOLUTION EMOTES ⚡═══[00FF00][B]
├─ [00FF00]Send Evolution Emote
│  └─ [00AAFF]/evo [uid] [1-100]
├─ [00FF00]Fast Evo (25x)
│  └─ [00AAFF]/evo_fast [uid] [1-100]
├─ [00FF00]Custom Evo (X times)
│  └─ [00AAFF]/evo_c [uid] [1-100] [x]
├─ [00FF00]Auto Cycle All Evo Emotes
│  └─ [00AAFF]@evos [uid]
└─ [00FF00]Stop Evo Emote Cycle
   └─ [00AAFF]@sevos
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, evo_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            

                            # ───── Badges Commands ─────
                            badge_commands = """[C][B][00AAFF]═══⚡ BADGE JOIN REQUESTS ⚡═══[00FF00][B]
├─ [00FF00]Join Req Craftland Badge
│  └─ [00AAFF]/s1 [uid]
├─ [00FF00]Join Req New V-Badge
│  └─ [00AAFF]/s2 [uid]
├─ [00FF00]Join Req Moderator Badge
│  └─ [00AAFF]/s3 [uid]
├─ [00FF00]Join Req Small V-Badge
│  └─ [00AAFF]/s4 [uid]
├─ [00FF00]Join Req Pro Badge
│  └─ [00AAFF]/s5 [uid]
└─ [00FF00]Join Requests All Badge
   └─ [00AAFF]/spam [uid]
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, badge_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
                            

        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

                            
async def MaiiiinE():
    
    Uid , Pw = 'paste_uid_here','paste_password_here'
    

    open_id , access_token = await GeNeRaTeAccEss(Uid , Pw)
    if not open_id or not access_token: print("ErroR - InvaLid AccounT") ; return None
    
    PyL = await EncRypTMajoRLoGin(open_id , access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: print("TarGeT AccounT => BannEd / NoT ReGisTeReD ! ") ; return None
    
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    if not UrL: print("Target Account => Banned ! ") ; return None
    # In the MaiiiinE function, find and comment out these print statements:
    os.system('clear')
    print("🔄 Starting TCP Connections...")
    print("📡 Connecting to Free Fire servers...")
    print("🌐 Server connection established")

    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    print("🔐 Authentication successful")
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: print("ErroR - GeTinG PorTs From LoGin DaTa !") ; return None
            
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP , OnLineporT = OnLinePorTs.split(":")
    ChaTiP , ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName
    
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen, region))  

    os.system('clear')
    print("Initializing FF TCP BOT...")
    print("┌────────────────────────────────────┐")
    print("│ █████████████░░░░░░░░░░░░░░░░░░ │")
    print("└────────────────────────────────────┘")
    time.sleep(0.5)
    os.system('clear')
    print("Connecting to Free Fire servers...")
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████░░░░░░░░░░░░ │")
    print("└────────────────────────────────────┘")
    time.sleep(0.5)
    os.system('clear')

    print("🤖 BOT - ONLINE")
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")
    print(f"🔹 UID: {TarGeT}")
    print(f"🔹 Name: {acc_name}")
    print(f"🔹 Status: 🟢 READY")
    print("")
    print("💡 Type /help for commands")
    await asyncio.gather(task1, task2)
    time.sleep(0.5)
    os.system('clear')
    await ready_event.wait()
    await asyncio.sleep(1)

    os.system('clear')
    print(render('TCP', colors=['white', 'green'], align='center'))
    print('')
    print("🤖 FF TCP BOT - ONLINE")
    print(f"🔹 UID: {TarGeT}")
    print(f"🔹 Name: {acc_name}")
    print(f"🔹 Status: 🟢 READY")
   
def handle_keyboard_interrupt(signum, frame):
    """Clean handling for Ctrl+C"""
    print("\n\n🛑 Bot shutdown requested...")
    print("👋 Thanks for using FF TCP BOT")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_keyboard_interrupt)
     
        
async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except KeyboardInterrupt:
            print("\n\n🛑 Bot shutdown by user")
            print("👋 Thanks for using FF TCP BOT!")
            break
        except asyncio.TimeoutError: print("Token ExpiRed ! , ResTartinG")
        except Exception as e: print(f"ErroR TcP - {e} => ResTarTinG ...")

if __name__ == '__main__':
    asyncio.run(StarTinG())