# Setting Up the "gaffer" Command #

After you have installed Gaffer, it will remain a collection of files and directories on your file system. Because it is not yet configured as a command, your operating system will not recognize it in the terminal unless you execute it from its install directory every time. This could become very tedious, so we recommend that you modify your terminal's `PATH` _environment variable_ to access the `gaffer` command.

### Environment Variables ###

An environment variable is simply a value, such as a string, number, boolean, or location that your terminal is aware of. For instance, when you ran the `tar` command to extract the downloaded Gaffer package, the `tar` command was not located in your `~/Downloads` folder, but actually in `/usr/bin/`. Whenever you open your terminal, several folders are added to your terminal's `PATH` environment variable, which provides your terminal with a list of locations in your file system from which it can source commands.

In order for the `gaffer` command to work in your terminal, you will need to add your Gaffer's install location to the `PATH` environment variable.


## Setting Up the "gaffer" Command in Linux ##

Depending on your Linux distribution and how it was configured, you may be running a different type of terminal. Most distributions of Linux use the common terminal _bash_, but there are others available, like _tcsh_. Because we cannot accommodate every available terminal, we will only provide instructions for editing the `PATH` variable in _bash_ and _tcsh_.

> Tip : 
> If you are not sure which terminal you are using, you can find its name by opening a terminal and typing: `echo $0`, which will return `/bin/bash`, `tcsh`, or some equivalent. If you are not using _bash_ or _tcsh_, the same principles of environment variables will apply, and your terminal's documentation should provide a comparable way of modifying the `PATH` variable.

> Note :
> For the purposes of this procedure, we will assume you have Gaffer installed to `/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux`.

To set up the `gaffer` command:

1. Open a terminal.

2. Use a text editor, such as _gedit_ or _vim_, to open your terminal's user configuration file:
    
    * _bash_ configuration file: `/.bashrc`
    * _tcsh_ configuration file: `/.tcshrc`

3. At the end of the file, append the location of Gaffer's binary directory to the end of the `PATH` variable:
    * _bash_: `export PATH=$PATH\:/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin`
    * _tcsh_: `setenv PATH=$PATH\:/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin`

4. Save, and close your text editor.

5. In the terminal, reload the user configuration file and test that the `PATH` variable has been updated:
    
    * _bash_:
    ```shell
    user@desktop ~ $ source ~/.bash_profile
    user@desktop ~ $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin
    ```
    
    * _tcsh_:
    ```shell
    user@desktop ~ $ source ~/.tcsh_profile
    user@desktop ~ $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin
    ```
    
    > Note :
    > Depending on your system configuration, the beginning of your `PATH` variable might not appear exactly as above. What's important is whether the `/opt/gaffer-!GAFFER_LINUX_PACKAGE!-linux/bin` location appears at the end.

`gaffer` is now a command you can execute from any directory in the terminal.


## Setting Up the "gaffer" Command in OSX ##

OSX's default terminal is _bash_, so you will be adding to the `PATH` variable by editing _bash's_ user config.

> Note :
> For the purposes of this procedure, we will assume you have Gaffer installed to `/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx`.

To set up the `gaffer` command in OSX:

1. Open a terminal.

2. Create and edit _bash's_ user configuration file:

    ```shell
    MacBook:~ user$ touch ~/.bash_profile
    MacBook:~ user$ open ~/.bash_profile
    ```
    Your default text editor will open.

3. At the end of the file, append the location of Gaffer's binary directory to the end of the `PATH` variable:

    ```
    export PATH=$PATH\:/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx/bin
    ```

4. Reload the _bash_ user configuration file and test that the `PATH` variable has been updated:

    ```shell
    MacBook:~ user$ source ~/.bash_profile
    MacBook:~ user$ echo $PATH
    /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx/bin
    ```

    > Note :
    > Depending on your system configuration, the beginning of your `PATH` variable might not appear exactly as above. What's important is whether the `/opt/gaffer-!GAFFER_OSX_PACKAGE!-osx/bin` location appears at the end.

`gaffer` is now a command you can execute from any directory in the terminal.


## Using the "gaffer" Command ##

Once you have added Gaffer to the `PATH` variable, you can enter the command `gaffer`, and Gaffer will now launch from any directory in the terminal.

### Linux ###

```shell
user@desktop ~ $ gaffer
```

### OSX ###

```shell
MacBook:~ user$ gaffer
```

## Opening Gaffer Graphs in the Terminal ##

You can also use the command to open Gaffer graphs you have created.


### Linux ###

```shell
user@desktop ~ $ cd ~/gaffer/projects/default/scripts
user@desktop ~/projects/default/scripts $ ls
myFirstProject.gfr  mySecondProject.gfr
user@desktop ~/projects/default/scripts $ gaffer myFirstProject.gfr
```


### OSX ###

```shell
MacBook:~ user$ cd ~/gaffer/projects/default/scripts
MacBook:~/gaffer/projects/default/scripts user$ ls
myFirstProject.gfr  mySecondProject.gfr
MacBook:~/gaffer/projects/default/scripts user$ gaffer myFirstProject.gfr
```


## See Also ##

* [Installing Gaffer](../InstallingGaffer/InstallingGaffer.md)
* [Configuring Gaffer for third-party tools](../ConfiguringGafferForThirdPartyTools/ConfiguringGafferForThirdPartyTools.md)
