# 安心打診おばあ デモ動画:[url](https://www.youtube.com/watch?v=wMtzEgBEyec)

![2024-10-27 11 04の画像 (1)](https://github.com/user-attachments/assets/b41391e4-8875-4d36-981e-96848e568c97)

## 製品概要
### 背景（製品開発のきっかけ、課題等）
私たちが過ごしている日常には、多くの危険が潜んでいます。帰りの夜道や交通量の多い通り、さらには予期していなかった雨。それらは慣れた日常の落とし穴と言えるでしょう。しかし、めまぐるしく変化を続ける現代を生きる私たちはそれらの危険に気づく余裕さえ持ち合わせていないのです。
### 製品説明（具体的な製品の説明） 
 **「安心打診おばあ」** は私たちの日常に潜む危険に気づきを与え、アドバイスを与え、さらには安心感を与えてくれます。今日の予定、明日の予定など事前に未来の予定を入力すれば、自分がしようとしている行動の中に潜む危険やアドバイスを、まさに **「おばあちゃんの知恵袋」** として教えてくれます。また、入力内容は保存されるので日常を記録する日記として活用することもできます。日記として過去の行動を入力し、その行動の危険やアドバイスをもらうことで自分の行動の反省にも活用することができるでしょう。
### 特長
1. 入力された情報から行動だけを抽出し、各行動に対するコメントをおばあちゃん口調でもらうことができます。
2. 行動が危険かどうかでおばあちゃんの表情が3段階で変化します。
3. 入力日の名古屋の天気を自動で教えてくれます。

### 解決出来ること
日常のなかの「油断した」ことで起きる危険を、事前に知りアドバイスを受けることで未然に防ぐことができます。
### 今後の展望
現状は天気情報が名古屋に固定されているため、入力された情報から場所を抜き出し、それぞれの地点の天気情報を表示できるように開発できるとより便利なツールになると考えています。また、現状は天気APIだけですが、今後他のAPIも実装していくことでさらに「おばあちゃんの知恵袋」からの情報を増やしていくことができると考えています。
### 注力したこと（こだわり等）
* **安心感** を与えられることを第一に考え、無機質なAI口調ではなく、 **温かみのあるおばあちゃん口調** であることに注力しました。
* 特に危険な行動をしようとしているときには、 **おばあちゃんが表情を変え**、忠告に危機感を持てるようにこだわりました。

## 開発技術
### 活用した技術
#### API・データ
* GeminiAPI 
* [天気予報 API](https://github.com/tsukumijima/weather-api)

#### フレームワーク・ライブラリ・モジュール
* Flask
* React
* MySQL

#### デバイス
* WindowsまたはMacのPC上で動作

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 事前開発は行っていないので、すべて2日間で開発しています
  * チームメンバーと当日に顔合わせ→アイデア出しから
  * チームメンバーのうち１人は開発経験ゼロ
  * 残業もゼロ（"ホワイト"！）
* 力を入れた部分  
  * [routes.py](https://github.com/jphacks/ng_2406/blob/main/backend/app/gemini_api.py)
  について、プロンプトを工夫してほしいデータを取得できるようにすることに力をいれた。
  * UIはシンプルでいて、ユーモアのあるものを目指した。
    * 個性を残しつつ良いUXを 
