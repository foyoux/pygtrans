"""ReadAloud"""
import asyncio
import json
import os
import re
import uuid
from datetime import datetime
from enum import Enum
from typing import Union

import requests
import websockets


class _VoiceType:
    """VoiceType"""

    def __init__(
            self,
            Name: str = None,
            ShortName: str = None,
            Gender: str = None,
            Locale: str = None,
            SuggestedCodec: str = None,
            FriendlyName: str = None,
            Status: str = None
    ):
        self.Name = Name
        self.ShortName = ShortName
        self.Gender = Gender
        self.Locale = Locale
        self.SuggestedCodec = SuggestedCodec
        self.FriendlyName = FriendlyName
        self.Status = Status


class Voice(Enum):
    """Voice

    Referer: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support
    """

    ar_EG_SalmaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ar-EG, SalmaNeural)',
        ShortName='ar-EG-SalmaNeural', Gender='Female', Locale='ar-EG',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Salma Online (Natural) - Arabic (Egypt)', Status='GA')
    ar_SA_ZariyahNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ar-SA, ZariyahNeural)',
        ShortName='ar-SA-ZariyahNeural', Gender='Female', Locale='ar-SA',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Zariyah Online (Natural) - Arabic (Saudi Arabia)',
        Status='GA')
    bg_BG_KalinaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (bg-BG, KalinaNeural)',
        ShortName='bg-BG-KalinaNeural', Gender='Female', Locale='bg-BG',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Kalina Online (Natural) - Bulgarian (Bulgaria)',
        Status='GA')
    ca_ES_JoanaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ca-ES, JoanaNeural)',
        ShortName='ca-ES-JoanaNeural', Gender='Female', Locale='ca-ES',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Joana Online (Natural) - Catalan (Spain)', Status='GA')
    cs_CZ_VlastaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (cs-CZ, VlastaNeural)',
        ShortName='cs-CZ-VlastaNeural', Gender='Female', Locale='cs-CZ',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Vlasta Online (Natural) - Czech (Czech)', Status='GA')
    cy_GB_NiaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (cy-GB, NiaNeural)',
        ShortName='cy-GB-NiaNeural', Gender='Female', Locale='cy-GB',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Nia Online (Natural) - Welsh (United Kingdom)', Status='GA')
    da_DK_ChristelNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (da-DK, ChristelNeural)',
        ShortName='da-DK-ChristelNeural', Gender='Female', Locale='da-DK',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Christel Online (Natural) - Danish (Denmark)',
        Status='GA')
    de_AT_IngridNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (de-AT, IngridNeural)',
        ShortName='de-AT-IngridNeural', Gender='Female', Locale='de-AT',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Ingrid Online (Natural) - German (Austria)', Status='GA')
    de_CH_LeniNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (de-CH, LeniNeural)',
        ShortName='de-CH-LeniNeural', Gender='Female', Locale='de-CH',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Leni Online (Natural) - German (Switzerland)', Status='GA')
    de_DE_KatjaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (de-DE, KatjaNeural)',
        ShortName='de-DE-KatjaNeural', Gender='Female', Locale='de-DE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Katja Online (Natural) - German (Germany)', Status='GA')
    el_GR_AthinaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (el-GR, AthinaNeural)',
        ShortName='el-GR-AthinaNeural', Gender='Female', Locale='el-GR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Athina Online (Natural) - Greek (Greece)', Status='GA')
    en_AU_NatashaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-AU, NatashaNeural)',
        ShortName='en-AU-NatashaNeural', Gender='Female', Locale='en-AU',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Natasha Online (Natural) - English (Australia)',
        Status='GA')
    en_CA_ClaraNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-CA, ClaraNeural)',
        ShortName='en-CA-ClaraNeural', Gender='Female', Locale='en-CA',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Clara Online (Natural) - English (Canada)', Status='GA')
    en_GB_MiaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-GB, MiaNeural)',
        ShortName='en-GB-MiaNeural', Gender='Female', Locale='en-GB',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Mia Online (Natural) - English (United Kingdom)', Status='GA')
    en_IE_EmilyNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-IE, EmilyNeural)',
        ShortName='en-IE-EmilyNeural', Gender='Female', Locale='en-IE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Emily Online (Natural) - English (Ireland)', Status='GA')
    en_IN_NeerjaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-IN, NeerjaNeural)',
        ShortName='en-IN-NeerjaNeural', Gender='Female', Locale='en-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Neerja Online (Natural) - English (India)', Status='GA')
    en_PH_RosaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-PH, RosaNeural)',
        ShortName='en-PH-RosaNeural', Gender='Female', Locale='en-PH',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Rosa Online (Natural) - English (Philippines)', Status='GA')
    en_US_AriaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-US, AriaNeural)',
        ShortName='en-US-AriaNeural', Gender='Female', Locale='en-US',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Aria Online (Natural) - English (United States)', Status='GA')
    en_US_GuyNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-US, GuyNeural)',
        ShortName='en-US-GuyNeural', Gender='Male', Locale='en-US',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Guy Online (Natural) - English (United States)', Status='GA')
    en_US_JennyNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-US, JennyNeural)',
        ShortName='en-US-JennyNeural', Gender='Female', Locale='en-US',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Jenny Online (Natural) - English (United States)',
        Status='GA')
    en_ZA_LeahNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (en-ZA, LeahNeural)',
        ShortName='en-ZA-LeahNeural', Gender='Female', Locale='en-ZA',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Leah Online (Natural) - English (South Africa)', Status='GA')
    es_AR_ElenaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (es-AR, ElenaNeural)',
        ShortName='es-AR-ElenaNeural', Gender='Female', Locale='es-AR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Elena Online (Natural) - Spanish (Argentina)', Status='GA')
    es_CO_SalomeNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (es-CO, SalomeNeural)',
        ShortName='es-CO-SalomeNeural', Gender='Female', Locale='es-CO',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Salome Online (Natural) - Spanish (Colombia)', Status='GA')
    es_ES_ElviraNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (es-ES, ElviraNeural)',
        ShortName='es-ES-ElviraNeural', Gender='Female', Locale='es-ES',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Elvira Online (Natural) - Spanish (Spain)', Status='GA')
    es_MX_DaliaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (es-MX, DaliaNeural)',
        ShortName='es-MX-DaliaNeural', Gender='Female', Locale='es-MX',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Dalia Online (Natural) - Spanish (Mexico)', Status='GA')
    et_EE_AnuNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (et-EE, AnuNeural)',
        ShortName='et-EE-AnuNeural', Gender='Female', Locale='et-EE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Anu Online (Natural) - Estonian (Estonia)', Status='GA')
    fi_FI_NooraNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (fi-FI, NooraNeural)',
        ShortName='fi-FI-NooraNeural', Gender='Female', Locale='fi-FI',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Noora Online (Natural) - Finnish (Finland)', Status='GA')
    fr_BE_CharlineNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (fr-BE, CharlineNeural)',
        ShortName='fr-BE-CharlineNeural', Gender='Female', Locale='fr-BE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Charline Online (Natural) - French (Belgium)',
        Status='GA')
    fr_CA_SylvieNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (fr-CA, SylvieNeural)',
        ShortName='fr-CA-SylvieNeural', Gender='Female', Locale='fr-CA',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Sylvie Online (Natural) - French (Canada)', Status='GA')
    fr_CH_ArianeNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (fr-CH, ArianeNeural)',
        ShortName='fr-CH-ArianeNeural', Gender='Female', Locale='fr-CH',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Ariane Online (Natural) - French (Switzerland)',
        Status='GA')
    fr_FR_DeniseNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (fr-FR, DeniseNeural)',
        ShortName='fr-FR-DeniseNeural', Gender='Female', Locale='fr-FR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Denise Online (Natural) - French (France)', Status='GA')
    ga_IE_OrlaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ga-IE, OrlaNeural)',
        ShortName='ga-IE-OrlaNeural', Gender='Female', Locale='ga-IE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Orla Online (Natural) - Irish(Ireland)', Status='GA')
    gu_IN_DhwaniNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (gu-IN, DhwaniNeural)',
        ShortName='gu-IN-DhwaniNeural', Gender='Female', Locale='gu-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Dhwani Online (Natural) - Gujarati (India)', Status='GA')
    he_IL_HilaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (he-IL, HilaNeural)',
        ShortName='he-IL-HilaNeural', Gender='Female', Locale='he-IL',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Hila Online (Natural) - Hebrew (Israel)', Status='GA')
    hi_IN_SwaraNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (hi-IN, SwaraNeural)',
        ShortName='hi-IN-SwaraNeural', Gender='Female', Locale='hi-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Swara Online (Natural) - Hindi (India)', Status='GA')
    hr_HR_GabrijelaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (hr-HR, GabrijelaNeural)',
        ShortName='hr-HR-GabrijelaNeural', Gender='Female', Locale='hr-HR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Gabrijela Online (Natural) - Croatian (Croatia)',
        Status='GA')
    hu_HU_NoemiNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (hu-HU, NoemiNeural)',
        ShortName='hu-HU-NoemiNeural', Gender='Female', Locale='hu-HU',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Noemi Online (Natural) - Hungarian (Hungary)', Status='GA')
    id_ID_GadisNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (id-ID, GadisNeural)',
        ShortName='id-ID-GadisNeural', Gender='Female', Locale='id-ID',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Gadis Online (Natural) - Indonesian (Indonesia)',
        Status='GA')
    it_IT_ElsaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (it-IT, ElsaNeural)',
        ShortName='it-IT-ElsaNeural', Gender='Female', Locale='it-IT',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Elsa Online (Natural) - Italian (Italy)', Status='GA')
    ja_JP_NanamiNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ja-JP, NanamiNeural)',
        ShortName='ja-JP-NanamiNeural', Gender='Female', Locale='ja-JP',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Nanami Online (Natural) - Japanese (Japan)', Status='GA')
    ko_KR_SunHiNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ko-KR, SunHiNeural)',
        ShortName='ko-KR-SunHiNeural', Gender='Female', Locale='ko-KR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft SunHi Online (Natural) - Korean (Korea)', Status='GA')
    lt_LT_OnaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (lt-LT, OnaNeural)',
        ShortName='lt-LT-OnaNeural', Gender='Female', Locale='lt-LT',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Ona Online (Natural) - Lithuanian (Lithuania)', Status='GA')
    lv_LV_EveritaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (lv-LV, EveritaNeural)',
        ShortName='lv-LV-EveritaNeural', Gender='Female', Locale='lv-LV',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Everita Online (Natural) - Latvian (Latvia)', Status='GA')
    mr_IN_AarohiNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (mr-IN, AarohiNeural)',
        ShortName='mr-IN-AarohiNeural', Gender='Female', Locale='mr-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Aarohi Online (Natural) - Marathi (India)', Status='GA')
    ms_MY_YasminNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ms-MY, YasminNeural)',
        ShortName='ms-MY-YasminNeural', Gender='Female', Locale='ms-MY',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Yasmin Online (Natural) - Malay (Malaysia)', Status='GA')
    mt_MT_GraceNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (mt-MT, GraceNeural)',
        ShortName='mt-MT-GraceNeural', Gender='Female', Locale='mt-MT',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Grace Online (Natural) - Maltese (Malta)', Status='GA')
    nb_NO_PernilleNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (nb-NO, PernilleNeural)',
        ShortName='nb-NO-PernilleNeural', Gender='Female', Locale='nb-NO',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Pernille Online (Natural) - Norwegian (Bokmål, Norway)',
        Status='GA')
    nl_BE_DenaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (nl-BE, DenaNeural)',
        ShortName='nl-BE-DenaNeural', Gender='Female', Locale='nl-BE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Dena Online (Natural) - Dutch (Belgium)', Status='GA')
    nl_NL_ColetteNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (nl-NL, ColetteNeural)',
        ShortName='nl-NL-ColetteNeural', Gender='Female', Locale='nl-NL',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Colette Online (Natural) - Dutch (Netherlands)',
        Status='GA')
    pl_PL_ZofiaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (pl-PL, ZofiaNeural)',
        ShortName='pl-PL-ZofiaNeural', Gender='Female', Locale='pl-PL',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Zofia Online (Natural) - Polish (Poland)', Status='GA')
    pt_BR_FranciscaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (pt-BR, FranciscaNeural)',
        ShortName='pt-BR-FranciscaNeural', Gender='Female', Locale='pt-BR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Francisca Online (Natural) - Portuguese (Brazil)',
        Status='GA')
    pt_PT_RaquelNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (pt-PT, RaquelNeural)',
        ShortName='pt-PT-RaquelNeural', Gender='Female', Locale='pt-PT',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Raquel Online (Natural) - Portuguese (Portugal)',
        Status='GA')
    ro_RO_AlinaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ro-RO, AlinaNeural)',
        ShortName='ro-RO-AlinaNeural', Gender='Female', Locale='ro-RO',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Alina Online (Natural) - Romanian (Romania)', Status='GA')
    ru_RU_SvetlanaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ru-RU, SvetlanaNeural)',
        ShortName='ru-RU-SvetlanaNeural', Gender='Female', Locale='ru-RU',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Svetlana Online (Natural) - Russian (Russia)',
        Status='GA')
    sk_SK_ViktoriaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (sk-SK, ViktoriaNeural)',
        ShortName='sk-SK-ViktoriaNeural', Gender='Female', Locale='sk-SK',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Viktoria Online (Natural) - Slovak (Slovakia)',
        Status='GA')
    sl_SI_PetraNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (sl-SI, PetraNeural)',
        ShortName='sl-SI-PetraNeural', Gender='Female', Locale='sl-SI',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Petra Online (Natural) - Slovenian (Slovenia)', Status='GA')
    sv_SE_SofieNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (sv-SE, SofieNeural)',
        ShortName='sv-SE-SofieNeural', Gender='Female', Locale='sv-SE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Sofie Online (Natural) - Swedish (Sweden)', Status='GA')
    sw_KE_ZuriNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (sw-KE, ZuriNeural)',
        ShortName='sw-KE-ZuriNeural', Gender='Female', Locale='sw-KE',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Zuri Online (Natural) - Swahili (Kenya)', Status='GA')
    ta_IN_PallaviNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ta-IN, PallaviNeural)',
        ShortName='ta-IN-PallaviNeural', Gender='Female', Locale='ta-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Pallavi Online (Natural) - Tamil (India)', Status='GA')
    te_IN_ShrutiNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (te-IN, ShrutiNeural)',
        ShortName='te-IN-ShrutiNeural', Gender='Female', Locale='te-IN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Shruti Online (Natural) - Telugu (India)', Status='GA')
    th_TH_PremwadeeNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (th-TH, PremwadeeNeural)',
        ShortName='th-TH-PremwadeeNeural', Gender='Female', Locale='th-TH',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Premwadee Online (Natural) - Thai (Thailand)',
        Status='GA')
    tr_TR_EmelNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (tr-TR, EmelNeural)',
        ShortName='tr-TR-EmelNeural', Gender='Female', Locale='tr-TR',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Emel Online (Natural) - Turkish (Turkey)', Status='GA')
    uk_UA_PolinaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (uk-UA, PolinaNeural)',
        ShortName='uk-UA-PolinaNeural', Gender='Female', Locale='uk-UA',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Polina Online (Natural) - Ukrainian (Ukraine)', Status='GA')
    ur_PK_UzmaNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (ur-PK, UzmaNeural)',
        ShortName='ur-PK-UzmaNeural', Gender='Female', Locale='ur-PK',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Uzma Online (Natural) - Urdu (Pakistan)', Status='GA')
    vi_VN_HoaiMyNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (vi-VN, HoaiMyNeural)',
        ShortName='vi-VN-HoaiMyNeural', Gender='Female', Locale='vi-VN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft HoaiMy Online (Natural) - Vietnamese (Vietnam)',
        Status='GA')
    zh_CN_XiaoxiaoNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (zh-CN, XiaoxiaoNeural)',
        ShortName='zh-CN-XiaoxiaoNeural', Gender='Female', Locale='zh-CN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Xiaoxiao Online (Natural) - Chinese (Mainland)',
        Status='GA')
    zh_CN_YunyangNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)',
        ShortName='zh-CN-YunyangNeural', Gender='Female', Locale='zh-CN',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft Yunyang Online (Natural) - Chinese (Mainland)',
        Status='GA')
    zh_HK_HiuMaanNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (zh-HK, HiuMaanNeural)',
        ShortName='zh-HK-HiuMaanNeural', Gender='Female', Locale='zh-HK',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft HiuMaan Online (Natural) - Chinese (Hong Kong)',
        Status='GA')
    zh_TW_HsiaoChenNeural = _VoiceType(
        Name='Microsoft Server Speech Text to Speech Voice (zh-TW, HsiaoChenNeural)',
        ShortName='zh-TW-HsiaoChenNeural', Gender='Female', Locale='zh-TW',
        SuggestedCodec='audio-24khz-48kbitrate-mono-mp3',
        FriendlyName='Microsoft HsiaoChen Online (Natural) - Chinese (Taiwan)',
        Status='GA')


class OutputFormat(Enum):
    """OutputFormat

    Referer: https://docs.microsoft.com/zh-cn/dotnet/api/microsoft.cognitiveservices.speech.speechsynthesisoutputformat?view=azure-dotnet
    """
    Audio16Khz128KBitRateMonoMp3 = 'audio-16khz-128kbitrate-mono-mp3'
    Audio16Khz32KBitRateMonoMp3 = 'audio-16khz-32kbitrate-mono-mp3'
    Audio16Khz64KBitRateMonoMp3 = 'audio-16khz-64kbitrate-mono-mp3'
    Audio24Khz160KBitRateMonoMp3 = 'audio-24khz-160kbitrate-mono-mp3'
    Audio24Khz48KBitRateMonoMp3 = 'audio-24khz-48kbitrate-mono-mp3'
    Audio24Khz96KBitRateMonoMp3 = 'audio-24khz-96kbitrate-mono-mp3'
    Audio48Khz192KBitRateMonoMp3 = 'audio-48khz-192kbitrate-mono-mp3'
    Audio48Khz96KBitRateMonoMp3 = 'audio-48khz-96kbitrate-mono-mp3'
    Ogg16Khz16BitMonoOpus = 'ogg-16khz-16bit-mono-opus'
    Ogg24Khz16BitMonoOpus = 'ogg-24khz-16bit-mono-opus'
    Ogg48Khz16BitMonoOpus = 'ogg-48khz-16bit-mono-opus'
    Raw16Khz16BitMonoPcm = 'raw-16khz-16bit-mono-pcm'
    Raw16Khz16BitMonoTrueSilk = 'raw-16khz-16bit-mono-truesilk'
    Raw24Khz16BitMonoPcm = 'raw-24khz-16bit-mono-pcm'
    Raw24Khz16BitMonoTrueSilk = 'raw-24khz-16bit-mono-truesilk'
    Raw48Khz16BitMonoPcm = 'raw-48khz-16bit-mono-pcm'
    Raw8Khz16BitMonoPcm = 'raw-8khz-16bit-mono-pcm'
    Raw8Khz8BitMonoALaw = 'raw-8khz-8bit-mono-alaw'
    Raw8Khz8BitMonoMULaw = 'raw-8khz-8bit-mono-mulaw'
    Riff16Khz16BitMonoPcm = 'riff-16khz-16bit-mono-pcm'
    Riff24Khz16BitMonoPcm = 'riff-24khz-16bit-mono-pcm'
    Riff48Khz16BitMonoPcm = 'riff-48khz-16bit-mono-pcm'
    Riff8Khz16BitMonoPcm = 'riff-8khz-16bit-mono-pcm'
    Riff8Khz8BitMonoALaw = 'riff-8khz-8bit-mono-alaw'
    Riff8Khz8BitMonoMULaw = 'riff-8khz-8bit-mono-mulaw'
    Webm16Khz16BitMonoOpus = 'webm-16khz-16bit-mono-opus'
    Webm24Khz16BitMonoOpus = 'webm-24khz-16bit-mono-opus'


class ReadAloud:
    """ReadAloud"""
    CHUNK = 10 ** 10
    TrustedClientToken = '6A5AA1D4EAFF4E9FB37E23D68491D6F4'

    def __init__(self, lang: Union[Voice, str] = Voice.zh_CN_XiaoxiaoNeural,
                 output_format: Union[OutputFormat, str] = OutputFormat.Audio48Khz192KBitRateMonoMp3,
                 rate: str = '+0%', pitch: str = '+0Hz', volume: str = '+0%'):
        if isinstance(lang, Voice):
            lang = lang.value.ShortName
        self.lang = lang
        if isinstance(output_format, OutputFormat):
            output_format = output_format.value
        self.output_format = output_format
        self.rate = rate
        self.pitch = pitch
        self.volume = volume
        self.azure_token = None

    def tts_edge(self, data: str, out: str = 'readaloud.mp3', voice: Union[Voice, str] = None,
                 output_format: Union[OutputFormat, str] = None,
                 rate: str = None, pitch: str = None, volume: str = None) -> str:
        """tts"""
        if voice is None:
            voice = self.lang
        elif isinstance(voice, Voice):
            voice = voice.value.ShortName

        if output_format is None:
            output_format = self.output_format
        elif isinstance(output_format, OutputFormat):
            output_format = output_format.value

        rate = rate or self.rate
        pitch = pitch or self.pitch
        volume = volume or self.volume

        asyncio.run(self.__tts_edge(data, out, voice, output_format, rate, pitch, volume))
        return os.path.abspath(out)

    @staticmethod
    async def __tts_edge(data: str, out: str,
                         voice: str, output_format: str,
                         rate: str = '+0%', pitch: str = '+0Hz', volume: str = '+0%'):
        """Edge大声朗读"""
        ConnectionId = uuid.uuid4().hex
        uri = f'wss://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1?TrustedClientToken={ReadAloud.TrustedClientToken}&ConnectionId={ConnectionId}'
        async with websockets.connect(
                uri, ssl=True, origin='chrome-extension://jdiccldimpdaibmpdkjnbmckianbfold',
                extra_headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
                    'origin': 'chrome-extension://jdiccldimpdaibmpdkjnbmckianbfold'
                }
        ) as ws:
            texts = iter([data[i: i + ReadAloud.CHUNK] for i in range(0, len(data), ReadAloud.CHUNK)])

            async def sub(text):
                """..."""
                print(text)
                await ws.send('\r\n'.join([
                    f'X-Timestamp: {datetime.utcnow().isoformat()[:-3]}',
                    f'Content-Type:application/json; charset=utf-8',
                    f'Path:speech.config',
                    '',
                    json.dumps({"context": {"synthesis": {"audio": {
                        "metadataoptions": {"sentenceBoundaryEnabled": False, "wordBoundaryEnabled": False},
                        "outputFormat": output_format}}}})
                ]))
                _id = uuid.uuid4().hex
                await ws.send('\r\n'.join([
                    f'X-RequestId:{_id}',
                    'Content-Type:application/ssml+xml',
                    f'X-Timestamp: {datetime.utcnow().isoformat()[:-3]}Z',
                    'Path:ssml',
                    '',
                    f"""<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'><voice  name='{voice}'><prosody pitch='{pitch}' rate ='{rate}' volume='{volume}'>{text}</prosody></voice></speak>"""
                ]))

            with open(out, 'wb') as mp3:
                await sub(next(texts))
                async for msg in ws:
                    if isinstance(msg, str) and msg.find('Path:turn.end') != -1:
                        try:
                            await sub(next(texts))
                        except StopIteration:
                            await ws.close()
                    if isinstance(msg, bytes):
                        bs = msg.split(b'\r\nPath:audio\r\n')[-1]
                        mp3.write(bs)

    def tts_azure(self, data: str, out: str = 'readaloud.mp3', voice: Union[Voice, str] = None,
                  output_format: Union[OutputFormat, str] = None,
                  rate: str = None, pitch: str = None, volume: str = None) -> str:
        """tts"""

        if voice is None:
            voice = self.lang
        elif isinstance(voice, Voice):
            voice = voice.value.ShortName

        if output_format is None:
            output_format = self.output_format
        elif isinstance(output_format, OutputFormat):
            output_format = output_format.value

        rate = rate or self.rate
        pitch = pitch or self.pitch
        volume = volume or self.volume

        try:
            asyncio.run(self.__tts_azure(data, out, voice, output_format, rate, pitch, volume))
        except:
            self.azure_token = None
            asyncio.run(self.__tts_azure(data, out, voice, output_format, rate, pitch, volume))
        return os.path.abspath(out)

    @staticmethod
    def _get_azure_token():
        return re.findall(
            'token: "([^"]+)"',
            requests.get(
                'https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/'
            ).text)[0]

    async def __tts_azure(self, data: str, out: str,
                          voice: str, output_format: str,
                          rate: str = '+0%', pitch: str = '+0Hz', volume: str = '+0%'):
        """Edge大声朗读"""
        if self.azure_token is None:
            self.azure_token = ReadAloud._get_azure_token()
        uri = f'wss://eastus.tts.speech.microsoft.com/cognitiveservices/websocket/v1?Authorization={self.azure_token}&X-ConnectionId={uuid.uuid4().hex.upper()}'
        async with websockets.connect(
                uri, ssl=True,
                extra_headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
                }
        ) as ws:
            texts = iter([data[i: i + ReadAloud.CHUNK] for i in range(0, len(data), ReadAloud.CHUNK)])

            async def sub(text):
                """..."""
                print(text)
                _id = uuid.uuid4().hex
                await ws.send('\r\n'.join([
                    'Path: synthesis.context',
                    f'X-RequestId: {_id}',
                    f'X-Timestamp: {datetime.utcnow().isoformat()[:-3] + "Z"}',
                    'Content-Type: application/json',
                    '',
                    json.dumps({"synthesis": {"audio": {
                        "metadataOptions": {
                            "bookmarkEnabled": False, "sentenceBoundaryEnabled": False, "visemeEnabled": False,
                            "wordBoundaryEnabled": False},
                        "outputFormat": output_format},
                        "language": {"autoDetection": False}
                    }})
                ]))
                await ws.send('\r\n'.join([
                    'Path: ssml',
                    f'X-RequestId: {_id}',
                    f'X-Timestamp: {datetime.utcnow().isoformat()[:-3] + "Z"}',
                    'Content-Type: application/ssml+xml',
                    '',
                    f'<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="{voice}"><prosody rate="{rate}" pitch="{pitch}" volume="{volume}">{text}</prosody></voice></speak>'
                ]))

            with open(out, 'wb') as mp3:
                await sub(next(texts))
                async for msg in ws:
                    if isinstance(msg, str) and msg.find('Path:turn.end') != -1:
                        try:
                            await sub(next(texts))
                        except StopIteration:
                            await ws.close()
                    if isinstance(msg, bytes):
                        bs = msg.split(b'\r\nPath:audio\r\n')[-1]
                        mp3.write(bs)
