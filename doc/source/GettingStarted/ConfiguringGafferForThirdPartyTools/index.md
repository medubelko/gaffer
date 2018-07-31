# Configuring Gaffer for Third-Party Tools #

Gaffer is shipped with Appleseed, an open-source renderer, which requires no additional configuration. Gaffer is further compatible with the following third-party tools:
* Arnold
* 3Delight
* Tractor

In order to make Gaffer interact with these tools, you will need to set some additional [environment variables](../SettingUpGafferCommand/index.md).

> Note :
> For the purposes of these instructions, we will assume you are using the bash shell and are familiar with terminal commands. Other shells will have comparable methods for setting environment variables.


## Configuring Gaffer for Arnold ##

You will add a `ARNOLD_ROOT` environment variable that points to the Arnold directory. Before you begin, make sure that Arnold is correctly installed and configured, and close any open instances of Gaffer.

### Linux ###

> Note :
> For the purposes of this instruction, we will assume you have Arnold !ARNOLD_VERSION! installed to `!ARNOLD_PATH_LINUX!`

To add the `ARNOLD_ROOT` environment variable in Linux:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export ARNOLD_ROOT=!ARNOLD_PATH_LINUX!
    ```
2. Save, and close the text editor.
3. In a terminal, reload the user configuration file, and then verify the variable is set:
    ```shell
    user@desktop ~ $ source ~/.bash_profile
    user@desktop ~ $ echo $ARNOLD_ROOT
    !ARNOLD_PATH_LINUX!
    ```
4. The next time you open Gaffer, the Arnold nodes will be available.
    <!-- ![Arnold node menu](images/arnoldNodes.png) -->

### OSX ###

> Note :
> For the purposes of this instruction, we will assume you have Arnold !ARNOLD_VERSION! installed to `!ARNOLD_PATH_OSX!`

To add the `ARNOLD_ROOT` environment variable in OSX:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export ARNOLD_ROOT=!ARNOLD_PATH_OSX!
    ```
2. Save, and close the text editor.
3. In a terminal (**Applications** > **Utilities** > **Terminal**), reload the user configuration file, and then verify the variable is set:
    ```shell
    MacBook:~ user$ source ~/.bash_profile
    MacBook:~ user$ echo $ARNOLD_ROOT
    !ARNOLD_PATH_OSX!
    ```
4. The next time you open Gaffer, the Arnold nodes will be available.
    <!-- ![Arnold node menu](images/arnoldNodes.png) -->


## Configuring Gaffer for 3Delight ##

You will add a `DELIGHT` environment variable that points to the 3Delight directory. Before you begin, make sure that 3Delight is correctly installed and configured, and close any open instances of Gaffer.

### Linux ###

> Note :
> For the purposes of this instruction, we will assume you have 3Delight !DELIGHT_VERSION! installed to `!DELIGHT_PATH_LINUX!`

To add the `DELIGHT` environment variable in Linux:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export DELIGHT=!DELIGHT_PATH_LINUX!
    ```
2. Save, and close the text editor.
3. In a terminal, reload the user configuration file, and then verify the variable is set:
    ```shell
    user@desktop ~ $ source ~/.bash_profile
    user@desktop ~ $ echo $DELIGHT
    !DELIGHT_PATH_LINUX!
    ```
4. The next time you open Gaffer, the 3Delight nodes will be available.
    <!-- ![Delight node menu](images/delightNodes.png) -->

### OSX ###

> Note :
> For the purposes of this instructions, we will assume you have DELIGHT !DELIGHT_VERSION! installed to `!DELIGHT_PATH_OSX!`.

To add the `DELIGHT` environment variable in OSX:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export DELIGHT=!DELIGHT_PATH_OSX!
    ```
2. Save, and close the text editor.
3. In a terminal (**Applications** > **Utilities** > **Terminal**), reload the user configuration file, and then verify the variable is set:
    ```shell
    MacBook:~ user$ source ~/.bash_profile
    MacBook:~ user$ echo $DELIGHT
    !DELIGHT_PATH_OSX!
    ```
4. The next time you open Gaffer, the 3Delight nodes will be available.
    <!-- ![Delight node menu](images/delightNodes.png) -->


## Configuring Gaffer for Tractor ##

Before you begin, make sure that Tractor is correctly installed and configured.
You will add the location of the Tractor python module to the `PYTHONPATH` environment variable.


### Linux ###

> Note :
> For the purposes of this instruction, we will assume you have Tractor !TRACTOR_VERSION! installed to `!TRACTOR_PATH_LINUX!`.

To add the Tractor python module to the `PYTHONPATH` environment variable in Linux:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export PYTHONPATH=$PYTHONPATH\:!TRACTOR_PATH_LINUX!/python2.7/site-packages
    ```
2. Save, and close the text editor.
3. In a terminal, reload the user configuration file, and then verify the variable is set:
    ```shell
    user@desktop ~ $ source ~/.bash_profile
    user@desktop ~ $ echo $PYTHONPATH
    /usr/bin/python2.7:/usr/lib/python2.7:!TRACTOR_PATH_LINUX!/python2.7/site-packages
    ```
    > Note :
    > Depending on your system's configuration, the beginning of your `PYTHONPATH` variable might not appear exactly as above. What's important is whether the `!TRACTOR_PATH_LINUX!/python2.7/site-packages` location appears at the end.
4. The next time you open Gaffer, Tractor will be available in the dispatch drop-down menu.
    <!-- ![Tractor dispatch](images/tractorDispatch.png) -->

### OSX ###

> Note :
> For the purposes of this instructions, we will assume you have Tractor !TRACTOR_VERSION! installed to `!TRACTOR_PATH_OSX!`.

To add the Tractor python module to the `PYTHONPATH` environment variable in OSX:

1. In a text editor, open the _bash_ user configuration file `~/.bash_profile`, and add the following line:
    ```
    export PYTHONPATH=$PYTHONPATH\:!TRACTOR_PATH_OSX!/python2.7/site-packages
    ```
2. Save, and close the text editor.
3. In a terminal (**Applications** > **Utilities** > **Terminal**), reload the user configuration file, and then verify the variable is set:
    ```shell
    MacBook:~ user$ source ~/.bash_profile
    MacBook:~ user$ echo $PYTHONPATH
    /Library/Frameworks/Python.framework/Versions/2.7/bin:!TRACTOR_PATH_OSX!/python2.7/site-packages
    ```
    > Note :
    > Depending on your system's configuration, the beginning of your `PYTHONPATH` variable might not appear exactly as above. What's important is whether the `!TRACTOR_PATH_OSX!/python2.7/site-packages` location appears at the end.
4. The next time you open Gaffer, Tractor will be available in the dispatch drop-down menu.
    <!-- ![Tractor dispatch](images/tractorDispatch.png) -->


## See Also ##

* [Setting up the "gaffer" command](../SettingUpGafferCommand/index.md)
* [Installing Gaffer](../InstallingGaffer/index.md)
