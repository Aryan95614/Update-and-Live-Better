import PySimpleGUI as sg
import sys
from ClickForCode.C_onstants import *
from twilio.rest import Client
from ClickForCode.network import Network


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.layout = [

            [self.c([sg.Text("Daily Reflection in Grades, Lifestyle and Activities!")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text("Write about your day and short term goals")])],
            self.c([sg.Frame("What are your grades currently?", [[
                sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=50, tick_interval=25),
                sg.Text(f"In {info['sub1']}"),
                sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=50),
                sg.Text(f"In {info['sub2']}"),
                sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=50),
                sg.Text(f"In {info['sub3']}"),
                sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=50),
                sg.Text(f"In {info['sub4']}")
            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"{info['sub1']}", size=(10, 1)),
                 sg.CBox(f"{info['sub2']}", default=False)],
                [sg.CBox(f"{info['sub3']}", size=(20, 1)),
                 sg.CBox(f"{info['sub4']}", default=False)]],
                title='What Subjects will you be doing today',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[
                    [sg.Radio(f"I might Not finish anything", "RADIO1", size=(20, 1)),
                     sg.Radio(f"I might finish a miniscule part", "RADIO1", default=False)],
                    [sg.Radio(f"I might finish most of it today", "RADIO1", size=(23, 1)),
                     sg.Radio(f"I will certainly be finishing it", "RADIO1", default=False)]],
                    title='How much work will you complete today?',
                    title_color='orange',
                    relief=sg.RELIEF_SUNKEN)]),

            [sg.Button('Ok')]]

        self.window = sg.Window('Succeed and Aim', self.layout, size=(800, 400), resizable=True, finalize=True)

    def play(self):
        true = True
        while True:

            event, values = self.window.read()
            if values != None:
                self.events = list(values.values())
            if event == sg.WINDOW_CLOSED:
                break
            if event == "Ok":
                info["Return Values"] = self.events
                true = False
                self.window.close()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break

    @staticmethod
    def send(events):

        try:
            account_sid = 'ACc2e51fc9bf8ecd1a2a39841b089e0105'
            auth_token = 'c68cdf9c02ba07d3cbb45b41b3b32899'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                from_='+15017122661',
                to='+15558675310'
            )
        except Exception as e:
            print(f"{e}")


class MathWindow():
    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):
        sg.theme("Black")
        self.net = Network()

        self.thing = (f"Your Reflection: {info['Return Values'][0]}. You have a {str(info['Return Values'][1])[:2:]}"+
                             f" in mathematics. You have a {info['Return Values'][2]} in English. You have a {str(info['Return Values'][3])[:2:]} "+
                             f" in Computer Science. You have a {info['Return Values'][4]} in History. "+
                             f" Looking at the workload promise you gave, you will give good performance'.")
        self.layout = [
            self.c([sg.Frame(
                layout=[[sg.Text("What will you be studying today?"), sg.MLine(size=(35, 5))],
                        [sg.MLine(
                            self.thing, size = (70, 8))]],
                title="Work"
            )]),
            [sg.Button('Ok')]]

        self.window = sg.Window('Computer Science', self.layout, size=(800, 400), resizable=True, finalize=True)

    def send_data(self):

        data = str(self.thing)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0, 0
    def play(self):

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                sys.exit()

            self.events = list(values.values())
            if event == "Ok":
                info["Search Values"] = self.events
                self.send_data()
                self.window.close()

            print(self.net.recieve(self.net.client))
