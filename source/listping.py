import argparse  # from std
import os


def Retrive(input_file_path):
    with open(input_file_path, 'r', encoding='UTF-8') as file:
        for host in file:
            try:
                # 去除斷行字元
                host = host.replace("\n", " ")
                response = os.system("ping -n 1" + " " + host)
                # and then check the response...
                if response == 0:
                    print("測試結果" + host, ': 回應上線中')
                else:
                    print("測試結果" + host, ': 無回應')
            except Exception as e:
                print("測試結果" + host + ':', e)


def main():

    # 準備參數解析
    example_text = "example usage: py.exe .\listping.py example_hosts_list.txt"
    parser = argparse.ArgumentParser(
        description="依給定主機清單偵測是否上線", epilog=example_text)
    parser.add_argument("input_file_path", help="主機清單檔案位置",
                        type=str, )
    args = parser.parse_args()

    # 執行函數
    Retrive(args.input_file_path)

    # end
    print("程式執行完畢")
    print()


if __name__ == "__main__":
    main()
