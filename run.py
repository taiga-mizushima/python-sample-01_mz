import controller.controller as Ctrl
from entity.entity import DataClassCard
import repository.repository as Rep

def main():
    print("Hello World!")

if __name__ == "__main__":

    # データ準備
    data1 = DataClassCard("20230212", "AAA", "1", 100)
    data2 = DataClassCard("20230212", "BBB", "0", 200)

    Rep.insert(data1)
    Rep.insert(data2)

    Ctrl.execute()