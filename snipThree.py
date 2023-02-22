import pickle


class SnipThree:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


if __name__ == "__main__":
    st = SnipThree()
    with open("snipThree.pickle", "wb") as f:
        pickle.dump(st, f, pickle.HIGHEST_PROTOCOL)

    with open("snipThree.pickle", "rb") as f:
        st2 = pickle.load(f)
