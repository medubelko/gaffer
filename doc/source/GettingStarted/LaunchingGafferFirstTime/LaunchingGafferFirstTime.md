# Launching Gaffer for the First Time #

Once Gaffer has been installed, you will probably want to try it out right away before performing any additional configuration. To launch it, you can run its application file directly from the binary directory.

> Note :
> For these instructions, we will assume your Gaffer install location is in the `/opt/` directory. If you have installed it elsewhere, replace `/opt/` with the directory you installed it to.

## Launching Gaffer for the First Time in Linux ##

To launch Gaffer for the first time:

1. Open a terminal.

2. Navigate to the Gaffer binary directory and run the Gaffer application:
    ```shell
    user@desktop ~ $ cd /opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin
    user@desktop /opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin $ ./gaffer
    ```

Gaffer will open in a new window.


## Launching Gaffer for the First Time in OSX ##

1. Open a terminal (**Finder** > **Go** > **Utilities** > **Terminal**).

2. Navigate to the Gaffer binary directory and run the Gaffer application:
    ```shell
    MacBook:~ user$ cd /opt/gaffer-!GAFFER_OSX_PACKAGE!-osx/bin
    MacBook:/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx/bin user$ ./gaffer
    ```

Gaffer will open in a new window.

> Caution : 
> When you run Gaffer from a terminal, its continued operation is dependent on that terminal window. If you close the terminal window, it will also close Gaffer, and you may lose any unsaved data.

## See Also ##

* [Installing Gaffer](../InstallingGaffer/InstallingGaffer.md)
* [Setting up the "gaffer" command](../SettingUpGafferCommand/SettingUpGafferCommand.md)
* [Configuring Gaffer for Third-Party Tools](../ConfiguringGafferForThirdPartyTools/ConfiguringGafferThirdPartyTools.md)
