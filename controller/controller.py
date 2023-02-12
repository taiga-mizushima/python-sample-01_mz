import repository.repository as Rep

def execute():

    print("DataClassの内容を出力")
    for item in Rep.read():
        print(item)
    
    # Pandas変換
    df = Rep.convert_to_dataframe()
    print("Pandas変換後の内容を出力")
    print(df)