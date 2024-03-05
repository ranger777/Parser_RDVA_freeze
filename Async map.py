import time

import requests
from _decimal import Decimal
from bs4 import BeautifulSoup
import numpy as np
import asyncio
import aiohttp
import aiomultiprocess


start_time = time.time()#обозначим время начала запуска скрипта

arrey_hosts = [
            'rdva10.rosdomofon.com',
            # 'rdva114.rosdomofon.com',
            'rdva11.rosdomofon.com',
            'rdva12.rosdomofon.com',
            'rdva13.rosdomofon.com',
            'rdva14.rosdomofon.com',
            'rdva15.rosdomofon.com',
            'rdva16.rosdomofon.com',
            'rdva17.rosdomofon.com',
            'rdva18.rosdomofon.com',
            'rdva19.rosdomofon.com',
            'rdva20.rosdomofon.com',
            'rdva21.rosdomofon.com',
            'rdva22.rosdomofon.com',
            'rdva23.rosdomofon.com',
            'rdva24.rosdomofon.com',
            'rdva25.rosdomofon.com',
            'rdva27.rosdomofon.com',
            'rdva28.rosdomofon.com',
            'rdva29.rosdomofon.com',
            'rdva30.rosdomofon.com',
            'rdva31.rosdomofon.com',
            'rdva32.rosdomofon.com',
            'rdva33.rosdomofon.com',
            'rdva34.rosdomofon.com',
            'rdva35.rosdomofon.com',
            'rdva36.rosdomofon.com',
            'rdva37.rosdomofon.com',
            'rdva38.rosdomofon.com',
            'rdva39.rosdomofon.com',
            'rdva40.rosdomofon.com',
            'rdva41.rosdomofon.com',
            'rdva42.rosdomofon.com',
            # 'rdva43.rosdomofon.com',test
            'rdva44.rosdomofon.com',
            'rdva45.rosdomofon.com',
            'rdva46.rosdomofon.com',
            'rdva47.rosdomofon.com',
            'rdva48.rosdomofon.com',
            'rdva49.rosdomofon.com',
            'rdva4.rosdomofon.com',
            'rdva50.rosdomofon.com',
            'rdva51.rosdomofon.com',
            'rdva52.rosdomofon.com',
            'rdva53.rosdomofon.com',
            'rdva54.rosdomofon.com',
            'rdva55.rosdomofon.com',
            'rdva56.rosdomofon.com',
            'rdva57.rosdomofon.com',
            'rdva58.rosdomofon.com',
            'rdva59.rosdomofon.com',
            'rdva60.rosdomofon.com',
            'rdva5.rosdomofon.com',
            'rdva7.rosdomofon.com',
            'rdva8.rosdomofon.com',
            'rdva9.rosdomofon.com'
        ]

async def get_page_data(el):#предаем в функцию параметры сессии и элемента списка рдва
        #print(f'el = {el}')
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        }
        try:
            r = requests.get(f'http://{el}:2205/sysinfo/tnx', headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            table1 = soup.find('table', {"class": "infotable"})
            array_all = []
            for i in table1.find_all('td'):
                if i.text != 'QueuedTime' and i.text != 'QueueWaitTime' and i.text != 'ID':
                    title = i.text
                    array_all.append(title)
            #print(f'{el} array_all = {array_all}')
            if float(float(array_all[1])) > 36000:
                print(f'(1){el} - {array_all[1]} секунд простоя, id камеры:{array_all[2]}')
            #else: print(f'норм {el}')
        except:
            #print(f'except1 sleep2 {el}')
            await asyncio.sleep(1)
            try:
                r = requests.get(f'http://{el}:2205/sysinfo/tnx', headers=headers)
                soup = BeautifulSoup(r.text, "lxml")
                table1 = soup.find('table', {"class": "infotable"})
                array_all = []
                for i in table1.find_all('td'):
                    if i.text != 'QueuedTime' and i.text != 'QueueWaitTime' and i.text != 'ID':
                        title = i.text
                        array_all.append(title)
                if float(float(array_all[1])) > 36000:
                    print(f'(2){el} - {array_all[1]} секунд простоя, id камеры:{array_all[2]}')
                # else:
                # print(f'норм2 {el}')
            except:
                # print(f'except2 sleep2 {el}')
                await asyncio.sleep(1)
                try:
                    r = requests.get(f'http://{el}:2205/sysinfo/tnx', headers=headers)
                    soup = BeautifulSoup(r.text, "lxml")
                    table1 = soup.find('table', {"class": "infotable"})
                    array_all = []
                    for i in table1.find_all('td'):
                        if i.text != 'QueuedTime' and i.text != 'QueueWaitTime' and i.text != 'ID':
                            title = i.text
                        array_all.append(title)
                    if float(float(array_all[1])) > 36000:
                        print(f'(3){el} - {array_all[1]} секунд простоя, id камеры:{array_all[2]}')
                    # else:
                    # print(f'норм3 {el}')
                except:
                    # print(f'except3 {el}')
                    print(f"{el} - нет данных на странице")




async def gether_data():
    tasks = []# создаем список задач
    async with aiomultiprocess.Pool() as pool:
        async for task in pool.map(get_page_data, arrey_hosts):
        # цикл, который пробегается по страницам с рдва
            tasks.append(task)#Пополняем список задач






def main():
    asyncio.run(gether_data())
    finish_time = time.time() - start_time
    print(f'Время работы скрипта: {finish_time}')
    input("Нажмите Enter, чтобы закрыть консоль...")


if __name__ == '__main__':
    main()









