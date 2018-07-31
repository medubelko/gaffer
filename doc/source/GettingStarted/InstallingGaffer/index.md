# Installing Gaffer #

Since the Gaffer packages hosted on the [Gaffer GitHub page](https://github.com/gafferhq/gaffer) are self-contained directories, you will need to manually install and configure them. Once extracted, the Gaffer directory contains the complete application ready for use.

> Note :
> As part of Unix/Linux/OSX best practices, we will be extracting Gaffer into the `/opt/` directory. However, you could extract it to anywhere on your file system.

## Installing in Linux ##

To install Gaffer in Linux:

1. Download the [latest Linux package of Gaffer](https://github.com/GafferHQ/gaffer/releases/download/!GAFFER_VERSION!/gaffer-!GAFFER_VERSION!-linux.tar.gz).

2. Open a terminal.

3. Extract the archive:
    ```shell
    user@desktop ~ $ cd ~/Downloads
    user@desktop ~/Downloads $ sudo tar -xzf gaffer-!GAFFER_VERSION!-linux.tar.gz -C /opt/
    ```

Gaffer is now installed to `/opt/gaffer-!GAFFER_VERSION!-linux`


## Installing in OSX ##

To install Gaffer in OSX:

1. Download the [latest OSX package of Gaffer](https://github.com/GafferHQ/gaffer/releases/download/!GAFFER_VERSION!/gaffer-!GAFFER_VERSION!-osx.tar.gz).

2. Open the terminal (Finder > Go > Utilities > Terminal).

3. Extract the archive:
    ```shell
    MacBook:~ user$ cd ~/Downloads
    MacBook:~/Downloads user$ tar -xzf gaffer-!GAFFER_VERSION!-osx.tar.gz -C /opt/
    ```

Gaffer is now installed to `/opt/gaffer-!GAFFER_VERSION!-osx`


## See Also ##

* [Launching Gaffer for the first time](../LaunchingGafferFirstTime/index.md)
* [Setting up the "gaffer" command](../SettingUpGafferCommand/index.md)
* [Configuring Gaffer for third-party tools](../ConfiguringGafferForThirdPartyTools/index.md)
