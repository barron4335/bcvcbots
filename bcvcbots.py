# /usr/bin/env Python
# -*-coding:utf-8-*-
import http

import selenium
import urllib3
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.common.exceptions import NoSuchElementException
from threading import Thread

from io import open
import time
from datetime import datetime
from datetime import date
import os
import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")
from bs4 import BeautifulSoup
from random import randint
import requests
import sqlite3 as sqlite

class App():
    def __init__(self):
        self.veritabani()

        self.urlList = []

        self.proxyList = []

        self.veritabani(islem="ip adres sil")

        time.sleep(2)

        self.veritabani(islem="listele")

        self.openproxyList = []

        self.badproxyList = []

        self.pencere = Tk()
        self.pencere.title("BCVC BOT")
        self.pencere.geometry("700x500+0+0")
        self.pencere.config(bg="#fff")
        self.pencere.resizable(False, False)

        self.proxyadetsayi = Label(self.pencere, text="Proxy Adet Sayısı Giriniz : ", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.proxyadetsayi.place(x=5, y=5)

        self.proxyadetsayiEntry = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.proxyadetsayiEntry.place(x=5, y=30)

        self.proxycreatorButton = Button(self.pencere, text="Start Proxy Creator", bg="red", fg="#fff", activebackground="black", activeforeground="#fff", font=("Ubuntu", 9, "bold"), command=lambda: self.proxycreator(self.proxyadetsayiEntry.get()))
        self.proxycreatorButton.place(x=5, y=58)

        self.kactekrarsayi = Label(self.pencere, text="Kaç Defa Tekrar Etsin : ", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.kactekrarsayi.place(x=5, y=95)

        self.kactekrarsayiEntry = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.kactekrarsayiEntry.place(x=5, y=118)

        self.kactekrarsayi1 = Label(self.pencere, text="Kaç Pencere'de Çalışsın : ", bg="#fff", fg="black",
                                   font=("Ubuntu", 9, "bold"))
        self.kactekrarsayi1.place(x=5, y=150)

        self.kactekrarsayiEntry1 = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.kactekrarsayiEntry1.place(x=5, y=170)

        self.linktext = Label(self.pencere, text="Linklerinizi Giriniz : ", bg="#fff", fg="black",
                                   font=("Ubuntu", 9, "bold"))
        self.linktext.place(x=162, y=5)

        self.linktextFrame = Frame(self.pencere, highlightthickness=2, bg="#fff")
        self.linktextFrame.config(highlightcolor="#fff", highlightbackground="red", width=460, height=370)

        self.linktextScrollbar = Scrollbar(self.linktextFrame)
        self.linktextScrollbar.pack(side=RIGHT, fill=Y)

        self.linktextHScrollbar = Scrollbar(self.linktextFrame, orient='horizontal')
        self.linktextHScrollbar.pack(side=BOTTOM, fill=X)

        self.linktextEditor = Text(self.linktextFrame, width=39, height=8, bg="#fff", fg="black", font=("Ubuntu", 9 ,"bold"), yscrollcommand=self.linktextScrollbar.set, wrap="none", xscrollcommand=self.linktextHScrollbar.set)
        self.linktextEditor.pack(side=RIGHT, padx=5)

        self.linktextScrollbar.config(command=self.linktextEditor.yview)
        self.linktextHScrollbar.config(command=self.linktextEditor.xview)

        self.linktextFrame.place(x=162, y=30)

        self.addlinks = Button(self.pencere, text="Start Link to Add List", bg="red", fg="#fff",
                               activebackground="black", activeforeground="#fff", font=("Ubuntu", 9, "bold"),
                               command=lambda: self.startaddlink(self.linktextEditor.get("1.0",'end-1c')))
        self.addlinks.place(x=162, y=180)

        container1 = Frame(self.pencere, width=200, height=520, highlightthickness=2)
        container1.config(highlightcolor="#fff", highlightbackground="red")
        canvas1 = Canvas(container1, bg="#fff", width=286, height=267)
        scrollbar1 = Scrollbar(container1, orient="vertical", command=canvas1.yview)
        self.scrollable_frame1 = Frame(canvas1, bg="#fff")

        self.scrollable_frame1.bind(
            "<Configure>",
            lambda e: canvas1.configure(
                scrollregion=canvas1.bbox("all")
            )
        )

        canvas1.create_window((0, 0), window=self.scrollable_frame1, anchor="nw")

        canvas1.configure(yscrollcommand=scrollbar1.set)

        # İçerik
        # for i in range(50):
        #    ttk.Label(scrollable_frame1, text="Sample scrolling label").pack()

        container1.place(x=162, y=214)
        canvas1.pack(side="left", fill="both", expand=True)
        scrollbar1.pack(side="right", fill="y")

        self.psonuc = Label(self.pencere, text="Proxy Sonuçları : ", bg="#fff", fg="black",
                              font=("Ubuntu", 9, "bold"))
        self.psonuc.place(x=475, y=5)

        container = Frame(self.pencere, width=200, height=520, highlightthickness=2)
        container.config(highlightcolor="#fff", highlightbackground="red")
        canvas = Canvas(container, bg="#fff", width=200, height=420)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#fff", height=1000000000000)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        # İçerik
        # for i in range(50):
        #    ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

        container.place(x=475, y=30)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.botbaslat = Button(self.pencere, text="Start Auto BCVC BOT", bg="red", fg="#fff", activebackground="black", activeforeground="#fff", font=("Ubuntu", 9, "bold"), command=lambda: self.startbotsthread(self.kactekrarsayiEntry.get(), self.kactekrarsayiEntry1.get()))
        self.botbaslat.place(x=475, y=460)

        self.pencere.mainloop()

    def GetProxy(self):
        # url = 'https://www.sslproxies.org/'
        # r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # return choice(list(map(lambda x: x[0] + ':' + x[1], list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])),
        #                                                            (map(lambda x: x.text, soup.find_all('td')[1::8])))))))

        url = 'https://free-proxy-list.net/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        div = soup.find('div', class_='table-responsive')
        tbody = div.find("tbody")
        proxies = tbody.find_all("tr")
        proxy = proxies[randint(0, len(proxies) - 1)]

        proxy_ip = proxy.find_all("td")[0].get_text()
        proxy_port = proxy.find_all("td")[1].get_text()

        return proxy_ip + ":" + proxy_port

    def proxycreator(self, padetsayi):
        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        if padetsayi:
            i = 1
            pasayi = int(padetsayi)
            while i <= pasayi:
                padress = self.GetProxy()
                if padress in self.proxyList:
                    print("Liste'ye daha önce eklenmiştir.")
                else:
                    self.proxyList.append(padress)

                    sorgu = "SELECT * FROM proxys WHERE padress = '"+padress+"'"
                    self.vt.execute(sorgu)
                    ipvarmi = self.vt.fetchall()
                    if ipvarmi:
                        print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                    else:
                        self.veritabani(islem="ip adres ekle", padress=padress, pdurum="None", prdate=tarih)

                    i += 1
                self.pencere.update()
            self.proxylists()
        else:
            print("Lütfen sayı giriniz.")

    def proxylists(self):
        for ip in range(0, len(self.proxyList)):
            ips = self.proxyList[ip]
            Label(self.scrollable_frame, text=f"{ip}-{ips}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold")).pack()
            self.pencere.update()

    def startaddlink(self, urls):
        self.urls = urls.split(",")
        for url in range(0, len(self.urls)):
            url = self.urls[url]
            if url in self.urlList:
                print("Url adres liste'ye daha önce eklenmiştir.")
            else:
                self.urlList.append(url)
        self.urlcreator()

    def urlcreator(self):
        self.linktextEditor.delete('1.0', END)
        for url in range(len(self.urlList)):
            url = self.urlList[url]
            self.label= Label(self.scrollable_frame1, text=f"{url}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            self.label.pack()
            self.pencere.update()

    def startbotsthread(self, ktekrarsayi, kpenceresayi):
        countx = 0
        county = 0
        x = 710
        y = 0
        for i in range(0, int(kpenceresayi)):
            time.sleep(2)
            thread = Thread(target=lambda: self.startbots(i, int(ktekrarsayi), x, y))#, args=(i, int(ktekrarsayi), x, y))
            thread.start()
            x += 310
            countx += 1
            if x == 1330:
                if countx == 2:
                    countx = 0
                    x = 710
                    y += 340
                    county += 1
                    if y == 680:
                        if county == 2:
                            x = 710
                            y = 0
                            county = 0

    def badproxycreator(self, proxyadress):
        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        padress = proxyadress
        if padress in self.badproxyList:
            pass
        else:
            self.badproxyList.append(padress)

            sorgu = "SELECT * FROM proxys WHERE padress = '"+padress+"'"
            self.vt.execute(sorgu)
            ipvarmi = self.vt.fetchall()
            if ipvarmi:
                print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                self.veritabani(islem="ip adres durum güncelle", padress=padress, pdurum="BAD", prdate=tarih)
            else:
                self.veritabani(islem="ip adres ekle", padress=padress, pdurum="BAD", prdate=tarih)

        self.pencere.update()

    def openproxycreator(self, proxyadress):

        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        padress = proxyadress
        if padress in self.openproxyList:
            pass
        else:
            self.openproxyList.append(padress)

            sorgu = "SELECT * FROM proxys WHERE padress = '"+padress+"'"
            self.vt.execute(sorgu)
            ipvarmi = self.vt.fetchall()
            if ipvarmi:
                print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                self.veritabani(islem="ip adres durum güncelle", padress=padress, pdurum="GOOD", prdate=tarih)
            else:
                self.veritabani(islem="ip adres ekle", padress=padress, pdurum="GOOD", prdate=tarih)
        self.pencere.update()


    def startbots(self, psayi, ktekrarsayi, x, y):
        while True:
            self.bsayi = 0
            self.bsizsayi = 0
            pencere1 = Tk()
            pencere1.title(f"{psayi} Pencere")
            pencere1.geometry(f"300x300+{x}+{y}")
            pencere1.config(bg="#fff")

            label1 = Label(pencere1, text="Denen Link Adresi :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label1.place(x=5, y=5)

            label1sonuc = Label(pencere1)
            label1sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label1sonuc.place(x=120, y=5)

            label2 = Label(pencere1, text="Denen Proxy Adresi :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label2.place(x=5, y=20)

            label2sonuc = Label(pencere1)
            label2sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label2sonuc.place(x=126, y=20)

            label3 = Label(pencere1, text="Dakika :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label3.place(x=5, y=35)

            label3sonuc = Label(pencere1)
            label3sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label3sonuc.place(x=126, y=35)

            for i in range(0, ktekrarsayi):
                try:

                    # Daha Çok Kazanç Elde Etmek İçin '#' işaretini kaldırmanız gerekmektedir
                    dkansn = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]
                    dksn = dkansn[randint(0, 10)]
                    self.dk = dksn[0]
                    sn = dksn[1]
                    sn1 = int(sn)

                    # Daha Çok Kazan Elde etmek için 370-372 satırların önüne '#' işareti koyunuz
                    # dkansn = [15, 900]
                    # self.dk = dkansn[0]
                    sn = dkansn[1]
                    label3sonuc.config(text=f"{self.dk} Saniye yeniden başlayacak", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
                    url = self.urlList[randint(0, len(self.urlList) + 2)]
                    label1sonuc.config(text=f"{url}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
                    ip = self.proxyList[randint(0, len(self.proxyList) + 2)]
                    label2sonuc.config(text=f"{ip}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
                    pencere1.update()

                    # firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
                    # firefox_capabilities['marionette'] = True
                    #
                    # firefox_capabilities['proxy'] = {
                    #     "proxyType": "MANUAL",
                    #     "httpProxy": ip,
                    #     "ftpProxy": ip,
                    #     "sslProxy": ip
                    # }
                    #
                    # options = Options()
                    # options.headless = False
                    # options = options
                    #
                    # driver = webdriver.Firefox(capabilities=firefox_capabilities)

                    # prox = Proxy()
                    # prox.proxy_type = ProxyType.MANUAL
                    # prox.http_proxy = ip
                    # prox.socks_proxy = ip
                    # # prox.ssl_proxy = ip
                    # capabilities = webdriver.DesiredCapabilities.CHROME
                    # prox.add_to_capabilities(capabilities)
                    # desired_capabilities = capabilities
                    chrome_options = Options()
                    chrome_options.add_argument(f'--proxy-server=http://{ip}')
                    chrome_options.add_extension('ublock.xpi')
                    # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                    # chrome_options.add_argument('headless')
                    # chrome_options.add_argument('window-size=0x0')
                    #chrome_options.set_headless(headless=True)
                    self.driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)
                    try:
                        self.driver.set_page_load_timeout(2000)
                        # extension_path = "adblock.xpi"
                        # driver.install_addon(extension_path, temporary=True)
                        self.driver.get("%s" % url)
                        time.sleep(sn1)

                        tikla = self.driver.find_element(By.CSS_SELECTOR, '#page-top > section')
                        tikla.click()

                        time.sleep(sn1)
                        window_after = self.driver.window_handles[1]
                        self.driver.switch_to.window(window_after)
                        self.driver.close()

                        time.sleep(sn1)
                        window_after = self.driver.window_handles[0]
                        self.driver.switch_to.window(window_after)

                        izinverclick = self.driver.find_element(By.CSS_SELECTOR, '#getLinkx')
                        izinverclick.click()

                        self.bsayi += 1
                        self.openproxycreator(ip)
                        pencere1.update()
                        self.driver.close()

                    except selenium.common.exceptions.TimeoutException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except selenium.common.exceptions.WebDriverException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except selenium.common.exceptions.InvalidSessionIdException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except http.client.RemoteDisconnected as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.NewConnectionError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except ConnectionRefusedError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.ProtocolError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.MaxRetryError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                except IndexError:
                    continue
                finally:
                    continue
                pass

            
            pencere1.mainloop()

    def veritabani(self, islem=None, padress=None, prdate=None, pdurum=None):
        self.data = sqlite.connect('veritabanı.db',  check_same_thread=False)
        self.vt = self.data.cursor()

        self.vt.execute("""CREATE TABLE IF NOT EXISTS proxys(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        padress text,
                        pdurum text,
                        prdate DATE
                        )""")

        if islem == "ip adres ekle":
            try:
                datacommands ="""INSERT INTO proxys(padress,pdurum,prdate) VALUES {}"""
                data = (padress, pdurum, prdate)
                self.vt.execute(datacommands.format(data))
                print(f"Proxy : {padress} Durum : {pdurum} Tarih : {prdate} eklenmiştir.")
            except Exception as e:
                print("Hata")
                print("-"*50)
                print(e)

        elif islem == "ip adres durum güncelle":
            try:
                datacommands1 = "SELECT * FROM proxys WHERE padress = '"+padress+"'"
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                for row in ipvarmi:
                    id = row[0]
                    print(id)
                    datacommands2 = "UPDATE proxys SET pdurum = '"+str(pdurum)+"' WHERE ID = '"+str(id)+"' AND padress = '"+str(padress)+"'"
                    self.vt.execute(datacommands2)
                    self.data.commit()
                    print(f"ID : {id} Proxy : {padress} Durumu: {pdurum} olarak güncellendi.")
            except Exception as e:
                print("Hata")
                print("-"*50)
                print(e)

        elif islem == "ip adres sil":
            try:
                datacommands1 = "SELECT * FROM proxys WHERE pdurum = 'BAD'"
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                if ipvarmi:
                    for row in ipvarmi:
                        id = row[0]
                        ipad = row[1]
                        self.vt.execute("DELETE from proxys WHERE pdurum = 'BAD' AND padress = '"+ipad+"'")
                        self.data.commit()
                        print(f"ID : {id} Proxy : {ipad} Veritabanından silinmiştir.")
            except Exception as e:
                print("Hata")
                print("-" * 50)
                print(e)

        elif islem == "listele":
            try:
                datacommands1 = """SELECT * FROM proxys"""
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                for row in ipvarmi:
                    padress1 = row[1]
                    self.proxyList.append(padress1)

            except Exception as e:
                print("Hata")
                print("-"*50)
                print(e)


class App1():
    def __init__(self):
        self.veritabani()

        self.urlList = []

        self.proxyList = []

        self.veritabani(islem="ip adres sil")

        time.sleep(2)

        self.veritabani(islem="listele")

        self.openproxyList = []

        self.badproxyList = []

        self.pencere = Tk()
        self.pencere.title("BCVC BOT")
        self.pencere.geometry("700x500+0+0")
        self.pencere.config(bg="#fff")
        self.pencere.resizable(False, False)

        self.proxyadetsayi = Label(self.pencere, text="Proxy Adet Sayısı Giriniz : ", bg="#fff", fg="black",
                                   font=("Ubuntu", 9, "bold"))
        self.proxyadetsayi.place(x=5, y=5)

        self.proxyadetsayiEntry = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.proxyadetsayiEntry.place(x=5, y=30)

        self.proxycreatorButton = Button(self.pencere, text="Start Proxy Creator", bg="red", fg="#fff",
                                         activebackground="black", activeforeground="#fff", font=("Ubuntu", 9, "bold"),
                                         command=lambda: self.proxycreator(self.proxyadetsayiEntry.get()))
        self.proxycreatorButton.place(x=5, y=58)

        self.kactekrarsayi = Label(self.pencere, text="Kaç Defa Tekrar Etsin : ", bg="#fff", fg="black",
                                   font=("Ubuntu", 9, "bold"))
        self.kactekrarsayi.place(x=5, y=95)

        self.kactekrarsayiEntry = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.kactekrarsayiEntry.place(x=5, y=118)

        self.kactekrarsayi1 = Label(self.pencere, text="Kaç Pencere'de Çalışsın : ", bg="#fff", fg="black",
                                    font=("Ubuntu", 9, "bold"))
        self.kactekrarsayi1.place(x=5, y=150)

        self.kactekrarsayiEntry1 = Entry(self.pencere, bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
        self.kactekrarsayiEntry1.place(x=5, y=170)

        self.linktext = Label(self.pencere, text="Linklerinizi Giriniz : ", bg="#fff", fg="black",
                              font=("Ubuntu", 9, "bold"))
        self.linktext.place(x=162, y=5)

        self.linktextFrame = Frame(self.pencere, highlightthickness=2, bg="#fff")
        self.linktextFrame.config(highlightcolor="#fff", highlightbackground="red", width=460, height=370)

        self.linktextScrollbar = Scrollbar(self.linktextFrame)
        self.linktextScrollbar.pack(side=RIGHT, fill=Y)

        self.linktextHScrollbar = Scrollbar(self.linktextFrame, orient='horizontal')
        self.linktextHScrollbar.pack(side=BOTTOM, fill=X)

        self.linktextEditor = Text(self.linktextFrame, width=39, height=8, bg="#fff", fg="black",
                                   font=("Ubuntu", 9, "bold"), yscrollcommand=self.linktextScrollbar.set, wrap="none",
                                   xscrollcommand=self.linktextHScrollbar.set)
        self.linktextEditor.pack(side=RIGHT, padx=5)

        self.linktextScrollbar.config(command=self.linktextEditor.yview)
        self.linktextHScrollbar.config(command=self.linktextEditor.xview)

        self.linktextFrame.place(x=162, y=30)

        self.addlinks = Button(self.pencere, text="Start Link to Add List", bg="red", fg="#fff",
                               activebackground="black", activeforeground="#fff", font=("Ubuntu", 9, "bold"),
                               command=lambda: self.startaddlink(self.linktextEditor.get("1.0", 'end-1c')))
        self.addlinks.place(x=162, y=180)

        container1 = Frame(self.pencere, width=200, height=520, highlightthickness=2)
        container1.config(highlightcolor="#fff", highlightbackground="red")
        canvas1 = Canvas(container1, bg="#fff", width=286, height=267)
        scrollbar1 = Scrollbar(container1, orient="vertical", command=canvas1.yview)
        self.scrollable_frame1 = Frame(canvas1, bg="#fff")

        self.scrollable_frame1.bind(
            "<Configure>",
            lambda e: canvas1.configure(
                scrollregion=canvas1.bbox("all")
            )
        )

        canvas1.create_window((0, 0), window=self.scrollable_frame1, anchor="nw")

        canvas1.configure(yscrollcommand=scrollbar1.set)

        # İçerik
        # for i in range(50):
        #    ttk.Label(scrollable_frame1, text="Sample scrolling label").pack()

        container1.place(x=162, y=214)
        canvas1.pack(side="left", fill="both", expand=True)
        scrollbar1.pack(side="right", fill="y")

        self.psonuc = Label(self.pencere, text="Proxy Sonuçları : ", bg="#fff", fg="black",
                            font=("Ubuntu", 9, "bold"))
        self.psonuc.place(x=475, y=5)

        container = Frame(self.pencere, width=200, height=520, highlightthickness=2)
        container.config(highlightcolor="#fff", highlightbackground="red")
        canvas = Canvas(container, bg="#fff", width=200, height=420)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#fff", height=1000000000000)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        # İçerik
        # for i in range(50):
        #    ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

        container.place(x=475, y=30)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.botbaslat = Button(self.pencere, text="Start Auto BCVC BOT", bg="red", fg="#fff", activebackground="black",
                                activeforeground="#fff", font=("Ubuntu", 9, "bold"),
                                command=lambda: self.startbotsthread(self.kactekrarsayiEntry.get(),
                                                                     self.kactekrarsayiEntry1.get()))
        self.botbaslat.place(x=475, y=460)

        self.pencere.mainloop()

    def GetProxy(self):
        # url = 'https://www.sslproxies.org/'
        # r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # return choice(list(map(lambda x: x[0] + ':' + x[1], list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])),
        #                                                            (map(lambda x: x.text, soup.find_all('td')[1::8])))))))

        url = 'https://free-proxy-list.net/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        div = soup.find('div', class_='table-responsive')
        tbody = div.find("tbody")
        proxies = tbody.find_all("tr")
        proxy = proxies[randint(0, len(proxies) - 1)]

        proxy_ip = proxy.find_all("td")[0].get_text()
        proxy_port = proxy.find_all("td")[1].get_text()

        return proxy_ip + ":" + proxy_port

    def proxycreator(self, padetsayi):
        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        if padetsayi:
            i = 1
            pasayi = int(padetsayi)
            while i <= pasayi:
                padress = self.GetProxy()
                if padress in self.proxyList:
                    print("Liste'ye daha önce eklenmiştir.")
                else:
                    self.proxyList.append(padress)

                    sorgu = "SELECT * FROM proxys WHERE padress = '" + padress + "'"
                    self.vt.execute(sorgu)
                    ipvarmi = self.vt.fetchall()
                    if ipvarmi:
                        print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                    else:
                        self.veritabani(islem="ip adres ekle", padress=padress, pdurum="None", prdate=tarih)

                    i += 1
                self.pencere.update()
            self.proxylists()
        else:
            print("Lütfen sayı giriniz.")

    def proxylists(self):
        for ip in range(0, len(self.proxyList)):
            ips = self.proxyList[ip]
            Label(self.scrollable_frame, text=f"{ip}-{ips}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold")).pack()
            self.pencere.update()

    def startaddlink(self, urls):
        self.urls = urls.split(",")
        for url in range(0, len(self.urls)):
            url = self.urls[url]
            if url in self.urlList:
                print("Url adres liste'ye daha önce eklenmiştir.")
            else:
                self.urlList.append(url)
        self.urlcreator()

    def urlcreator(self):
        self.linktextEditor.delete('1.0', END)
        for url in range(len(self.urlList)):
            url = self.urlList[url]
            self.label = Label(self.scrollable_frame1, text=f"{url}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            self.label.pack()
            self.pencere.update()

    def startbotsthread(self, ktekrarsayi, kpenceresayi):
        countx = 0
        county = 0
        x = 710
        y = 0
        for i in range(0, int(kpenceresayi)):
            time.sleep(2)
            thread = Thread(
                target=lambda: self.startbots(i, int(ktekrarsayi), x, y))  # , args=(i, int(ktekrarsayi), x, y))
            thread.start()
            x += 310
            countx += 1
            if x == 1330:
                if countx == 2:
                    countx = 0
                    x = 710
                    y += 340
                    county += 1
                    if y == 680:
                        if county == 2:
                            x = 710
                            y = 0
                            county = 0

    def badproxycreator(self, proxyadress):
        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        padress = proxyadress
        if padress in self.badproxyList:
            pass
        else:
            self.badproxyList.append(padress)

            sorgu = "SELECT * FROM proxys WHERE padress = '" + padress + "'"
            self.vt.execute(sorgu)
            ipvarmi = self.vt.fetchall()
            if ipvarmi:
                print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                self.veritabani(islem="ip adres durum güncelle", padress=padress, pdurum="BAD", prdate=tarih)
            else:
                self.veritabani(islem="ip adres ekle", padress=padress, pdurum="BAD", prdate=tarih)

        self.pencere.update()

    def openproxycreator(self, proxyadress):

        bugun = datetime.now()
        tarih = f"{bugun.year}-{bugun.month}-{bugun.day} {bugun.hour}:{bugun.minute}:{bugun.second}"

        padress = proxyadress
        if padress in self.openproxyList:
            pass
        else:
            self.openproxyList.append(padress)

            sorgu = "SELECT * FROM proxys WHERE padress = '" + padress + "'"
            self.vt.execute(sorgu)
            ipvarmi = self.vt.fetchall()
            if ipvarmi:
                print(f"Veritabanında İp Adres : {padress} bulunmaktadır.")
                self.veritabani(islem="ip adres durum güncelle", padress=padress, pdurum="GOOD", prdate=tarih)
            else:
                self.veritabani(islem="ip adres ekle", padress=padress, pdurum="GOOD", prdate=tarih)
        self.pencere.update()

    def startbots(self, psayi, ktekrarsayi, x, y):
        while True:
            self.bsayi = 0
            self.bsizsayi = 0
            pencere1 = Tk()
            pencere1.title(f"{psayi} Pencere")
            pencere1.geometry(f"300x300+{x}+{y}")
            pencere1.config(bg="#fff")

            label1 = Label(pencere1, text="Denen Link Adresi :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label1.place(x=5, y=5)

            label1sonuc = Label(pencere1)
            label1sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label1sonuc.place(x=120, y=5)

            label2 = Label(pencere1, text="Denen Proxy Adresi :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label2.place(x=5, y=20)

            label2sonuc = Label(pencere1)
            label2sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label2sonuc.place(x=126, y=20)

            label3 = Label(pencere1, text="Dakika :", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label3.place(x=5, y=35)

            label3sonuc = Label(pencere1)
            label3sonuc.config(text=f"", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
            label3sonuc.place(x=126, y=35)

            for i in range(0, ktekrarsayi):
                try:

                    # Daha Çok Kazanç Elde Etmek İçin '#' işaretini kaldırmanız gerekmektedir
                    dkansn = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14],
                              [15, 15]]
                    dksn = dkansn[randint(0, 10)]
                    self.dk = dksn[0]
                    sn = dksn[1]
                    sn1 = int(sn)

                    # Daha Çok Kazan Elde etmek için 370-372 satırların önüne '#' işareti koyunuz
                    # dkansn = [15, 900]
                    # self.dk = dkansn[0]
                    sn = dkansn[1]
                    label3sonuc.config(text=f"{self.dk} Saniye yeniden başlayacak", bg="#fff", fg="black",
                                       font=("Ubuntu", 9, "bold"))
                    url = self.urlList[randint(0, len(self.urlList) + 2)]
                    label1sonuc.config(text=f"{url}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
                    ip = self.proxyList[randint(0, len(self.proxyList) + 2)]
                    label2sonuc.config(text=f"{ip}", bg="#fff", fg="black", font=("Ubuntu", 9, "bold"))
                    pencere1.update()

                    # firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
                    # firefox_capabilities['marionette'] = True
                    #
                    # firefox_capabilities['proxy'] = {
                    #     "proxyType": "MANUAL",
                    #     "httpProxy": ip,
                    #     "ftpProxy": ip,
                    #     "sslProxy": ip
                    # }
                    #
                    # options = Options()
                    # options.headless = False
                    # options = options
                    #
                    # driver = webdriver.Firefox(capabilities=firefox_capabilities)

                    # prox = Proxy()
                    # prox.proxy_type = ProxyType.MANUAL
                    # prox.http_proxy = ip
                    # prox.socks_proxy = ip
                    # # prox.ssl_proxy = ip
                    # capabilities = webdriver.DesiredCapabilities.CHROME
                    # prox.add_to_capabilities(capabilities)
                    # desired_capabilities = capabilities
                    chrome_options = Options()
                    chrome_options.add_argument(f'--proxy-server=http://{ip}')
                    chrome_options.add_extension('ublock.xpi')
                    # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                    # chrome_options.add_argument('headless')
                    # chrome_options.add_argument('window-size=0x0')
                    # chrome_options.set_headless(headless=True)
                    self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
                    try:
                        self.driver.set_page_load_timeout(2000)
                        # extension_path = "adblock.xpi"
                        # driver.install_addon(extension_path, temporary=True)
                        self.driver.get("%s" % url)
                        time.sleep(sn1)

                        tikla = self.driver.find_element(By.CSS_SELECTOR, '#page-top > section')
                        tikla.click()

                        time.sleep(sn1)
                        window_after = self.driver.window_handles[1]
                        self.driver.switch_to.window(window_after)
                        self.driver.close()

                        time.sleep(sn1)
                        window_after = self.driver.window_handles[0]
                        self.driver.switch_to.window(window_after)

                        izinverclick = self.driver.find_element(By.CSS_SELECTOR, '#getLinkx')
                        izinverclick.click()

                        self.bsayi += 1
                        self.openproxycreator(ip)
                        pencere1.update()
                        self.driver.close()

                    except selenium.common.exceptions.TimeoutException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except selenium.common.exceptions.WebDriverException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except selenium.common.exceptions.InvalidSessionIdException as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except http.client.RemoteDisconnected as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.NewConnectionError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except ConnectionRefusedError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.ProtocolError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                    except urllib3.exceptions.MaxRetryError as ex:
                        print("Exception has been thrown. " + str(ex))
                        self.bsizsayi += 1
                        self.badproxycreator(ip)
                        self.driver.close()
                        continue

                except IndexError:
                    continue
                finally:
                    continue
                pass

            pencere1.mainloop()

    def veritabani(self, islem=None, padress=None, prdate=None, pdurum=None):
        self.data = sqlite.connect('veritabanı.db', check_same_thread=False)
        self.vt = self.data.cursor()

        self.vt.execute("""CREATE TABLE IF NOT EXISTS proxys(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        padress text,
                        pdurum text,
                        prdate DATE
                        )""")

        if islem == "ip adres ekle":
            try:
                datacommands = """INSERT INTO proxys(padress,pdurum,prdate) VALUES {}"""
                data = (padress, pdurum, prdate)
                self.vt.execute(datacommands.format(data))
                print(f"Proxy : {padress} Durum : {pdurum} Tarih : {prdate} eklenmiştir.")
            except Exception as e:
                print("Hata")
                print("-" * 50)
                print(e)

        elif islem == "ip adres durum güncelle":
            try:
                datacommands1 = "SELECT * FROM proxys WHERE padress = '" + padress + "'"
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                for row in ipvarmi:
                    id = row[0]
                    print(id)
                    datacommands2 = "UPDATE proxys SET pdurum = '" + str(pdurum) + "' WHERE ID = '" + str(
                        id) + "' AND padress = '" + str(padress) + "'"
                    self.vt.execute(datacommands2)
                    self.data.commit()
                    print(f"ID : {id} Proxy : {padress} Durumu: {pdurum} olarak güncellendi.")
            except Exception as e:
                print("Hata")
                print("-" * 50)
                print(e)

        elif islem == "ip adres sil":
            try:
                datacommands1 = "SELECT * FROM proxys WHERE pdurum = 'BAD'"
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                if ipvarmi:
                    for row in ipvarmi:
                        id = row[0]
                        ipad = row[1]
                        self.vt.execute("DELETE from proxys WHERE pdurum = 'BAD' AND padress = '" + ipad + "'")
                        self.data.commit()
                        print(f"ID : {id} Proxy : {ipad} Veritabanından silinmiştir.")
            except Exception as e:
                print("Hata")
                print("-" * 50)
                print(e)

        elif islem == "listele":
            try:
                datacommands1 = """SELECT * FROM proxys"""
                self.vt.execute(datacommands1)
                ipvarmi = self.vt.fetchall()
                for row in ipvarmi:
                    padress1 = row[1]
                    self.proxyList.append(padress1)

            except Exception as e:
                print("Hata")
                print("-" * 50)
                print(e)

if __name__ == '__main__':
    if os.name == "nt":
        import tkinter as tk
        from tkinter import *
        from tkinter import ttk
        App1()
    elif os.name == "posix":
        import tkinter as tk
        from tkinter import *
        from tkinter import ttk
        App()
