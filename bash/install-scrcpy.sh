#!/bin/bash

# Packages requirements
sudo dnf install android-tools ffmpeg SDL2-devel ffms2-devel meson gcc make

# Dependencies requirements

# Android SDK installed

# Download Android SDK from https://developer.android.com/studio#downloads
tar xvfz android-studio-ide-201.6953283-linux.tar.gz 
mv android-studio ~/opt/android-studio-201.6953283
ln -s ~/opt/android-studio-201.6953283 ~/opt/android-studio
export ANDROID_SDK_ROOT=~/opt/android-studio

# Install Android SDK
cd ANDROID_SDK_ROOT/bin
./studio.sh

# Accept all licenses
yes | $ANDROID_SDK_ROOT/tools/bin/sdkmanager --licenses

# Oracle JDK15 from https://www.oracle.com/es/java/technologies/javase-jdk15-downloads.html
sudo rpm -Uvh jdk-15.0.1_linux-x64_bin.rpm 
sudo alternatives --config java
java -version

# Build and install scrcpy from https://raw.githubusercontent.com/Genymobile/scrcpy/master/BUILD.md
tar xvfz scrcpy-1.17.tar.gz
cd scrcpy-1.17/
meson x --buildtype release --strip -Db_lto=true # configure
ninja -Cx # build in directory x 
sudo ninja -Cx install # install from x to /usr/local/bin/scrcpy


# Permission with suitbit in adb, kill and start with persmission fixed
# from: https://stackoverflow.com/questions/14460656/android-debug-bridge-adb-device-no-permissions
sudo chown root:$USER /usr/bin/adb
sudo chmod 4550 /usr/bin/adb
lsusb
ls -l /dev/bus/usb/001/{028}
ls -l /dev/bus/usb/001/028
ps -ef  | grep adb
kill 714547
kill -9 714547
sudo adb start-server


# Run over tcpip instead cable
# https://futurestud.io/tutorials/how-to-debug-your-android-app-over-wifi-without-root


adb devices
adb disconnect 10.69.0.100:5555
#connect with usb
adb devices
adb tcpip 5555
#disconnect usb
adb devices
adb connect 10.69.0.100:5555

# remote connection from desktop
# INFO: scrcpy 1.17 <https://github.com/Genymobile/scrcpy>
/usr/local/bin/scrcpy
