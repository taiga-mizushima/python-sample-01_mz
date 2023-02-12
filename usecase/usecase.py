import repository.repository as Rep
from entity.entity import DataClassCard

def execute():

    print("01.DataClassの内容を出力")
    for item in Rep.read():
        print(item)
    print("\n")
    
    # DataClass → Pandas変換
    # あくまでDataClass(entity)が基本。
    # Pandas変換はrepositoryに変換メソッドを準備し、一時的な利用とする。
    df = Rep.class_to_frame()
    print("02.Pandas変換後の内容を出力")
    print(df)
    print("\n")

    # Pandas → DataClass変換
    # この後データ登録する場合は、PandasからDataClass(entity)に戻して操作する。
    outlist = Rep.frame_to_class(df)
    print("03.再びDataClass変換後の内容を出力")
    for item in outlist:
        print(item)