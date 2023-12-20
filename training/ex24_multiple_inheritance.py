from my_utils import dir2


class Phone:
    def __init__(self, **kwargs):
        print('Phone.__init__() called')
        self.phone_model = kwargs.get('phone_model')

    def make_call(self):
        print('making a call...')

    def print_info(self):
        print(f'phone_model = {self.phone_model}')


class Camera:
    def __init__(self, **kwargs):
        print('Camera.__init__() called')
        self.resoltion = kwargs.get('resolution', '5MP')

    def take_picture(self):
        print('taking a picture...')

    def print_info(self):
        print(f'resoltion = {self.resoltion}')

class MobilePhone(Phone):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('MobilePhone.__init__() called')
        self.keypad_type = kwargs.get('keypad_type', 'qwerty')

    def send_sms(self):
        print('sending a message')

    def print_info(self):
        super().print_info()
        print(f'keypad_type = {self.keypad_type}')


class Radio:
    def __init__(self, **kwargs):
        print('Radio.__init__() called')
        self.frequency_type = kwargs.get('frequency_type', 'AM+FM')

    def tune_to_station(self):
        print('tuning to station...')

    def print_info(self):
        print(f'frequency_type = {self.frequency_type}')


class MusicPlayer():
    def __init__(self, **kwargs):
        print('MusicPlayer.__init__() called')
        self.format_supported = kwargs.get('format_supported', 'MP3,WAV')

    def play_song(self):
        print('playing song...')

    def print_info(self):
        print(f'format_supported = {self.format_supported}')


class SmartPhone(Camera, MobilePhone, MusicPlayer, Radio):
    def __init__(self, **kwargs):
        MobilePhone.__init__(self, **kwargs)
        Camera.__init__(self, **kwargs)
        Radio.__init__(self, **kwargs)
        MusicPlayer.__init__(self, **kwargs)
        print('SmartPhone.__init__() called')
        self.cpu_speed = kwargs.get('cpu_speed', '1.2GHz')

    def print_info(self):
        MobilePhone.print_info(self)
        Camera.print_info(self)
        Radio.print_info(self)
        MusicPlayer.print_info(self)
        print(f'cpu_speed = {self.cpu_speed}')


if __name__ == '__main__':
    sp = SmartPhone(frequency_type='FM', phone_model='iPhone3', resolution='50MP', format_supported='MP3/4, WAV', cpu_speed='2.1GHz')
    print(dir2(sp))
    print(SmartPhone.mro())
    print()
    sp.print_info()
