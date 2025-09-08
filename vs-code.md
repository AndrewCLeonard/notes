# VS Code Lessons Learned

## Basic Keyboard Shortcuts

Some I know, some I've never used. Learning what all of them are for will help me get faster.

| Category                   | Action                       | Windows/Linux                       | macOS                             |
| -------------------------- | ---------------------------- | ----------------------------------- | --------------------------------- |
| Basic Editing              | Copy Line Up/Down            | Alt + Shift + Up/Down               | Option + Shift + Up/Down          |
|                            | Move Line Up/Down            | Alt + Up/Down                       | Option + Up/Down                  |
|                            | Delete Line                  | Ctrl + Shift + K                    | Cmd + Shift + K                   |
|                            | Insert Line Below/Above      | Ctrl + Enter / Ctrl + Shift + Enter | Cmd + Enter / Cmd + Shift + Enter |
|                            | Comment/Uncomment Line       | Ctrl + /                            | Cmd + /                           |
|                            | Toggle Block Comment         | Shift + Alt + A                     | Shift + Option + A                |
| Navigation & Search        | Go to Definition             | F12                                 | Cmd + Click                       |
|                            | Quick Open File              | Ctrl + P                            | Cmd + P                           |
|                            | Go to File...                | Ctrl + P                            | Cmd + P                           |
|                            | Go to Line...                | Ctrl + G                            | Cmd + G                           |
|                            | Find                         | Ctrl + F                            | Cmd + F                           |
|                            | Replace                      | Ctrl + H                            | Cmd + H                           |
|                            | Find Next/Previous           | F3 / Shift + F3                     | Cmd + G / Cmd + Shift + G         |
| File & Window Management   | Toggle Sidebar Visibility    | Ctrl + B                            | Cmd + B                           |
|                            | New File                     | Ctrl + N                            | Cmd + N                           |
|                            | Save                         | Ctrl + S                            | Cmd + S                           |
|                            | Save As...                   | Ctrl + Shift + S                    | Cmd + Shift + S                   |
|                            | Close Editor                 | Ctrl + W                            | Cmd + W                           |
|                            | Close All Editors            | Ctrl + K W                          | Cmd + K W                         |
|                            | Split Editor                 | Ctrl + \\                           | Cmd + \\                          |
|                            | Toggle Full Screen           | F11                                 | Ctrl + Cmd + F                    |
| Code Editing & Refactoring | Trigger Suggest/IntelliSense | Ctrl + Space                        | Cmd + Space                       |
|                            | Format Document              | Shift + Alt + F                     | Shift + Option + F                |
|                            | Rename Symbol                | F2                                  | Cmd + F2                          |
|                            | Go to Symbol in File...      | Ctrl + Shift + O                    | Cmd + Shift + O                   |
| Terminal & Debugging       | Toggle Integrated Terminal   | Ctrl + \`                           | Cmd + \`                          |
|                            | Start Debugging              | F5                                  | F5                                |
|                            | Step Over                    | F10                                 | F10                               |
|                            | Step Into                    | F11                                 | F11                               |

## `code` CLI

| Command                                  | Description                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------- |
| `code`                                   | Open Visual Studio Code.                                                      |
| `code .`                                 | Open the current directory in Visual Studio Code.                             |
| `code -n`                                | Open a new instance of Visual Studio Code.                                    |
| `code -n .`                              | Open the current directory in a new instance of Visual Studio Code.           |
| `code file1.txt file2.txt`               | Open multiple files at once in Visual Studio Code.                            |
| `code -g file.txt:line[:column]`         | Open a file at a specific line (and optionally column) in Visual Studio Code. |
| `code --diff file1.txt file2.txt`        | Open two files in side-by-side comparison mode in Visual Studio Code.         |
| `code --add path/to/folder`              | Add a folder to the current workspace in Visual Studio Code.                  |
| `code --list-extensions`                 | List all installed extensions in Visual Studio Code.                          |
| `code --install-extension extensionName` | Install an extension by its identifier in Visual Studio Code.                 |
| `code --locale=es`                       | Launch Visual Studio Code with a specific locale (e.g., Spanish).             |
