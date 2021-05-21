import random
import time
# we imported the necessary libraries

class Remote():

    def __init__(self, tv_case="close", tv_volume=0, channel_list=["FOX"], channel="FOX"):

        self.tv_case = tv_case
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel


    def open_tv(self):
        if (self.tv_case == "open"):
            print("The TV is already open.")
        else:
            print("The TV  is opening...")
            self.tv_case = "open"

    def close_tv(self):
        if (self.tv_case == "close"):
            print("The TV is already close.")
        else:
            print("The TV is closing.")
            self.tv_case = "close"

    def voice_settings(self):
        """Sets voice of TV
        lower the sound: '<'
        Increase the volume: '>'
        Quit : quit
        """
        while True:
            answer = input("lower the sound: '<'\nincrease the volume: '>'\nQuit : quit")
            if (answer == '<'):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("voice:",self.tv_volume)
            elif (answer == ">"):
                if (self.tv_volume != 51):
                    self.tv_volume += 1
                    print("voice:",self.tv_volume)
                else:
                    print("The voice is updated:", self.tv_volume)
                    break
            if answer == 'quit':
                print("The voice is updated:", self.tv_volume)
                break

    def add_channel(self, channel_name):
        """"
        it adds one or more channel in the channel list.
        arg1 : channel name
        """
        print("The channels are adding")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("The channels added")

    def random_channel(self):
        """"
            it chooses random one channel in the channel list.
            returns: current channel
        """
        random_channel = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[random_channel]
        print("Current channel is :", self.channel)

    def __len__(self):
        """"
        return: length of channel list
        """
        return len(self.channel_list)

    def __str__(self):
        """
        Its gives the general information about the television
        :param self:0
        :return:
        """
        return f"TV Status : {self.tv_case}\n TV Voice: {self.tv_volume}\nChannel List: {self.channel_list}\nCurrent Channel: {self.channel}\n"


remote = Remote()
print('''
TV Application

1. Open TV
2. Close TV
3. Sound settings
4. Add a Channel 
5. Finding the Number of Channels
6. Random Channel Switching
7. Informations of Tv

Please enter 'q' to be quit ...''')

while True:
    operation = input("Please choose operation: ")

    if (operation == 'q'):
        print("The TV is closing")
        break
    elif (operation == "1"):
        remote.open_tv()
    elif (operation == "2"):
        remote.close_tv()
    elif (operation == "3"):
        remote.voice_settings()
    elif (operation == "4"):
        channel_list = input("Please enter channel names separated by ',':")

        channel_list = channel_list.split(",")

        for will_be_adds in channel_list:
            remote.add_channel(will_be_adds)
    elif (operation == "5"):
        print("Number of channel :", len(remote))

    elif (operation == "6"):
        remote.random_channel()
    elif (operation == "7"):
        print(remote)

    else:
        print("Invalid operation.....")


































