# Using Custom Servers

TOH is designed to be able to be used on official servers, but may experience temporary issues on official servers due to server-side changes or other factors.  
You can use custom servers for more stable experience that is not affected by official server-side changes.

!!! warning
    Using custom servers is only supported on Windows/Android/iOS. You cannot use custom servers on Nintendo Switch, etc.

## Using Public Custom Servers

You can use public custom servers maintained by third-party volunteers. Here is how to connect to public servers maintained by [miniduikboot](https://github.com/miniduikboot) and [GD825](https://github.com/GD825)[^1].

### :fontawesome-brands-windows:{ .s-color-windows } Windows

1. Download the auto-install batch file (Created by: [GD825](https://github.com/GD825))  

    [:material-download: Download Auto Installer](https://github.com/GD825/regioninfo/releases/download/V3A/Custom_server.bat){ .md-button .s-button--filled .s-style }

1. Double-click the downloaded file (`Custom_server.bat`) and run it
1. Start Among Us and make sure custom regions are added to the server selections

Once you have done this, you do not need to do any additional actions again as long as the regions are not removed.

!!! info
    Depending on the future situation, we may make TOH add custom regions automatically.

!!! tip
    If you have installed one of certain mods before, you may already have custom regions that this step adds. In that case, you do not need to do anything.

### :fontawesome-brands-android:{ .s-color-android } Android / :fontawesome-brands-apple:{ .s-color-apple } iOS

1. View this page in your device's browser
1. Start Among Us and go to the online menu

    [:material-rocket-launch: Start Among Us](amongus:){ .md-button .s-button--outlined .s-style }  

1. Keep Among Us running and switch back to the browser
1. Tap the button for the region you want to add below (you can add multiple at once)

    [:material-plus-circle: Add Modded_AS (Asia) Region](amongus://init?servername=Modded_AS&serverport=443&serverip=https%3A%2F%2Fau-as.duikbo.at&usedtls=false){ .md-button .s-button--filled .s-style }  

    [:material-plus-circle: Add Modded_NA (North America) Region](amongus://init?servername=Modded_NA&serverport=443&serverip=https%3A%2F%2Faumods.org&usedtls=false){ .md-button .s-button--filled .s-style }  

    [:material-plus-circle: Add Modded_EU (Europe) Region](amongus://init?servername=Modded_EU&serverport=443&serverip=https%3A%2F%2Fau-eu.duikbo.at&usedtls=false){ .md-button .s-button--filled .s-style }  

1. Go back to Among Us and you will find custom regions that you have added in the server selection

Once you have done this, you can connect to custom regions without any additional actions.

## (For Advanced Users) Hosting and Using a Private Custom Server

You can also set up your own custom server using [Impostor](https://github.com/Impostor/Impostor) or other tools. See the Impostor documentation for details.

!!! warning
    To use TOH with your server, be sure to set the [`AllowHostAuthority` option](https://github.com/Impostor/Impostor/blob/master/docs/Server-configuration.md#compatibility) to `true`.  
    TOH will not work properly without this setting.

[^1]: Reference: [Among Us Custom Server - TOWN OF HOST MODS](https://aumods.org/)
