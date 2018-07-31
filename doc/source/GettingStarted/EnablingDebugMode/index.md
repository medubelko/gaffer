# Enabling Debug Mode #

By default, Gaffer will print only a limited subset of errors to the terminal. For fully debugging errors and diagnosing crashes, Gaffer can be launched using the [GNU Debugger](https://www.gnu.org/software/gdb/) in Linux and the [LLDB Debugger](https://lldb.llvm.org) in OSX. 

If you run into problems with Gaffer and request support from the [GitHub Issues](https://github.com/gafferHQ/gaffer/issues) page or the [Gaffer Google group](https://groups.google.com/forum/#!forum/gaffer-dev), you may be asked to provide stack traces from GDB/LLDB.

As with setting up the `gaffer` command, this will require setting an [environment variable](../SettingUpGafferCommand/index.md#environment_variables). For debugging, you will set `GAFFER_DEBUG` to `1` and then launch Gaffer.

> Note :
> For the purposes of these instructions, we will assume you have [set up the "Gaffer" command](../SettingUpGafferCommand/index.md).


## Enabling Debug Mode in Linux ##

As with other environment variables, the command to set the variable will depend on your terminal. Because we cannot accommodate every available terminal, we will only provide instructions for  _bash_ and _tcsh_.

> Tip : 
> If you are not sure which terminal you are using, you can find its name by opening a terminal and typing: `echo $0`, which will return `/bin/bash`, `tcsh`, or some equivalent. If you are not using _bash_ or _tcsh_, the same principles of environment variables will apply, and your terminal's documentation should provide a comparable way of modifying the `GAFFER_DEBUG` variable.

To launch Gaffer in debug mode:

1. Open a terminal.

2. Set the `GAFFER_DEBUG` environment variable:
    * _bash:_ `export GAFFER_DEBUG=1`
    * _tcsh:_ `setenv GAFFER_DEBUG 1`

3. Launch Gaffer with the `gaffer` command. Instead of a normal launch, the _gdb_ command will run in the terminal.

4. You will be prompted for what to do. Type `run` and hit <kbd>Enter</kbd>. Gaffer will launch as normal.

You will now be running Gaffer within _gdb_, and all errors you encounter will be printed to the terminal.

When you close Gaffer, _gdb_ will still be running. To exit _gdb,_ type `quit` and hit <kbd>Enter</kdb>.


## Enabling Debug Mode in OSX ##

As with setting other environment variables, you will be using your terminal.

To launch Gaffer in debug mode:

1. Open the terminal (**Finder** > **Go** > **Utilities** > **Terminal**).

2. Set the `GAFFER_DEBUG` environment variable:
    ```shell
    export GAFFER_DEBUG=1
    ```
3. Launch Gaffer with the `gaffer` command. Instead of a normal launch, the _lldb_ command will run in the terminal.

4. You will be prompted for what to do. Type `run` and hit <kbd>Enter</kbd>. Gaffer will launch as normal.

You will now be running Gaffer within _lldb_, and all errors you encounter will be printed to the terminal.

When you close Gaffer, _lldb_ will still be running. To exit _lldb,_ enter the following commands:

```shell
(lldb) quit
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y
```


## See Also ##

* [Installing Gaffer](../InstallingGaffer/index.md)
* [Setting up the "Gaffer" command](../SettingUpGafferCommand/index.md)