import repository.repository as Rep
from entity.entity import DataClassCard

def execute():

    print("DataClassの内容を出力")
    for item in Rep.read():
        print(item)
    
    # DataClass → Pandas変換
    df = Rep.class_to_frame()
    print("Pandas変換後の内容を出力")
    print(df)

    # Pandas → DataClass変換
    outlist = Rep.frame_to_class(df)
    print("再びDataClass変換後の内容を出力")
    for item in outlist:
        print(item)