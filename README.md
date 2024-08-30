# WhatsApp Business Group Chat Automation

This project automates the process of exporting and clearing chat history for WhatsApp Business groups using Appium and Python. The script reads group names from a text file and performs the following actions for each group:

1. Searches for the group in WhatsApp Business.
2. Exports the chat history to Google Drive.
3. Clears the chat history.
4. Repeats the process for each group listed in the `usernames.txt` file.

## Prerequisites

Before running this project, ensure you have the following installed:

### 1. Java Development Kit (JDK)

Appium requires Java to be installed on your system.

- **Download and install JDK:**
  - Visit the [Oracle JDK Download Page](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) and download the appropriate version for your OS.
  - Follow the installation instructions.

- **Set up the JAVA_HOME environment variable:**
  - On Windows:
    1. Right-click on `This PC` or `My Computer` and select `Properties`.
    2. Click on `Advanced system settings`.
    3. Click on `Environment Variables`.
    4. Under `System variables`, click `New` and add `JAVA_HOME` as the variable name and the path to your JDK installation as the variable value.
    5. Add `; %JAVA_HOME%\bin` to the end of the `Path` variable under `System variables`.

  - On macOS/Linux:
    - Add the following lines to your `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc` file:
      ```bash
      export JAVA_HOME=/path/to/your/jdk
      export PATH=$JAVA_HOME/bin:$PATH
      ```
    - Replace `/path/to/your/jdk` with the actual path to your JDK installation.
    - Run `source ~/.bash_profile` or `source ~/.zshrc` to apply the changes.

### 2. Android SDK

The Android SDK is required for Appium to interact with your Android device.

- **Download and install Android Studio:**
  - Visit the [Android Studio Download Page](https://developer.android.com/studio) and download Android Studio.
  - Install Android Studio, which includes the Android SDK.

- **Set up the ANDROID_HOME environment variable:**
  - On Windows:
    1. Right-click on `This PC` or `My Computer` and select `Properties`.
    2. Click on `Advanced system settings`.
    3. Click on `Environment Variables`.
    4. Under `System variables`, click `New` and add `ANDROID_HOME` as the variable name and the path to your Android SDK installation (e.g., `C:\Users\YourUserName\AppData\Local\Android\Sdk`) as the variable value.
    5. Add `; %ANDROID_HOME%\tools; %ANDROID_HOME%\platform-tools` to the end of the `Path` variable under `System variables`.

  - On macOS/Linux:
    - Add the following lines to your `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc` file:
      ```bash
      export ANDROID_HOME=$HOME/Library/Android/sdk
      export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
      ```
    - Run `source ~/.bash_profile` or `source ~/.zshrc` to apply the changes.

### 3. Appium

- **Install Appium:**
  - Install Node.js from [Node.js Downloads](https://nodejs.org/en/download/).
  - After installing Node.js, open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS/Linux) and install Appium globally:
    ```bash
    npm install -g appium
    appium driver install uiautomator2 - Android
    appium driver install espresso - Android
    appium driver install xcuitest - IOS
    ```
    appium version is = 2.4.1

- **Start the Appium server:**
  - In your terminal, start the Appium server by running:
    ```bash
    appium -p 4724
    ```

### 4. Appium Inspector

Appium Inspector is a graphical tool that helps you inspect mobile apps for elements.

- **Download and install Appium Inspector:**
  - Visit the [Appium Inspector GitHub Page](https://github.com/appium/appium-inspector/releases) and download the latest version for your OS.
  - Install and run Appium Inspector to inspect your mobile app's UI elements.

### 5. Python and Dependencies

- **Install Python 3.x:**
  - Download and install Python from the [Python official site](https://www.python.org/downloads/).

- **Install the required Python packages:**
  - Open a terminal and install the necessary packages using pip:
    ```bash
    pip install selenium appium-python-client
    ```

## Usage

1. **Modify the script with your device details:**

    - Update the `platform_version` and `device_name` in the script to match your Android device.

    ```python
    options.platform_version = "Your Android version"
    options.device_name = "Your device ID"
    ```

2. **Prepare the `usernames.txt` file:**

    - Create a `usernames.txt` file in the same directory as your script.
    - Add the names of the WhatsApp groups, each on a new line.

1. Enter Group Names using Tkinter Script
You can use a Tkinter-based GUI to enter the WhatsApp group names that you want to process. This script allows you to enter the names through a simple interface, and it will save them to the usernames.txt file.

Run the Tkinter script:

tkinter_script.exe
Enter the WhatsApp group names in the text area, each on a new line.

Click the "Save" button to save the group names to usernames.txt.

2. Select Data for Processing using Tkinter
A Tkinter-based GUI allows you to select the data that you want to process. This is useful if you want to selectively process certain groups or specific types of data and it file run automation.py programme automatically

Run the Tkinter selection script:

tkinter_print.exe
Select the group names or data types that you want to process.

Click the "Process" button to initiate the automation script for the selected items.

3. Extract Google Drive Zip Files
If your exported chat history from WhatsApp Business is in a zip format, you can use this script to extract and convert the zip files into readable text files.

Place the Google Drive zip files in the appropriate directory.

Run the extraction script:

extract_file.exe

The script will extract the contents and convert them to readable text files, which will be saved in the output directory.
    ```

    The script will start processing each group, exporting the chat history to Google Drive, and clearing the chat.

## Logging

The script uses Python's `logging` module to log the process. Logs will be displayed in the terminal with timestamps and log levels, indicating the progress and any errors encountered.

## Troubleshooting

- **Element Not Found:** If the script fails to find an element, verify the XPath or Accessibility ID used. You may need to update these values if WhatsApp Business is updated or if the UI is different on your device.
  
- **Connection Issues:** Ensure your device is properly connected and recognized by your computer. You can verify the connection with:

    ```bash
    adb devices
    ```

- **Appium Issues:** Ensure your Appium server is running and accessible at the specified `command_executor` URL.

## Contributing

Feel free to contribute to this project by submitting a pull request or opening an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
