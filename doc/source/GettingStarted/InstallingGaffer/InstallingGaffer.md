# Installing Gaffer #

Since the Gaffer packages hosted on the [Gaffer GitHub page](https://github.com/gafferhq/gaffer) are self-contained directories, you will need to manually install and configure them. Once extracted, the Gaffer directory contains the complete application ready for use.

> Note :
> As part of Unix/Linux/OSX best practices, we will be extracting Gaffer into the `/opt/` directory. However, you could extract it to anywhere on your file system.

## Installing in Linux ##

To install Gaffer in Linux:

1. Download the [latest Linux package of Gaffer](https://github.com/GafferHQ/gaffer/releases/download/!GAFFER_LINUX_PACKAGE!/gaffer-!GAFFER_LINUX_PACKAGE!-linux.tar.gz).

2. Open a terminal.

3. Extract the archive:
    ```shell
    user@desktop ~ $ cd ~/Downloads
    user@desktop ~/Downloads $ tar -xzf gaffer-!GAFFER_LINUX_PACKAGE!-linux.tar.gz -C /opt/
    ```

Gaffer is now installed to `/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux`


## Installing in OSX ##

To install Gaffer in OSX:

1. Download the [latest OSX package of Gaffer](https://github.com/GafferHQ/gaffer/releases/download/!GAFFER_OSX_PACKAGE!/gaffer-!GAFFER_OSX_PACKAGE!-osx.tar.gz).

2. Open a terminal (**Finder** > **Go** > **Utilities** > **Terminal**).

3. Extract the archive:
    ```shell
    MacBook:~ user$ cd ~/Downloads
    MacBook:~/Downloads user$ tar -xzf gaffer-!GAFFER_OSX_PACKAGE!-osx.tar.gz -C /opt/
    ```

Gaffer is now installed to `/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx`


## See Also ##

* [Launching Gaffer for the first time](../LaunchingGafferFirstTime/LaunchingGafferFirstTime.md)
* [Setting up the "gaffer" command](../SettingUpGafferCommand/SettingUpGafferCommand.md)
* [Configuring Gaffer for third-party tools](../ConfiguringGafferForThirdPartyTools/ConfiguringGafferForThirdPartyTools.md)
