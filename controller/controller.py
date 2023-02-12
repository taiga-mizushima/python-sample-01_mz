from entity.entity import DataClassCard
import repository.repository as Rep

def execute():

    # データ準備
    data1 = DataClassCard("20230212", "AAA", "1", 100)
    data2 = DataClassCard("20230212", "BBB", "0", 200)

    Rep.insert(data1)
    Rep.insert(data2)

    print("DataClassの内容を出力")
    for item in Rep.read():
        print(item)
    
    # Pandas変換
    df = Rep.convert_to_dataframe()
    print("Pandas変換後の内容を出力")
    print(df)