import os
import sys

def find_files(search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        for file in files:
            if file.find('.apk') != -1 and file.index('.apk')+4 == len(file):
                                        result.append(os.path.join(root, file))
            if file.find('.APK') != -1 and file.index('.APK')+4 == len(file):
                                        result.append(os.path.join(root, file))
    return result

def install_apk(apk_file_list):
    for i in apk_file_list:
        if(i == "./10040714_com.tencent.tmgp.sgame_a1987568_3.72.1.27_HHq1Qb.apk") or \
            (i == "./10040714_com.tencent.lolm_a1931885_3.0.0.5296_qLvjGX.apk"):
            cmd = "adb install --abi armeabi-v7a "
        else:
            cmd = "adb install "
        commands = cmd + i
        print("Excuting command => %s" %commands)
        os.system(commands)

def main():
    input_path="."
    apk_file_list = find_files(input_path)
    install_apk(apk_file_list)
    os.system("adb reboot")


if __name__ == '__main__':
    main()
