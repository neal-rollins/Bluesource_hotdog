import time
from hotdog.BasePage import HotDogBasePage
from hotdog.FindEither import FindEither
from webium import Find
import webium

webium.settings.implicit_wait = 5

class CBCWebBase(HotDogBasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
