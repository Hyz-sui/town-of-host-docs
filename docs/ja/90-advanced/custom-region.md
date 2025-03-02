# カスタムサーバーを使用する

TOHはカスタムサーバーを必要とせず公式サーバー上で動作するように設計されたmodですが，サーバー側の仕様変更等により一時的に公式サーバー上で正常に動作しなくなることがあります．  
カスタムサーバーを使用することで，公式サーバーの仕様変更に左右されず，より安定したプレイを楽しむことができます．  

!!! warning
    カスタムサーバーはWindows/Android/iOSでのみサポートされています．Switch等では使用できません

## 公開カスタムサーバーを使用する
<!-- TODO: スクリーンショット等を追加する -->

有志によって運営されている公開カスタムサーバーを利用できます．ここでは，[miniduikboot](https://github.com/miniduikboot)氏と[GD825](https://github.com/GD825)氏によって運営されている公開サーバーに接続する方法について説明します[^1]．

### :fontawesome-brands-windows:{ .s-color-windows } Windows

1. 自動インストール用のバッチファイルをダウンロードする (作: [GD825](https://github.com/GD825)氏)  

    [:material-download: 自動インストーラをダウンロード](https://github.com/GD825/regioninfo/releases/download/V3A/Custom_server.bat){ .md-button .s-button--filled .s-style }

1. ダウンロードされたファイル(`Custom_server.bat`)をダブルクリックして実行する
1. Among Usを起動し，サーバー選択にカスタムリージョンが追加されていることを確認する

一度この手順を行えば，リージョンを削除しない限り再び追加の操作を行う必要はありません

!!! info
    今後の状況により，TOHをインストールすれば追加の操作なしでカスタムリージョンを使用できるように変更する可能性があります

!!! tip
    特定のmodを使用したことがある場合，この手順でインストールされるものと同じカスタムリージョンがすでに追加されていることがあります．その場合は上記の手順を踏む必要はありません

### :fontawesome-brands-android:{ .s-color-android } Android / :fontawesome-brands-apple:{ .s-color-apple } iOS

1. デバイスのブラウザでこのページを表示する
1. Among Usを起動し，オンラインの画面を開く

    [:material-rocket-launch: Among Usを起動する](amongus:){ .md-button .s-button--outlined .s-style }  

1. Among Usが起動した状態のまま，画面をブラウザに切り替える
1. 以下から追加したいリージョンのボタンを押す(一度に複数追加できます)

    [:material-plus-circle: Modded_AS(アジア)リージョンを追加する](amongus://init?servername=Modded_AS&serverport=443&serverip=https%3A%2F%2Fau-as.duikbo.at&usedtls=false){ .md-button .s-button--filled .s-style }  

    [:material-plus-circle: Modded_NA(北米)リージョンを追加する](amongus://init?servername=Modded_NA&serverport=443&serverip=https%3A%2F%2Faumods.org&usedtls=false){ .md-button .s-button--filled .s-style }  

    [:material-plus-circle: Modded_EU(欧州)リージョンを追加する](amongus://init?servername=Modded_EU&serverport=443&serverip=https%3A%2F%2Fau-eu.duikbo.at&usedtls=false){ .md-button .s-button--filled .s-style }

1. Among Usに戻り，サーバー選択にカスタムリージョンが追加されていることを確認する

一度この手順を行えば，以降は追加の操作なしでカスタムリージョンを使用できます

## (上級者向け)非公開カスタムサーバーをホストして使用する

[Impostor](https://github.com/Impostor/Impostor)等を使用し，自分でカスタムサーバーを立ち上げることもできます．詳細についてはImpostorの説明を参照してください．

!!! warning
    TOHを使用するためにカスタムサーバーをホストする場合，必ず[`AllowHostAuthority`オプション](https://github.com/Impostor/Impostor/blob/master/docs/Server-configuration.md#compatibility)を`true`に設定してください  
    この設定を行わない場合，TOHは正しく動作しません

[^1]: 出典: [Among Us Custom Server - TOWN OF HOST MODS](https://aumods.org/)
