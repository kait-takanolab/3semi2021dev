#!/usr/bin/env python
# coding: utf-8

# This is written by Tomoya Yoshii
# edited by 3semi2021

from pydub import AudioSegment
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#get_ipython().run_line_magic()


path = os.getcwd()
#name ="ultra.mp3"
name = "programs_music_Latin_000704.mp3"



sound = AudioSegment.from_file(name)



samples = np.array(sound.get_array_of_samples())
sample = samples[::sound.channels]



#フーリエ変換
spec = np.fft.fft(sample)



freq = np.fft.fftfreq(sample.shape[0],1.0/sound.frame_rate)



#窓幅
w = 2000
#刻み
s = 500



#スペクトル格納用
ampList = []

#刻みずつずらしながら窓幅分のデータをフーリエ変換する
for i in range(int((sample.shape[0]- w) / s)):
    data = sample[i*s:i*s+w]
    spec = np.fft.fft(data)
    spec = spec[:int(spec.shape[0]/2)]
    spec[0] = spec[0] / 2
    ampList.append(np.abs(spec))


#周波数は共通なので１回だけ計算（縦軸表示に使う）  
freq = np.fft.fftfreq(data.shape[0], 1.0/sound.frame_rate)
freq = freq[:int(freq.shape[0]/2)]

#時間も共通なので１回だけ計算（横軸表示に使う）
time = np.arange(0, i+1, 1) * s / sound.frame_rate

#numpyの配列にしておく
ampList = np.array(ampList)



df_amp = pd.DataFrame(data=ampList, index=time, columns=freq)



#seabornのheatmapを使う
a = plt.figure(figsize=(20, 6))
l = sns.heatmap(data=np.log(df_amp.iloc[:, :100].T), 
            xticklabels=1000, 
            yticklabels=10, 
            cmap=plt.cm.gist_rainbow_r,
           )
l.set_ylabel("freq[Hz]",fontsize = 20)
l.set_xlabel("time[s]",fontsize = 20)



a.savefig("%s\/%s.png"%(path, name),bbox_inches="tight")

print("saved: %s\/%s.png"%(path, name))