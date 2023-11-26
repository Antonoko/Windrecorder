![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/product-header-cn.jpg)
<h1 align="center"> 🦝 Windrecorder | 捕風記錄儀</h1>
<p align="center"> Windows 上での <a href="https://www.rewind.ai/">Rewind</a> の代替ツールで、メモリクーを取り戻すのに役立ちます。</p>

<p align="center"> <a href="https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/README-en.md">English</a>  | <a href="https://github.com/yuka-friends/Windrecorder/blob/main/README.md">简体中文</a> | <a href="https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/README-ja.md">日本語</a> </p>

---

画面を継続的に記録し、キーワード検索などでいつでも思い出を呼び出すことができるツールです。

**そのすべての機能 (記録、認識処理、ストレージ トレースバックなど) は完全にローカルで実行され、インターネット接続やデータのアップロードは必要なく、実行すべきことのみを実行します。 **

![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/product-preview-cn.jpg)

> [!警告]
>
> 🤯 このプロジェクトはまだ開発の初期段階にあり、経験や使用においていくつかの小さな問題が発生する可能性があります。 この問題に遭遇した場合は、問題のフィードバックを送信し、更新情報に注意してください。

# 🦝 インストール

## 自動インストール (準備ができていません)

[Releases](https://github.com/yuka-friends/Windrecorder/releases)から統合パッケージをダウンロードし、データを格納したいディレクトリに解凍して使用します。


## 手動インストール

- [ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) をダウンロードし、bin ディレクトリ内の ffmpeg.exe を `C:\Windows\System32` (または他のディレクトリ) に解凍します。 PATH にあります)

- [Git](https://git-scm.com/downloads)、[Python](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)をインストール) (インストール中に python.exe を PATH に追加するをチェックします)、[Pip](https://pip.pypa.io/en/stable/installation/);
     - **知らせ！ 現在、Python 3.12** はサポートされていないため、上記のリンクで示されているバージョンである Python 3.10 を使用することをお勧めします。

- このツールをインストールするディレクトリに移動し (十分なスペースのあるパーティションに配置することをお勧めします)、ターミナル コマンド `git clone https://github.com/yuka-friends/ を使用してツールをダウンロードします。ウィンドレコーダー`;

     - インストールするフォルダーを開き、パスバーに「cmd」と入力して Enter キーを押し、現在のディレクトリターミナルに入り、上記のコマンドを貼り付けて Enter キーを押して実行します。

- ディレクトリ内の「install_update_setting.bat」を開いて、ツールをインストールして設定し、問題がなければ使用を開始できます。

     - ネットワーク上の理由によりエラーが報告された場合は、プロキシ `set https_proxy=http://127.0.0.1:xxxx` を追加するか、メインランド [ミラー ソース] (https://mirrors.tuna.tsinghua.edu.cn) を追加できます。 /help/pypi/);


#🦝使い方

現在、ツールを使用するには、ディレクトリ内のバッチ スクリプトを開く必要があります。

- ディレクトリ内の「start_record.bat」を開いて画面の記録を開始します。

> 注: 記録するには、ターミナル ウィンドウを最小化したままにし、バックグラウンドで実行する必要があります。 同様に、録音を一時停止する必要がある場合は、ターミナル ウィンドウを閉じるだけです。

- ディレクトリ内の「start_webui.bat」を開き、トレースバック、メモリのクエリ、および設定を行います。

> ベストプラクティス: WebUI で起動時に自動的に開始するように「start_record.bat」を設定すると、手間をかけずにすべてを記録できます。 コンピュータがアイドル状態で誰も使用していないとき、「start_record.bat」は自動的に録画を一時停止し、期限切れのビデオを圧縮してクリーンアップします。設定するだけで、あとは忘れてください。

---
### ロードマップ:
- [x] より小さいファイルサイズで安定した継続的な画面録画を実現
- [x] 変更された画像のみを識別し、データベースにインデックスを保存します
- [x] 完全なグラフィカル インターフェイス (webui)
- [x] ワードクラウド、タイムライン、ライトボックス、散布図のデータ概要
- [x] 録画後にクリップを自動的に識別し、空いた時間にビデオを自動的にメンテナンス、クリーンアップ、圧縮します。
- [x] 多言語サポート: インターフェイスおよび OCR 認識の i18n サポートが完了しました
- [ ] コードをリファクタリングして、より標準化され、開発が容易になり、パフォーマンスが向上します。
- [ ] ツールをパッケージ化し、より便利な使用モードを提供し、ユーザーフレンドリーにします
- [ ] 画面モダリティの認識を追加して、画面コンテンツの説明の検索を可能にします
- [ ] データベース暗号化機能を追加
- [ ] フォアグラウンドプロセス名を記録し、OCR ワードの対応する位置を記録して、検索時の手がかりとして表示します。
- [ ] 単語埋め込みインデックス、ローカル/API LLM クエリを追加
- [ ] マルチスクリーン録画サポートを追加 (pyautogui の将来の機能に応じて)
- [ ] 🤔


# 🦝 Q&A | よくある質問
Q: webui を開いたときに最近のデータがありません。

- A: start_record.bat がデータのインデックスを作成している場合、webui は最新の一時データベース ファイルを作成しません。 db ディレクトリ内のサフィックス _TEMP_READ.db を持つデータベース ファイルを削除し、start_record.bat のインデックス作成後に更新できます。 この戦略は将来的に修正され、リファクタリングされる予定です。 [#26](https://github.com/yuka-friends/Windrecorder/issues/26)

Q: WebUI を開くと、「FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません: './db\\user_2023-10_wind.db-journal'」というプロンプトが表示されます。

- A: 通常、start_record.bat がまだデータのインデックスを作成している間に、WebUI に初めてアクセスしたときに発生します。
解決策: start_record.bat のバックグラウンド インデックス作成が完了したら、db フォルダー内のサフィックス _TEMP_READ.db を持つ対応するデータベース ファイルを削除し、更新します。

Q: 記録中にマウスが点滅します

- A: Windows の歴史に残っている問題については、[この投稿](https://stackoverflow.com/questions/34023630/how-to-avoid-mouse-pointer-flicker-when-capture-a-window) を試してください。 -by-ffmpeg ) を解決するメソッド🤔。 (本当は慣れて気にならなくても大丈夫です(逃げ)

Q: Windows.Media.Ocr.Cli OCR が利用できない/認識率が低すぎる

- A1: ターゲット言語の言語パック/入力メソッドがシステムに追加されているかどうかを確認します: https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr

- A2: 以前のバージョンのデフォルト ポリシーでは、高さが 1500 を超える画面解像度は「高 DPI/高解像度画面」として扱われ、録画されるビデオ解像度は元の 4 分の 1 に低下します。 たとえば、3840x2160 の 4k モニターでは、録画されるビデオの解像度は 1920x1080 となり、OCR 認識精度の低下につながる可能性があります。 高解像度の画面で小さいフォントやスケーリングを使用する場合は、[録画とビデオの保存] でこのオプションをオフにし、元のビデオをより小さい値に圧縮する前に保存する日数を設定することで、ビデオを圧縮できます。ビデオ OCR インデックスからしばらく後のビデオ ボリューム。

- A3: Windows.Media.Ocr.Cli は、小さなテキストの認識率が低い場合があります。設定で「類似グリフ検索」オプションをオンにすると、検索時の再現ヒット率が向上します。

#🧡
以下のプロジェクトにヘルプが導入されました。

- https://github.com/DayBreak-u/chineseocr_lite

- https://github.com/zh-h/Windows.Media.Ocr.Cli


---

🧡 このツールは気に入りましたか? [YUKA NAGASE](https://www.youtube.com/channel/UCf-PcSHzYAtfcoiBr5C9DZA) の優しい音楽を聴く YouTube とストリーミング音楽プラットフォームへようこそ、ありがとう!

> "Your tools suck, check out my girl Yuka Nagase, she's amazing, I code 10 times faster when listening to her." -- @jpswing